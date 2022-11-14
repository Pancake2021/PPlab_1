import os
from time import sleep
from bs4 import BeautifulSoup
import requests
##import cv2
##import numpy as np
import os.path
##import lxml

header = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 '
                  'Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
}

def creating_folder(folder_name):
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    if not os.path.exists(os.path.join('dataset',folder_name)):
        os.mkdir(os.path.join('dataset',folder_name))

def creating_url(request_name):
    for page_number in range(1,36):
        print(page_number, "page")
        request_name.replace('','%20')
        link = f'https://yandex.ru/images/search?text={request_name}&p={page_number}'
        response = requests.get(link, headers=header).text
        sleep(2)
        soup = BeautifulSoup(response, 'lxml')
        image_control = soup.find_all('img', class_='serp-item__thumb justifier__thumb')
        for image in image_control:
            image_link = 'https:' + image.get('src')
            print(image_link)
            yield (image_link)  # итератор

def download_image(image_link, image_name, folder_name):
    response = requests.get(image_link, headers=header).content
    file_name = open(os.path.join(os.path.join('dataset', folder_name), f"{image_name}.jpg"), 'wb')
    with file_name as handler:
        handler.write(response)

def run(animal_name):
    count = 0
    creating_folder(animal_name)
    for url in creating_url(animal_name):
        download_image(url, str(count).zfill(4), animal_name)
        count += 1
        sleep(2)
        print(count, ' downloaded')
##
##def cmp(image_1: cv2.Cat, image_2: cv2.Cat) -> bool:
  ##  dsize = (400, 400)
   ## test_1 = cv2.resize(image_1, dsize)
   ## test_2 = cv2.resize(image_2, dsize)
   ## return test_1 == test_2
##def remove_duplicate(path_dir):
  ##  if os.path.isdir(f'dataset/{path_dir}'):
    ##    path = f'dataset/{path_dir}'
      ##i, j = 0, 0
        ##length_names = len(names)
        ##while i < length_names:
          ##  j = i
            ##while j < length_names:
              ##  img_1 = cv2.imread(f'{path}/{names[i]}')
                ##img_2 = cv2.imread(f'{path}/{names[j]}')
                ##if np.all(cmp(img_1, img_2) == True) and i != j:
                  ##  print("DUblicate: ", names[i], " and ", names[j])
                    ##os.remove(f'{path}/{names[j]}')
              ##  j += 1
           ## print(names[i])
           ## names = os.listdir(path)
           ## length_names = len(names)
           ## i += 1
            ##