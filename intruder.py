from scan_urls import scan_possible_urls
import asyncio

def main():
    print("Intruder")
    asyncio.run(scan_possible_urls('http://172.17.0.2'))

if __name__ == "__main__":
    main()