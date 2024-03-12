import scrapy

class MITREAttackSpider(scrapy.Spider):
    name = 'mitreattack'
    start_urls = ['https://attack.mitre.org/groups/']

    def parse(self, response):
        # Extracting data from the table with class name 'table'
        table_rows = response.css('table.table tr')

        for row in table_rows:
            # Extracting data from each column in the row
            column1_data = row.css('td:nth-child(1) a::text').get()
            column1_url = row.css('td:nth-child(1) a::attr(href)').get()
            column2_data = row.css('td:nth-child(2) a::text').get()
            column3_data = row.css('td:nth-child(3)::text').get()
            column4_data = row.css('td:nth-child(4) p::text').get()

            # Extracting URL from the first column using a different selector
            column1_url = row.css('td:nth-child(1) a::attr(href)').extract_first()

            # Creating an absolute URL
            column1_url_absolute = response.urljoin(column1_url.strip()) if column1_url else None

            yield {
                'Column1': column1_data.strip() if column1_data else None,
                'Column1_URL': column1_url_absolute,
                'Column2': column2_data.strip() if column2_data else None,
                'Column3': column3_data.strip() if column3_data else None,
                'Column4': column4_data.strip() if column4_data else None,
            }
