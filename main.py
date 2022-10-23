import os
import bs4 import BeautifulSoup


def creating_folder(folder_name):
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    if not os.path.exists(os.path.join('dataset',folder_name)):
        os.mkdir(os.path.join('dataset',folder_name))