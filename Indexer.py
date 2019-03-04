
from collections import defaultdict
from bs4 import BeautifulSoup as BS
from uuid import uuid4
import requests, re

link = "https://en.wikipedia.org/wiki/Main_Page"

req = requests.get(link)

soup = BS(str(req.content), 'lxml')

nodes = soup.findAll()

REFERENCES = defaultdict(lambda:[])
IDS = defaultdict(lambda:str(uuid4()))

docId = IDS[link]

def getTags(nodes):
    tags = set([])
    for n in nodes:
        tags.add(n.name)
    return tags

def getText():
    pass
