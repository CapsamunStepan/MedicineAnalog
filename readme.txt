cd .\meds_scraper\
scrapy crawl apteka_md -O apteka_md.json
scrapy crawl farmacie_md -O farmacie_md.json

root directory
python manage.py load2db --path meds_scraper\apteka_md.json --pharmacy AptekaMD --manufacturer True
python manage.py load2db --path meds_scraper\farmacie_md.json --pharmacy FarmacieMD
