from scan_urls import scan_possible_urls
from intruder import intruder
from help import display_help
import asyncio
import argparse

class CustomFormatter(argparse.HelpFormatter):
    def add_argument(self, action):
        if action.help == 'SUPPRESS':
            return
        help_text = self._expand_help(action)
        self._add_item(self._format_action, (action, help_text))

def check_arg_value(value_arg, default_value):
    if value_arg is not None:
        return value_arg
    else:
        return default_value

def run_scanner(address, wordlist):
    wordlist_file_name = check_arg_value(wordlist, "common.txt")
    address = check_arg_value(address, "http://172.17.0.2")
    
    results = asyncio.run(scan_possible_urls(address, wordlist_file_name))
    return results

def run_intruder(address, r_type, wordlist):
    wordlist_file_name = check_arg_value(wordlist, "common.txt")
    address = check_arg_value(address, "http://172.17.0.2")
    r_type = check_arg_value(r_type, 'GET')
    
    results = asyncio.run(intruder(address, r_type, wordlist))
    return results

def main():
    parser = argparse.ArgumentParser(description="Intruder_PY", add_help=False, formatter_class=CustomFormatter)
    parser.add_argument("-h","--help", action='store_true')
    parser.add_argument("-m", "--mode")
    parser.add_argument("-w", "--wordlist")
    parser.add_argument("-a", "--address")

    args = parser.parse_args() 
    
    if args.help is True:
        display_help()
    else:
        if args.mode == "s":
            run_scanner(args.address, args.wordlist)
        elif args.mode == "i":
            run_intruder(args.address, 'POST', args.wordlist)
        else:
            display_help()

    

if __name__ == "__main__":
    main()