import requests
import asyncio
import json

def format_post_params(param):
    return json.loads(json.dumps(param))

async def do_get_request(req, data):
    return requests.get(req, params=data)

async def do_post_request(req,data):
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    return requests.post(req,data=data,headers=headers)

async def intruder(address, r_type, wordlist ):
    try:
        words_file = open(wordlist,'r')
        words_list = [word.strip() for word in words_file]
    
        if r_type == 'GET':
            for item in words_list:
                r_data = format_post_params(item)
                r = await do_get_request(address, r_data)
                size = r.headers['content-length']
                print(f'Request results: Params: {item} Code: {r.status_code} Size: {size}' )
        if r_type == 'POST':
            for item in words_list:
                r_data = format_post_params(item)
                r = await do_post_request(address, r_data)
                size = r.headers['content-length']
                print(f'Request results: Params: {item} Code: {r.status_code} Size: {size}' )
        words_file.close()
    except Exception as error: 
        print("Something went wrong. Can't connect with host")
        print(error)
