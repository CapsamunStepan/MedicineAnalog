# getting info from websites
# scrapy directory

cd .\meds_scraper\
scrapy crawl apteka_md -O apteka_md.json
scrapy crawl farmacie_md -O farmacie_md.json
scrapy crawl farmacia_familiei -O farmacia_familiei.json
scrapy crawl hippocrates -O hippocrates.json




# loading medicines to database
# root directory

python manage.py load2db --path meds_scraper\apteka_md.json --pharmacy AptekaMD --manufacturer True
python manage.py load2db --path meds_scraper\farmacie_md.json --pharmacy FarmacieMD
python manage.py load2db --path meds_scraper\farmacia_familiei.json --pharmacy FarmaciaFamiliei --manufacturer True
python manage.py load2db --path meds_scraper\hippocrates.json --pharmacy Hippocrates --manufacturer True




# launching website
# root directory

python manage.py runserver