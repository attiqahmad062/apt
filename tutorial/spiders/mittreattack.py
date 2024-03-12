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
                'MittreName': column1_data.strip() if column1_data else None,
                'Url': column1_url_absolute,
                'GroupName': column2_data.strip() if column2_data else None,
                'AssociatedGroups': column3_data.strip() if column3_data else None,
                'Summary': column4_data.strip() if column4_data else None,
            }
    #         yield response.follow(column1_url_absolute, callback=self.parse_group)
    # def parse_group(self, response):
    #     # Extracting data from the group page
    #     print("hello i m ",response)
    #     # group_name = response.css('h1::text').get()
    #     # description = response.css('div.container p::text').get()

    #     # yield {
    #     #     'Group Name': group_name.strip() if group_name else None,
    #     #     'Description': description.strip() if description else None,
    #     #     'URL': response.url
    #     # }