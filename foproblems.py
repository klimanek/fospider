import os
import scrapy

class FOSpiderProblems(scrapy.Spider):
    name = "foproblems"
    start_urls = [
        "http://fyzikalniolympiada.cz/archiv/zadani-a-reseni",
    ]

    def parse(self, response):
        links = response.css('a[href$=".pdf"]::attr(href)').getall()
        problems_and_solutions = [link for link in links if 'archiv' in link] # Chceme jen archiv, ne současné dokumenty

        for link in problems_and_solutions:
            file_name = os.path.basename(link)
            
            yield scrapy.Request( # Stahujeme PDF
                url=response.urljoin(link),
                callback=self.save_pdf,
                meta={'title': file_name}
            )


    def save_pdf(self, response):
        """Stahuje PDF soubor"""
        title = response.meta['title']
        filename = f"{title}.pdf"
        download_dir = "Ulohy/"

        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        with open(download_dir + filename, 'wb') as f:
            f.write(response.body)

        self.log(f"Saved file {filename}")

