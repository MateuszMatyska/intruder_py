import requests
import asyncio
import sys

def read_extensions():
    extensions = open("extensions_common.txt", 'r')
    return [ext.strip() for ext in extensions]
    extensions.close()

async def do_request(req):
    return requests.get(req)

async def scan_possible_urls(address, wordlist = "common.txt"):
    try:
        exts = read_extensions()
        words_file = open(wordlist,'r')
        words_list = [word.strip() for word in words_file]
        ok_addresses = []
        for item in words_list:
            for ext in exts:
                req = f'{address}/{item}{ext}'
                connection = await do_request(req)
                if connection.status_code == requests.codes.ok:
                    print(f'{req} : -- Status OK {connection.status_code}')
                    ok_addresses.append(f'{req} : -- Status OK {connection.status_code}')
                else:
                    print(f'{req} : {connection.status_code}')
                    sys.stdout.write("\033[F") #back to previous line 
                    sys.stdout.write("\033[K") #clear line 

        return ok_addresses
        words_file.close()
    except: 
        print("Something went wrong. Can't connect with host")