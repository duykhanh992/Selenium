from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import pandas as pd
from time import sleep
from openpyxl import Workbook

browser = webdriver.Firefox(executable_path="./geckodriver")

# browser.get("https://www.benchmarkintl.com/")
url = "https://www.benchmarkintl.com/about/global-team/dealmakers/"
browser.get(url)
content = browser.page_source
soup = BeautifulSoup(content)
employees_name = []  # List to employee name
locations = []  # List to location of employee
titles = []  # List to title of employee

for container in soup.findAll("div", attrs={"class": "btmsq-o"}):

    name = container.div.span
    location = container.a
    title = container.div.span.findNext("span")
    employees_name.append(name.text)
    locations.append(location.text)
    titles.append(title.text.replace('"', ""))


# print(dict(zip(employees_name, title)))


df = pd.DataFrame(
    {"Employee Name": employees_name, "Title": titles, "Location": locations}
)


df.to_excel("Deal Makers.xlsx", encoding="utf-8", index=True, index_label="No.")


# container = soup.findAll("div", attrs={"class": "btmsq-o"})
# print(len(container))
# print(elem)
# filename ="employee.csv"
# f = open(filename, "w")

sleep(20)  # Close window after 20 second

browser.close()
