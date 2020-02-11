--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.10
-- Dumped by pg_dump version 9.6.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: values; Type: TABLE; Schema: public; Owner: jannusch
--

CREATE TABLE public."values" (
    date date NOT NULL,
    magie integer,
    impuls integer,
    bw integer
);


ALTER TABLE public."values" OWNER TO jannusch;

--
-- Data for Name: values; Type: TABLE DATA; Schema: public; Owner: jannusch
--

COPY public."values" (date, magie, impuls, bw) FROM stdin;
2018-06-17	27	42	29
2018-06-18	24	48	31
2020-01-01	17	49	30
2020-01-02	19	45	31
2020-01-03	13	49	31
2020-01-04	14	47	30
2020-01-05	0	0	0
2020-01-06	19	54	31
2020-01-07	12	48	29
2020-01-08	19	57	32
2020-01-09	0	0	0
2020-01-10	0	0	0
2020-01-11	12	52	32
2020-01-12	15	47	29
2020-01-13	17	48	30
2020-01-14	0	0	0
2020-01-15	14	52	31
2020-01-16	12	47	31
2020-01-17	12	52	31
2020-01-18	14	49	30
2020-01-19	0	0	0
2020-01-20	17	51	29
2020-01-21	18	49	31
2020-01-22	12	51	27
2020-01-23	14	44	30
2020-01-24	14	57	29
2020-01-25	13	49	31
2020-01-26	11	51	32
2020-01-27	0	0	0
2020-01-28	12	53	31
2020-01-29	0	0	0
2020-01-30	12	49	29
2020-01-31	0	0	0
2020-02-01	0	0	0
2020-02-02	13	51	29
2020-02-03	13	47	34
2020-02-04	17	51	29
2020-02-05	15	47	29
2020-02-06	16	48	32
2020-02-07	0	0	0
2020-02-08	0	0	0
2020-02-09	0	0	0
2020-02-10	0	0	0
2019-01-01	0	0	0
2019-01-02	12	46	31
2019-01-03	12	51	30
2019-01-04	0	0	0
2019-01-05	18	49	34
2019-01-06	18	51	31
2019-01-07	0	0	0
2019-01-08	0	0	0
2019-01-09	0	0	0
2019-01-10	0	0	0
2019-01-11	17	53	34
2019-01-12	0	0	0
2019-01-13	0	0	0
2019-01-14	0	0	0
2019-01-15	13	47	32
2019-01-16	0	0	0
2019-01-17	0	0	0
2019-01-18	0	0	0
2019-01-19	11	46	32
2019-01-20	21	56	29
2019-01-21	17	49	28
2019-01-22	9	53	31
2019-01-23	0	0	0
2019-01-24	0	0	0
2019-01-25	0	0	0
2019-01-26	12	44	33
2019-01-27	0	0	0
2019-01-28	0	0	0
2019-01-29	0	0	0
2019-01-30	0	0	0
2019-01-31	0	0	0
2019-02-01	0	0	0
2019-02-02	0	0	0
2019-02-03	11	46	31
2019-02-04	14	52	31
2019-02-05	0	0	0
2019-02-06	0	0	0
2019-02-07	0	0	0
2019-02-08	17	51	32
2019-02-09	0	0	0
2019-02-10	0	0	0
2019-02-11	0	0	0
2019-02-12	12	54	30
2019-02-13	0	0	0
2019-02-14	0	0	0
2019-02-15	0	0	0
2019-02-16	0	0	0
2019-02-17	0	0	0
2019-02-18	0	0	0
2019-02-19	11	49	34
2019-02-20	17	54	31
2019-02-21	0	0	0
2019-02-22	0	0	0
2019-02-23	0	0	0
2019-02-24	0	0	0
2019-02-25	0	0	0
2019-02-26	0	0	0
2019-02-27	12	49	34
2019-02-28	0	0	0
2019-03-01	0	0	0
2019-03-02	0	0	0
2019-03-03	0	0	0
2019-03-04	15	51	31
2019-03-05	0	0	0
2019-03-06	0	0	0
2019-03-07	0	0	0
2019-03-08	0	0	0
2019-03-09	0	0	0
2019-03-10	0	0	0
2019-03-11	0	0	0
2019-03-12	0	0	0
2019-03-13	0	0	0
2019-03-14	0	0	0
2019-03-15	0	0	0
2019-03-16	0	0	0
2019-03-17	0	0	0
2019-03-18	0	0	0
2019-03-19	0	0	0
2019-03-20	0	0	0
2019-03-21	0	0	0
2019-03-22	0	0	0
2019-03-23	0	0	0
2019-03-24	0	0	0
2019-03-25	0	0	0
2019-03-26	0	0	0
2019-03-27	0	0	0
2019-03-28	0	0	0
2019-03-29	0	0	0
2019-03-30	0	0	0
2019-03-31	0	0	0
2019-04-01	0	0	0
2019-04-02	0	0	0
2019-04-03	0	0	0
2019-04-04	0	0	0
2019-04-05	0	0	0
2019-04-06	0	0	0
2019-04-07	0	0	0
2019-04-08	0	0	0
2019-04-09	0	0	0
2019-04-10	19	51	32
2019-04-11	21	52	30
2019-04-12	24	54	33
2019-04-13	0	0	0
2019-04-14	12	48	34
2019-04-15	12	53	31
2019-04-16	0	0	0
2019-04-17	0	0	0
2019-04-18	0	0	0
2019-04-19	17	51	32
2019-04-20	0	0	0
2019-04-21	0	0	0
2019-04-22	0	0	0
2019-04-23	0	0	0
2019-04-24	0	0	0
2019-04-25	0	0	0
2019-04-26	14	51	32
2019-04-27	0	0	0
2019-04-28	19	51	31
2019-04-29	0	0	0
2019-04-30	0	0	0
2019-05-01	0	0	0
2019-05-02	0	0	0
2019-05-03	0	0	0
2019-05-04	0	0	0
2019-05-05	0	0	0
2019-05-06	0	0	0
2019-05-07	0	0	0
2019-05-08	0	0	0
2019-05-09	0	0	0
2019-05-10	0	0	0
2019-05-11	0	0	0
2019-05-12	0	0	0
2019-05-13	0	0	0
2019-05-14	0	0	0
2019-05-15	0	0	0
2019-05-16	0	0	0
2019-05-17	0	0	0
2019-05-18	0	0	0
2019-05-19	0	0	0
2019-05-20	0	0	0
2019-05-21	0	0	0
2019-05-22	0	0	0
2019-05-23	0	0	0
2019-05-24	0	0	0
2019-05-25	0	0	0
2019-05-26	0	0	0
2019-05-27	0	0	0
2019-05-28	0	0	0
2019-05-29	0	0	0
2019-05-30	0	0	0
2019-05-31	0	0	0
2019-06-01	0	0	0
2019-06-02	0	0	0
2019-06-03	0	0	0
2019-06-04	0	0	0
2019-06-05	0	0	0
2019-06-06	0	0	0
2019-06-07	0	0	0
2019-06-08	0	0	0
2019-06-09	0	0	0
2019-06-10	0	0	0
2019-06-11	0	0	0
2019-06-12	0	0	0
2019-06-13	0	0	0
2019-06-14	0	0	0
2019-06-15	0	0	0
2019-06-16	0	0	0
2019-06-17	21	47	28
2019-06-18	21	46	29
2019-06-19	14	49	31
2019-06-20	24	57	29
2019-06-21	15	52	32
2019-06-22	16	47	29
2019-06-23	16	47	29
2019-06-24	16	51	29
2019-06-25	26	48	31
2019-06-26	0	0	0
2019-06-27	0	0	0
2019-06-28	11	56	28
2019-06-29	12	55	32
2019-06-30	11	57	34
2019-07-01	13	53	32
\.


--
-- Name: values values_pkey; Type: CONSTRAINT; Schema: public; Owner: jannusch
--

ALTER TABLE ONLY public."values"
    ADD CONSTRAINT values_pkey PRIMARY KEY (date);


--
-- Name: TABLE "values"; Type: ACL; Schema: public; Owner: jannusch
--

GRANT ALL ON TABLE public."values" TO magieuser;


--
-- PostgreSQL database dump complete
--

