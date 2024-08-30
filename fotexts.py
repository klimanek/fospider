import os
import scrapy

class FOSpiderTexts(scrapy.Spider):
    name = "fotexts"
    start_urls = [
        "http://fyzikalniolympiada.cz/studijni-texty",
    ]

    def parse(self, response):
        for row in response.css('table.texty-arch tr'):
            # Získání textu před a uvnitř <strong>
            before_strong = row.css('td::text').get()
            inside_strong = row.css('td strong::text').get()
            
            # Spojení textu před a uvnitř <strong>
            full_title = f"{before_strong.strip() if before_strong else ''} {inside_strong.strip() if inside_strong else ''}".strip()
            pdf_link = row.css('a i.pdf::text').get()

            if pdf_link:
                # Hledáme odkazy na PDF
                pdf_url = row.css('a[href$=".pdf"]::attr(href)').get()
                
                if pdf_url:
                    yield { # Získáváme data
                        'title': full_title,
                        'pdf_url': response.urljoin(pdf_url)
                    }

                    yield scrapy.Request( # Stahujeme PDF
                        url=response.urljoin(pdf_url),
                        callback=self.save_pdf,
                        meta={'title': full_title if full_title else 'No title'}
                    )


    def save_pdf(self, response):
        """Stahuje PDF soubor"""
        title = response.meta['title']
        filename = f"{title}.pdf"
        download_dir = "Texty/"

        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        with open(download_dir + filename, 'wb') as f:
            f.write(response.body)

        self.log(f"Saved file {filename}")
