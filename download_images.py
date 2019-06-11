import os
import sys
import requests
from bs4 import BeautifulSoup as soup

urllist = ['https://www.ikea.in/beds', 'https://www.ikea.in/chairs-stools-benches',
           'https://www.ikea.in/tables', 'https://www.ikea.in/lighting']

name = ''

count = 1


def get_source(link):
    print(link)
    try:
        r = requests.get(link)
        if r.status_code == 200:
            return soup(r.text, features="html.parser")
        else:
            return None
    except:
        return None


def download_image(name, source):
    try:
        global count
        r = requests.get(source)
        filename = r'images\{0}_{1}.jpg'.format(name, count)
        with open(filename, 'wb') as f:
            f.write(r.content)
        count += 1
    except:
        pass


def get_source_data(link2):
    global name
    html_source2 = get_source(link2)
    if html_source2:
        # print(html_source2)
        class_attr3 = html_source2.findAll('a', attrs={"class": 'single_pro_link'})
        if class_attr3:
            for cls3 in class_attr3:
                link4 = cls3.get('href')
                get_source_data(link4)
        class_attr2 = html_source2.findAll('div', attrs={"class": "image-claim-height"})
        next_page = html_source2.find('a', attrs={"class": "pagination__right button button--primary"})
        for cls2 in class_attr2:
            #print(cls2)
            img_data = cls2.findAll('img')
            for data in img_data:
                name2 = data.get('alt')
                source = data.get('src')
                print(name2, source)
                download_image(name, source)
        if next_page:
            urllink2 = next_page.get('href')
            get_source_data(urllink2)


for list1 in urllist:
    if "chair" in list1:
        name = 'chair'
    elif "table" in list1:
        name = 'table'
    elif "bed" in list1:
        name = "bed"
    elif "light" in list1:
        name = "lighting"
    else:
        raise ValueError("Unknown data")
    html_source = get_source(list1)
    if html_source:
        #print(html_source)
        class_attr = html_source.findAll('a', attrs={"class": 'single_pro_link'})
        print(class_attr)
        for cls in class_attr:
            link = cls.get('href')
            get_source_data(link)





