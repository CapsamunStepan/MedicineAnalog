from bs4 import BeautifulSoup
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36"
}


def get_info(url):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        dom = etree.HTML(str(soup))
        item1 = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]')
        item1_desc = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[1]/div['
                               '2]/a/div')
        item2 = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]')
        item2_desc = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[2]/div['
                               '2]/a/div')
        item3 = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]')
        item3_desc = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[3]/div['
                               '2]/a/div')
        item4 = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[4]/div[1]/div[1]')
        item4_desc = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[4]/div[2]')

        item5 = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[5]/div[1]/div[1]')
        item5_desc = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[5]/div[2]')

        item6 = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[6]/div[1]/div[1]')
        item6_desc = dom.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[4]/div[2]/div[1]/div[2]/div[6]/div[2]')
        description = [
            {
                'name': item1[0].text.strip(),
                'desc': item1_desc[0].text.strip(),
            },
            {
                'name': item2[0].text.strip(),
                'desc': item2_desc[0].text.strip(),
            },
            {
                'name': item3[0].text.strip(),
                'desc': item3_desc[0].text.strip(),
            },
            {
                'name': item4[0].text.strip(),
                'desc': item4_desc[0].text.strip(),
            },
            {
                'name': item5[0].text.strip(),
                'desc': item5_desc[0].text.strip(),
            },
            {
                'name': item6[0].text.strip(),
                'desc': item6_desc[0].text.strip(),
            },
        ]

        return description

    else:
        return None


if __name__ == "__main__":
    url_ = "https://www.apteka.md/ru/product/acc-100-porosok-dprig-rra-dpriema-vnutr-100-mg-n2x10-1892"

    dictionary = get_info(url_)
