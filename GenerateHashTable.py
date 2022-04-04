import time
import hashlib,binascii
from turtle import st
import progressbar
import datetime


def generateWordlist(filename):
    with open(filename, "r", encoding='ISO-8859-1') as file:
        f = file.read().split("\n")
    
    file = open("generated_hash.txt", "w", encoding='ISO-8859-1')

    bar = progressbar.ProgressBar(maxval=len(f), \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()

    for index,item in enumerate(f):
        ntlm_hash = binascii.hexlify(hashlib.new('md4', item.encode('utf-16le')).digest()).decode("utf-8")
        file.write(ntlm_hash+":"+item+"\n")
        bar.update(index)
    file.close()
    bar.finish()


if __name__ == "__main__":
    start = datetime.datetime.now()
    filename = input("Enter The Path To The Wordlist: ")
    generateWordlist(filename)
    stop = datetime.datetime.now()
    print(stop-start)