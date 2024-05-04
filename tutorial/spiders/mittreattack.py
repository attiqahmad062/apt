import scrapy
import re
from tutorial.pipelines import GroupTable, TechniquesTable,SoftwareTable,CompainsTable,SubTechniques,ProcedureExamples,Mitigations,Detections
class MITREAttackSpider(scrapy.Spider):
    name = 'mitreattack'
    start_urls = ['https://attack.mitre.org/groups/']
    def parse(self, response):# crawl the main page of groups
        # Extracting data from the table with class name 'table'
        groupTable = response.css('table.table tr')
        for row in groupTable:
            column1_data = row.css('td:nth-child(1) a::text').get()
            column1_url = row.css('td:nth-child(1) a::attr(href)').get()
            column2_data = row.css('td:nth-child(2) a::text').get()
            column3_data = row.css('td:nth-child(3)::text').get()
            column4_data = row.css('td:nth-child(4) p::text').get()
            # Extracting URL from the first column using a different selector
            column1_url = row.css('td:nth-child(1) a::attr(href)').extract_first()
            # Creating an absolute URL
            column1_url_absolute = response.urljoin(column1_url.strip()) if column1_url else None
            yield GroupTable ({
                'MittreName': column1_data.strip() if column1_data else None,
                'Url': column1_url_absolute,
                'GroupName': column2_data.strip() if column2_data else None,
                'AssociatedGroups': column3_data.strip() if column3_data else None,
                'Summary': column4_data.strip() if column4_data else None,
            })
#             # Follow the URL to the group's page and parse the table data
#             if column1_url_absolute:
#               yield response.follow(column1_url_absolute, self.parse_group_page,column1_data)
# #     def parse_group_page(self, response):
#         id_= response.xpath('//span[contains(text(), "ID:")]/following-sibling::text()').get().strip()
#             # Extracting First Seen
#         first_seen = response.xpath('//span[contains(text(), "First Seen:")]/following-sibling::text()').get()
#         first_seen_text = response.xpath('//span[contains(text(), "First Seen:")]/following-sibling::text()').get()
#         first_seen = first_seen_text.strip() if first_seen_text else ''
        
#         # Extracting Last Seen
#         last_seen_text = response.xpath('//span[contains(text(), "Last Seen:")]/following-sibling::text()').get()
#         last_seen = last_seen_text.strip() if last_seen_text else ''
#         contributors_text = response.xpath('//span[contains(text(), "Contributors:")]/following-sibling::text()').get()
#         contributors = contributors_text.strip() if contributors_text else ''
#         # Extracting Version
#         version_text = response.xpath('//span[contains(text(), "Version")]/following-sibling::text()').get()
#         version = version_text.strip() if version_text else ''
        
#         # Extracting Created
#         created_text = response.xpath('//span[contains(text(), "Created:")]/following-sibling::text()').get()
#         created = created_text.strip() if created_text else ''
        
#         # Extracting Last Modified
#         last_modified_text = response.xpath('//span[contains(text(), "Last Modified:")]/following-sibling::text()').get()
#         last_modified = last_modified_text.strip() if last_modified_text else ''
#         # yield {
#         #     'ID': id_,
#         #     "Contributors":contributors,
#         #     # 'First_Seen': first_seen,
#         #      'Version': version,
#         #      'Created': created,
#         #     'Last Modified': last_modified
#         # }




#         techniqueTable = response.css('table.techniques-used tr')
#         for row in techniqueTable:
#             domain_data = row.css('td:nth-child(1)::text').get()
#             id_data = row.css('td:nth-child(2) a::text').get()
#             technique_url = row.css('td:nth-child(2) a::attr(href)').get()
#             references = []

#             if len(row.css('td')) >= 5:
#                 sub_id_data = row.css('td:nth-child(3) a::text').get()
#                 name_data = ' '.join(row.css('td:nth-child(4) *::text').getall()).strip()
#                 use_data = ' '.join(row.css('td:nth-child(5) *::text').getall()).strip()
#                 references_tag = 'td:nth-child(5) a'
#             else:
#                 sub_id_data = None
#                 name_data = ' '.join(row.css('td:nth-child(3) *::text').getall()).strip()
#                 use_data = ' '.join(row.css('td:nth-child(4) *::text').getall()).strip()
#                 references_tag = 'td:nth-child(4) a'

#             # Extract references only from the current row
#             for link in row.css(references_tag):
#                 href = link.css('::attr(href)').get()
#                 text = link.css('::text').get()

#                 if text and text.strip().startswith('[') and text.strip().endswith(']'):
#                     if href not in references:
#                         references.append(href)

#         #     technique_url = response.urljoin(technique_url.strip()) if technique_url else None
#         #     references_string = ' '.join(references)
#         #     # yield TechniquesTable( {
#             #     'Domain': domain_data.strip() if domain_data else None,
#             #     'ID': id_data.strip() if id_data else None,
#             #     'SubId': sub_id_data.strip() if sub_id_data else None,
#             #     'Use': use_data if use_data else None,
#             #     "References": references_string
#             # })
#             # # if technique_url:
#             #     yield response.follow(technique_url, self.parse_techniques)
            
