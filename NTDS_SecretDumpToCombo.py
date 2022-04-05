import argparse
import sys
from os.path import exists

def create_combos(args):
    dump = args.dump
    outfile = args.outfile
    with open(dump, "r", encoding="utf-8") as dumpfile:
        for line in dumpfile:
            if ":::" in line:
                line = line.replace(":::", "")
                items = line.split(":")
                username = items[0]
                ntlm_hash = items[3]
                with open(outfile, "a", encoding="utf-8") as file:
                    if args.verbose:
                        print(username+ ":"+ ntlm_hash.replace("\n", ""))
                    file.write(username+ ":"+ ntlm_hash)

def error_handler():
    if len(sys.argv) >= 5:
        args = parser.parse_args() 
        if exists(args.dump):
            return args
        else:
            print(f"File {args.dump} does not exists")
            sys.exit(1)
    parser.print_help()
    sys.exit(1)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This script converts the output of secretsdump to the format "username:hash"')
    parser.add_argument('-d', dest="dump", help="File with secretsdumps output",type=str, required=True)
    parser.add_argument('-o', dest="outfile", help="Output file",type=str, required=True)
    parser.add_argument('-v', dest="verbose", help="Print Combos", action="store_true")
    args = error_handler()       
    create_combos(args)  


