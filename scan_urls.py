import requests
import asyncio

async def do_request(req):
    return requests.get(req)

async def scan_possible_urls(address):
    words_list = open("common.txt",'r')

    
    for item in words_list:
        req = f'{address}/{item}'.strip()
        connection = await do_request(req)
        if connection.status_code == requests.codes.ok:
            print(f'{req} : -- Status OK {connection.status_code}')
        else:
            print(f'{req} : {connection.status_code}')



    words_list.close()