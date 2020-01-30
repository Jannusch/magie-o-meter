import scrapy
import sqlite3

class QuotesSpider(scrapy.Spider):
    name = "magieValue"
    start_urls = [
        'https://tagesenergie.org/energie-des-tages/tagesenergie-am-30-01-2020/',
    ]


# CSS       html.wf-loading.Firefox.Firefox72.cssanimations.csstransitions.no-touchevents.js_active.vc_desktop.vc_transform body.post-template-default.single.single-post.postid-2936.single-format-standard.wpb-js-composer.js-comp-ver-5.5.2.vc_responsive div#mk-boxed-layout div#mk-theme-container div#theme-page.master-holder.blog-post-type-image.blog-style-compact.clearfix div.mk-main-wrapper-holder div#mk-page-id-2936.theme-page-wrapper.mk-main-wrapper.mk-grid.full-layout.false div.theme-content.false article#2936.mk-blog-single.post-2936.post.type-post.status-publish.format-standard.has-post-thumbnail.hentry.category-energie-des-tages.category-sonnenkraft.tag-energie-des-tages.tag-sonnenkraft div.mk-single-content.clearfix div.wpb_row.vc_row.vc_row-fluid.mk-fullwidth-false.attched-false.js-master-row.mk-grid.mk-in-viewport div.vc_col-sm-12.wpb_column.column_container._.height-full div.wpb_row.vc_inner.vc_row.vc_row-fluid.attched-false div.wpb_column.vc_column_container.vc_col-sm-4 div.vc_column-inner div.wpb_wrapper div#mk-chart-9.mk-chart.js-el div.mk-chart__chart.easyPieChart span.mk-chart__percent
            # XPath     /html/body/div[2]/div/div[1]/div[2]/div/div[1]/article/div[3]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/span
            # Scrapy    response.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/article/div[3]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/span/text()').get()
    def parse(self, response):
        magie_o_meter_value = response.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/article/div[3]/div[2]/div/div[2]/div[3]/div/div/div/div[1]/span/text()').get()
        print(f'Magie-o-meter Wert: {magie_o_meter_value}')   

def safe_in_db(value, date):
    conn = sqlite3.connect('././magie.db')
    c = conn.cursor()
    c.execute('''INSERT INTO magie_values VALUES ('30.01.2020', '12', '49', '29')''')
    conn.commit()
    conn.close()
