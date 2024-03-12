<<<<<<< HEAD
# import scrapy

# class MITREAttackSpider(scrapy.Spider):
#     name = 'mitreattack'
#     start_urls = ['https://attack.mitre.org/groups/']

#     def parse(self, response):
#         # Extracting data from the table with class name 'table'
#         table_rows = response.css('table.table tr')

#         for row in table_rows:
#             # Extracting data from each column in the row
#             column1_data = row.css('td:nth-child(1) a::text').get()
#             column1_url = row.css('td:nth-child(1) a::attr(href)').get()
#             column2_data = row.css('td:nth-child(2) a::text').get()
#             column3_data = row.css('td:nth-child(3)::text').get()
#             column4_data = row.css('td:nth-child(4) p::text').get()

#             # Extracting URL from the first column using a different selector
#             column1_url = row.css('td:nth-child(1) a::attr(href)').extract_first()

#             # Creating an absolute URL
#             # Creating an absolute URL by joining the base URL with the relative URL
#             column1_url_absolute = response.urljoin(column1_url.strip()) if column1_url else None

#             yield {
#                 'Column1': column1_data.strip() if column1_data else None,
#                 'Column1_URL': column1_url_absolute,
#                 'Column2': column2_data.strip() if column2_data else None,
#                 'Column3': column3_data.strip() if column3_data else None,
#                 'Column4': column4_data.strip() if column4_data else None,
#             }

#             # Follow the link in the first column to crawl the next table
#             if column1_url_absolute:
#                 yield scrapy.Request(url=column1_url_absolute, callback=self.parse_second_table, meta={'Column1': column1_data.strip()})

#     def parse_second_table(self, response):
#         # Extracting data from the second table with headers: Domain, ID, Name, Use
#         second_table_rows = response.css('table.second-table tr')
#         for second_row in second_table_rows:
#             # Extracting data from each column in the second row
#             domain_data = second_row.css('td:nth-child(1)::text').get()
#             id_data = second_row.css('td:nth-child(2) a::text').get()
#             name_data = second_row.css('td:nth-child(3) a::text').get()
#             use_data = second_row.css('td:nth-child(4)::text').get()
#             print("--------------------------------------",use_data)
#             yield {
#                 'Column1': response.meta['Column1'],
#                 'Column1_URL': response.url,
#                 'Column2': None,  # No data from the second table in these columns
#                 'Column3': None,
#                 'Column4': None,
#                 'Domain': domain_data.strip() if domain_data else None,
#                 'ID': id_data.strip() if id_data else None,
#                 'Name': name_data.strip() if name_data else None,
#                 'Use': use_data.strip() if use_data else None,
#             }
=======
import scrapy

class MITREAttackSpider(scrapy.Spider):
    name = 'mittreattack'
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
            # Creating an absolute URL by joining the base URL with the relative URL
            column1_url_absolute = response.urljoin(column1_url.strip()) if column1_url else None

            yield {
                'Column1': column1_data.strip() if column1_data else None,
                'Column1_URL': column1_url_absolute,
                'Column2': column2_data.strip() if column2_data else None,
                'Column3': column3_data.strip() if column3_data else None,
                'Column4': column4_data.strip() if column4_data else None,
            }

    #         # Follow the link in the first column to crawl the next table
    #         if column1_url_absolute:
    #             yield scrapy.Request(url=column1_url_absolute, callback=self.parse_second_table, meta={'Column1': column1_data.strip()})

    # def parse_second_table(self, response):
    #     # Extracting data from the second table with headers: Domain, ID, Name, Use
    #     second_table_rows = response.css('table.second-table tr')
    #     for second_row in second_table_rows:
    #         # Extracting data from each column in the second row
    #         domain_data = second_row.css('td:nth-child(1)::text').get()
    #         id_data = second_row.css('td:nth-child(2) a::text').get()
    #         name_data = second_row.css('td:nth-child(3) a::text').get()
    #         use_data = second_row.css('td:nth-child(4)::text').get()

    #         yield {
    #             'Column1': response.meta['Column1'],
    #             'Column1_URL': response.url,
    #             'Column2': None,  # No data from the second table in these columns
    #             'Column3': None,
    #             'Column4': None,
    #             'Domain': domain_data.strip() if domain_data else None,
    #             'ID': id_data.strip() if id_data else None,
    #             'Name': name_data.strip() if name_data else None,
    #             'Use': use_data.strip() if use_data else None,
    #         }
>>>>>>> 6fd347b6e826deef1dbe60f4d092c9504082fea5