# #         # Software Table:
# #         softwareTable = response.css('table.table-alternate tr')
# #         for index, row in enumerate(softwareTable, start=1):
# #             # Extracting data from each column in the row
# #             id_data = ' '.join(row.css('td:nth-child(1) *::text').getall()).strip()
# #             name_data = ' '.join(row.css('td:nth-child(2) *::text').getall()).strip()
# #             # references_data = ' '.join(row.css('td:nth-child(3) *::text').getall()).strip()
# #             references_data = row.css('td:nth-child(3) span sup a::attr(href)').get()
# #             # Extracting techniques
# #             techniques_data = []
# #             techniques_nodes = row.css('td:nth-child(4) *::text').getall()
# #             for node in techniques_nodes:
# #                 techniques_data.append(node.strip())
# #             # Check if ID starts with 'S'
# #             if id_data and id_data.startswith('S') and id_data[1:].isdigit():
# #                 yield SoftwareTable( {
# #                     'ID': id_data if id_data else None,
# #                     'Name': name_data if name_data else None,
# #                     'References': references_data if references_data else None,
# #                     'Techniques': ' '.join(techniques_data) if techniques_data else None,
# #                 } )
# #         # campaigns 
# #         if response.css('h2#campaigns'):
# #             for row in response.xpath('//*[@id="v-attckmatrix"]/div[2]/div/div/div/div[3]'):
# #                 yield  CompainsTable({
# #                     'ID': row.css('td:nth-child(1) a::text').get(),
# #                     'Name': row.css('td:nth-child(2) a::text').get(),
# #                     'FirstSeen': row.css('td:nth-child(3) *::text').get(),
# #                     'LastSeen': row.css('td:nth-child(4) *::text').get(),
# #                     'References': row.css('td:nth-child(5)  p sup a::attr(href)').get(),
# #                      'Techniques': row.css('td:nth-child(6) a::attr(href)').getall(),
# #                 })
# #         #associated groups (aliasDescription)
# #         if response.css('h2#aliasDescription'):
# #             for row in response.xpath('//*[@id="v-attckmatrix"]/div[2]/div/div/div/div[2]/table/tbody/tr'):
# #                 name = row.xpath('./td[1]/text()').get()
# #                 cleaned_name = re.sub(r'\W+', '', name) if name else name
# #                 description = row.xpath('/html/body/div[1]/div[3]/div[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr[1]/td[2]/p/span/sup/a/@href').get()
# #                 yield {
# #                     'Name': cleaned_name,
# #                     'Description': description
# #                 }
# # #      def parse_techniques(self, response):
# # #         #  subtechniques
# # #         for row in response.xpath('//div[@id="subtechniques-card-body"]//table//tbody/tr'):
# # #             # yield SubTechniques( {
# # #             #     'ID': row.xpath('td[1]/a/text()').get(),
# # #             #     'Name': row.xpath('td[2]/a/text()').get(),
# # #             # })
            
# # #         # procedure examples
# # #         if response.css('h2#examples'):
# # #                 rows = response.xpath('/html/body/div[1]/div[3]/div[2]/div/div[2]/div/div/div/div[2]/table')
# # #                 for row in rows:
# # #                         # Extract the data from each cell in the row
# # #                         id = row.css('td:nth-child(1) a::text').get()
# # #                         name = row.css('td:nth-child(2) a::text').get()
# # #                         description = row.css('td:nth-child(3) p::text').get()
                        
                    
# # #                         yield ProcedureExamples( {
# # #                             'ID': id,
# # #                             'Name': name,
# # #                             'Description': description
# # #                     })
# # #         #mitigations
# # #         # if response.css('h2#mitigations'):
# # #         #     rows = response.xpath('//*[@id="v-attckmatrix"]/div[2]/div/div/div/div[3]/table')
# # #         #     for row in rows: 
# # #         #         id = row.css('td:nth-child(1) a::text').get()
# # #         #         mitigation = row.css('td:nth-child(2) a::text').get()
# # #         #         description = row.css('td:nth-child(3) p::text').get()
# # #         #         mitigation_url = row.css('td:nth-child(2) a::attr(href)').get()
# # #         #         technique_url=response.urljoin(technique_url.strip()) if technique_url else None
# # #         #         if id.__contains__('M'):
               
# # #         #            yield Mitigations({
# # #         #             'ID': id,
# # #         #             'Mitigation': mitigation,
# # #         #             'Description': description
# # #         #         })
# # #         #detections
# # #         # if response.css('h2#detection'):
# # #         #      rows = response.css('table.table.datasources-table.table-bordered tbody tr')
# # #         #      for row in rows:
# # #         #         # Extract the data from each cell in the row
# # #         #         id = row.css('td:nth-child(1) a::text').get()
# # #         #         data_source = row.css('td:nth-child(2) a::text').get()
# # #         #         data_component = row.css('td:nth-child(3) a::text').get()
# # #         #         detects = row.css('td:nth-child(4) p::text').get()
# # #         #         # Yield the extracted   data
# # #         #         yield   {
# # #         #             'ID': id,
# # #         #             'DataSource': data_source,
# # #         #             'DataComponent': data_component,
# # #         #             'Detects': detects
# # #         #         }
# # # #
# # # # 
        
