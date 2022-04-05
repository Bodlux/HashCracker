import time
import hashlib,binascii
from turtle import st
import progressbar
import datetime


def generateWordlist(filename):  
    with open(filename, "r", encoding='ISO-8859-1') as file:
        bar = progressbar.ProgressBar(maxval=len(file.readlines()), \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]) # Script Will Crash if the wordlist is to big. You can solve this issue by removing the code related to the progress bar
        bar.start()
        loop = True
        line = file.readline()
        counter = 0
        with open("generated_hash.txt", "w", encoding='ISO-8859-1') as f:
            while(loop):
                ntlm_hash = binascii.hexlify(hashlib.new('md4', line.encode('utf-16le')).digest()).decode("utf-8")
                f.write(ntlm_hash+":"+line)
                bar.update(counter)
                counter +=1
                line = file.readline()
                if(len(line) == 0):
                    loop=False
                
        bar.finish()


if __name__ == "__main__":
    start = datetime.datetime.now()
    filename = input("Enter The Path To The Wordlist: ")
    generateWordlist(filename)
    stop = datetime.datetime.now()
    print(stop-start)