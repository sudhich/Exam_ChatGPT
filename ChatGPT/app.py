import requests
from bs4 import BeautifulSoup
import os

HTMLFileToBeOpened = open("/config/workspace/ChatGPT/index.html", "r")
contents = HTMLFileToBeOpened.read()

soup = BeautifulSoup(contents, 'html.parser')
data = soup.text
os.remove('/config/workspace/ChatGPT/temp.txt')
os.remove('/config/workspace/ChatGPT/file.txt')

with open('/config/workspace/ChatGPT/temp.txt', 'w') as wf:
    data = str(data)
    wf.write(str(data))
result = ''

with open('/config/workspace/ChatGPT/temp.txt', 'r') as file:
    for line in file:
        if not line.isspace():
            result += line
    
    file.seek(0)  
    with open('/config/workspace/ChatGPT/file.txt', 'w') as wf:
        wf.write(result)
