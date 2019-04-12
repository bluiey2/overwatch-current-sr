import requests
import time
import datetime

def SRUpdate(rank):
    with open('sr.txt', 'w') as f:
        f.write(rank)

def get_rank():
    try:
        r = requests.get("https://playoverwatch.com/en-us/career/pc/Bluey-11648")
        html = r.text
        string = 'u-align-center h5">'
        start = html.find(string)
        end = html.find('</div>', start)
        return html[start+len(string):end]
    except:
        print('error, no')
        return None

while True:
    rank = get_rank()
    if rank != None:
        SRUpdate(rank)
        print(f"{datetime.datetime.now()} {rank}")
    time.sleep(480)
