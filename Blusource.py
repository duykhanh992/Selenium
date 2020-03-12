from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import pandas as pd
from time import sleep
from openpyxl import Workbook

import re  # import regression expression package

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


url = "https://www.blusource.com/"
with webdriver.Firefox(executable_path="./geckodriver") as browser:
    browser.get(url)
    browser.find_element_by_xpath(
        "/html/body/div/div[3]/main/div/div[3]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/a/img"
    ).click()
    browser.find_element_by_xpath(
        "/html/body/main/div[2]/section/div/div/div[1]/a/div[2]/span"
    ).click()
    browser.find_element_by_xpath(
        "/html/body/main/div/section/div/div[2]/div/a[1]/p"
    ).click()
    content = browser.page_source
    soup = BeautifulSoup(content, features="html.parser")
    catgories = []  # Category of product
    product_names = []  # Name of the product
    product_types = []
    product_prices = []  # Price of the product
    product_color = []
    details = []
    set_Quantity = []

    for container in soup.findAll("div", attrs={"class": "product-item__info-inner"}):
        detail = container.a
        item_Quantity = int(detail.text[0:2])  # Number of item
        p = re.findall("\$[0-9.]+", detail.text)
        price = "".join(p)

        name = container.a.findNext("a").text
        product_names.append(name)
        product_prices.append(price)
        catgories.append("Bag")
        set_Quantity.append(item_Quantity)

    divTag = soup.findAll("div", attrs={"class": "product-item__info-inner"})
    for tag in divTag:
        firstTag = tag.findAll("div", attrs={"class": "color-swatch-list"})
        for secondTag in firstTag:
            print(secondTag.div.label["title"])
    # element_to_hover_over = browser.find_element_by_name("Shop")

    # hover = ActionChains(browser).move_to_element(element_to_hover_over)
    # hover.perform()
    # print(element_to_hover_over)
# print(dict(zip(product_names, product_prices)))
product_names[18] = 'Wholesale 18" Clear Backpacks'
df = pd.DataFrame(
    {
        "Product Name": product_names,
        "Categories": catgories,
        "Price": product_prices,
        "Quantity/Set": set_Quantity,
    }
)


df.to_excel(
    "BluSource.xlsx", encoding="utf-8", index=True, index_label="No.", sheet_name="Bag"
)


sleep(60)

