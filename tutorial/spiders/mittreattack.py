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
            column2_data = row.css('td:nth-child(2) a::text').get()
            column3_data = row.css('td:nth-child(3)::text').get()
            column4_data = row.css('td:nth-child(4) p::text').get()
        for link in column1_data:
            mainLink="https://attack.mitre.org/groups/"
            mainLink.append(link)
            print(mainLink)
            yield response.follow("https://attack.mitre.org/groups/"+link, callback=self.parse_group)
            # yield {

            #     'Column1': column1_data.strip() if column1_data else None,
            #     'Column2': column2_data.strip() if column2_data else None,
            #     'Column3': column3_data.strip() if column3_data else None,
            #     'Column4': column4_data.strip() if column4_data else None,
            # }
    def parse_group(self, response):
        # Extracting data from the group page
        print("hello i m ",response)
        # group_name = response.css('h1::text').get()
        # description = response.css('div.container p::text').get()

        # yield {
        #     'Group Name': group_name.strip() if group_name else None,
        #     'Description': description.strip() if description else None,
        #     'URL': response.url
        # }