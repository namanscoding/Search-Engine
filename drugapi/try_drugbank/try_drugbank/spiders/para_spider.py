import scrapy


class ParaSpider(scrapy.Spider):
    name = "para"

    def __init__(self, *args, **kwargs):
        super(ParaSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get('start_urls').split(',')

    def parse(self, response):
        yld = dict()
        yld['generic_name']     = response.xpath(            "string(//dt[@id='generic-name']/following-sibling::dd)")      .get()
        yld['synonyms']         = response.xpath(            "(//dt[@id='synonyms']/following-sibling::dd//ul//li/text())") .getall()
        yld['brand_names']      = response.xpath(            "string(//dt[@id='brand-names']/following-sibling::dd)")       .get().split(", ")
        yld['indication']       = response.xpath(            "string(//dt[@id='indication']/following-sibling::dd)")        .get()
        yld['chemical_formula'] = response.xpath(            "string(//dt[@id='chemical-formula']/following-sibling::dd)")  .get()
        return yld



    # def start_requests(self):
    #     urls = [
    #     "https://go.drugbank.com/drugs/DB00316",  # paracetamol
    #     "https://go.drugbank.com/drugs/DB01060",  # amoxxillin
    #     "https://go.drugbank.com/drugs/DB01050",  # ibuprofen
    #     "https://go.drugbank.com/drugs/DB00341",  # Cetirizine
    #     "https://go.drugbank.com/drugs/DB00207",  # Azithromycin
    #     "https://go.drugbank.com/drugs/DB00381",  # Amlodipine
    #     "https://go.drugbank.com/drugs/DB01001",  # Salbutamol
    #     "https://go.drugbank.com/drugs/DB00924",  # Cyclobenzaprine
    #     "https://go.drugbank.com/drugs/DB00567",  # Cephalexin
    #     "https://go.drugbank.com/drugs/DB00999",  # Hydrochlorothiazide
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)


# generic name
# brand name
# indications
# chem formula