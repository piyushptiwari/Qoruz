import re
import lxml
import json

from bs4 import BeautifulSoup
from requests import get

tag_list=[]
gen_list=[]
dir_list=[]
url= "https://www.imdb.com/title/tt6710474/"
page = get(url)
soup = BeautifulSoup(page.content, 'lxml')
content = soup.find(id="main")

articleTitle = soup.find("h1", class_="sc-b73cd867-0 fbOhB").text.replace("\n","")
#print(articleTitle)
yr= soup.find("a", class_="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh").text.replace("\n","")
#print(yr)

duration=soup.find("li", class_="ipc-inline-list__item").text.replace("/n","")

for tag in soup.find_all("li", class_="ipc-inline-list__item"):
    tag_list.append(tag.text)
#print(tag_list[2])


Rating= soup.find("span", class_="sc-7ab21ed2-1 jGRxWM").text.replace("\n","")
given_by=soup.find("div", class_="sc-7ab21ed2-3 dPVcnq").text.replace("\n","")
com=Rating+"/10, " + given_by

#gen=soup.find_all("div", class_="ipc-chip-list sc-16ede01-4 bMBIRz")
for gen in soup.find_all("div", class_="ipc-chip-list sc-16ede01-4 bMBIRz"):
    gen_list.append(gen.text)
#print(gen_list)


des=soup.find_all("span", class_="sc-16ede01-0 fMPjMP")
#print(des)


for dire in soup.find_all("li", class_="ipc-metadata-list__item"):
    dir_list.append(dire.text)
#print(dir_list[0])
#print(dir_list[1])
#print(dir_list[2])


json_data = ({"articleTitle":articleTitle},{"Year":yr},{"Duration":tag_list[2]}, {"IMDB Rating": com},{"Genre":gen_list},{"Description":des},{"Directors":dir_list[0].replace("Directors",'')},{"Writers":dir_list[1].replace("Writers",'')},{"Stars":dir_list[2].replace("Stars",'')})


print(json_data)



