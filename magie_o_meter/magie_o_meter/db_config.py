import psycopg2

def inster_date_to_database(date_value, magie_value, impuls_value, bw_value):
    command = f"INSERT INTO values(date, magie, impuls, bw) VALUES (DATE '{date_value}', {magie_value}, {impuls_value}, {bw_value});"
    __execute_command(command)


def __execute_command(command):
    try:
        connection = psycopg2.connect(user = "jannusch",
                                      password = "",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "MagieOMeter")

        cursor = connection.cursor()
        print(connection.get_dsn_parameters(), "\n")

        cursor.execute(command)
        try:
            record = cursor.fetchone()
            print(f"You are connected to - {record} \n")
        except (Exception, psycopg2.Error) as error:
            print(f"Error while writing to PostgreSQL {error}")
        finally:
            connection.commit()

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL {error}")
    finally:
        # closing database connection
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

