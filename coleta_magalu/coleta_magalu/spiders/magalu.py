import scrapy


class MagaluSpider(scrapy.Spider):
    name = "magalu"
    allowed_domains = ["www.magazineluiza.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/cafeteira-tres-coracoes/eletroportateis/s/ep/ctcr/"]

    def parse(self, response):

        products = response.css('div.sc-dcjTxL.xDJfk')

        for product in products:

            price_of = product.css('p.sc-kpDqfm.efxPhd.sc-gEkIjz.jmNQlo::text').get()
            # price_of_cleaned = price_of.replace('R$\xa0', '')
            # price_of_cleaned_float = float(price_of_cleaned) if price_of_cleaned else None

            price_per = product.css('p.sc-kpDqfm.eCPtRw.sc-bOhtcR.dOwMgM::text').get()
            # price_per_cleaned = price_per.replace('R$\xa0', '')
            # price_per_cleaned_float = float(price_per_cleaned) if price_per_cleaned else None


            yield{
                'title': product.css('h2.sc-fvwjDU.fbccdO::text').get(),
                'price_of': price_of,
                'price_per': price_per
            }