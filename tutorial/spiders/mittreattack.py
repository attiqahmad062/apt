import scrapy
import re


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

            # yield {
            #     'MittreName': column1_data.strip() if column1_data else None,
            #     'Url': column1_url_absolute,
            #     'GroupName': column2_data.strip() if column2_data else None,
            #     'AssociatedGroups': column3_data.strip() if column3_data else None,
            #     'Summary': column4_data.strip() if column4_data else None,
            # }
            # Follow the URL to the group's page and parse the table data
            if column1_url_absolute:
                yield response.follow(column1_url_absolute, self.parse_group_page)

    def parse_group_page(self, response):
        # Updated CSS selectors to match the new structure and maintain sequence
        table_rows = response.css('table.techniques-used tr')

        for row in table_rows:
            # Extracting data from each column in the row, ensuring correct sequence
            domain_data = row.css('td:nth-child(1)::text').get()
            id_data = row.css('td:nth-child(2) a::text').get()
            sub_id_data = row.css('td:nth-child(3) a::text').get() if len(row.css('td')) >= 5 else None
            name_data = ' '.join(row.css('td:nth-child(4) *::text').getall()).strip()
            use_data = ' '.join(row.css('td:nth-child(5) *::text').getall()).strip()

            # yield {
            #     'Domain': domain_data.strip() if domain_data else None,
            #     'ID': id_data.strip() if id_data else None,
            #     'SubID': sub_id_data.strip() if sub_id_data else None,
            #     'Name': name_data if name_data else None,
            #     'Use': use_data if use_data else None,
            # }

        # New section to scrape the table with class name 'table-alternate'
        
        alternate_table_rows = response.css('table.table-alternate tr')

        for row in alternate_table_rows:
            # Extracting data from each column in the row
            id_data = ' '.join(row.css('td:nth-child(1) *::text').getall()).strip()
            name_data = ' '.join(row.css('td:nth-child(2) *::text').getall()).strip()
            references_data = ' '.join(row.css('td:nth-child(3) *::text').getall()).strip()
            # Extracting techniques
            techniques_data = []
            techniques_nodes = row.css('td:nth-child(4) *::text').getall()
            for node in techniques_nodes:
                techniques_data.append(node.strip())



            # Check if ID starts with 'S'
            if id_data and id_data.startswith('S') and id_data[1:].isdigit():
                yield {
                    'ID': id_data if id_data else None,
                    'Name': name_data if name_data else None,
                    'References': references_data if references_data else None,
                    'Techniques': ' '.join(techniques_data) if techniques_data else None,
                }


                
