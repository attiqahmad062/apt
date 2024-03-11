import scrapy

class MITREAttackSpider(scrapy.Spider):
    name = 'mitreattack'
    start_urls = ['https://attack.mitre.org/groups/']

    def parse(self, response):
        # Extracting data from the table with class name 'table'
        table_rows = response.css('table.table tr')

        for row in table_rows:
            # Extracting data from each row
            column1 = row.css('td:nth-child(1)::text').get()
            column2 = row.css('td:nth-child(2)::text').get()
            column3 = row.css('td:nth-child(3)::text').get()
            column4 = row.css('td:nth-child(4)::text').get()

            yield {
                'Column1': column1,
                'Column2': column2,
                'Column3': column3,
                'Column4': column4,
            }
