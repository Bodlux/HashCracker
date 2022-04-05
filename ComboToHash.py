import sys, argparse
from os.path import exists


def get_hashes(args):
    combo = args.combo
    outfile = args.outfile
    with open(combo, "r", encoding="utf-8") as combofile:
        for line in combofile:
            items = line.split(":")
            with open(outfile, "a", encoding="utf-8") as file:
                if args.verbose:
                    print(items[1].replace("\n", ""))
                file.write(items[1])


def error_handler():
    if len(sys.argv) >= 5:
        args = parser.parse_args() 
        if exists(args.combo):
            return args
        else:
            print(f"File {args.combo} does not exists")
            sys.exit(1)
    parser.print_help()
    sys.exit(1)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This script will extract all the hashes from a file with combos: "username:hash". Can be used in combination with NTDS_SecretDumpToCombo.py')
    parser.add_argument('-c', dest="combo", help="Combo file",type=str, required=True)
    parser.add_argument('-o', dest="outfile", help="Output file",type=str, required=True)
    parser.add_argument('-v', dest="verbose", help="Print hashes", action="store_true")
    args = error_handler()       
    get_hashes(args)  