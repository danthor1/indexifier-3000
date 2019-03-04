
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
TAGS = set(["h1","h2","h3","h4","h5","p"])
REPLACE = ["\\n","\\t","\n","\t"] #characters to replace with ""
STOP_WORDS = set(["the","in","a","I",""]) #can be statistically modified
FILTERS = set(["poop"])
REMOVE = STOP_WORDS | FILTERS

docId = IDS[link]

def getTags(nodes):
    tags = set([])
    for n in nodes:
        tags.add(n.name)
    return tags

def extractAllWords(nodeStrs):
    global REPLACE
    global REMOVE
    
    words = set([])
    for s in nodeStrs:
        for j in REPLACE:
            s = s.replace(j,"")
        words = words | set(s.split(" "))

    return words - REMOVE

def updateRefs(docId, words):
    global REFERENCES
    
    for word in words:
        REFERENCES[word].append(docId)
        

foundTags = TAGS & getTags(nodes)

targets = [node for node in nodes if node.name in foundTags]

nodesText = [str(targ.getText()) for targ in targets]

words = extractAllWords(nodesText)

updateRefs(docId, words)

if(__name__=="__main__"):
    import sys

    
