import hashlib
import datetime
import zlib ,sys,time,base64

cracked_list = []
failed = 0
def load_hash_list(filename):
    hash_list = []
    
    with open(filename, "r", encoding='ISO-8859-1') as file:
        f = file.read().split("\n")
    for item in f:
        hash_list.append(item)
    return hash_list

def getHashes(hash_list,verbose):
    start_time = datetime.datetime.now()
    filename = "hash.txt"
    with open(filename, "r", encoding='ISO-8859-1') as file:
        f = file.read().split("\n")
    for item in f:
        #print(item)
        find_hash(hash_list,item,verbose)     #find_hash(hash_list,hashlib.md5(item.encode('ISO-8859-1')).hexdigest(),verbose)
    print("\n\33[31m" + str(len(cracked_list)), "Hashes Succesfull Cacked!!!\33[37m")
    print("\33[31m" + str(failed), "Hashes Failed!\33[37m")
    end_time = datetime.datetime.now()
    print("\33[31mTime To Crack:", end_time-start_time,"\33[37m")
        

def find_hash(hash_list, hash,verbose):
    return crack_hashes(hash_list, hash, 0, len(hash_list),verbose)

def crack_hashes(hash_list,hash,begin,end,verbose):
    global cracked_list
    global failed
    if (end -begin) > 0:
        mid = (begin + end) //2
        mid_hash = hash_list[mid]
        if hash < mid_hash.split(':')[0]:
            return crack_hashes(hash_list,hash,begin,mid,verbose)
        elif hash > mid_hash.split(':')[0]:
            return crack_hashes(hash_list,hash,mid+1,end,verbose)
        else:
            if verbose:
                print("\33[31m[" + str(len(cracked_list)+1) + "]Hash Cracked => "+mid_hash+ "\33[37m")
            cracked_list.append(mid_hash)
            return mid_hash
    else:
        failed +=1
        not_found = "Hash Not Found"
        return not_found

def get_file_name():
    print("\33[31m1. MD5\n\33[31m2. SHA256\n\33[31m3. SHA512\n")
    hash_type = int(input("Chose a hash type : "))
    while  1 < hash_type > 3:
        print("Incorrect number")
        hash_type = print("\33[31m1. MD5\n2. SHA256\n3. SHA512\n")
        hash_type = int(input("\33[31mChose a hash type : "))
    
    if hash_type == 1:
        filename = "MD5.HList"
    elif hash_type == 2:
        filename = "SHA256.HList"
    elif hash_type == 3:
        filename = "SHA512.HList"
    print("\33[32mLoading Passwords ....\33[37m")  
    return filename

def main():
    verbose = input("\33[31mDo You Want A Verbose Output?[Y/n] : \33[37m")
    if verbose == "y" or verbose == "" or verbose == "Y":
        verbose = True
    else:
        verbose = False 
    input("\33[31mPress A Key To Crack The Hashes!\33[37m")
    print("\33[31mCracker Started...\33[37m")
    getHashes(hash_list,verbose)

if(__name__=="__main__"):
    print('\33[34m' + "██╗  ██╗ █████╗ ███████╗██╗  ██╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ ")
    print("██║  ██║██╔══██╗██╔════╝██║  ██║    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗")
    print("███████║███████║███████╗███████║    ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝")
    print("██╔══██║██╔══██║╚════██║██╔══██║    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗")
    print("██║  ██║██║  ██║███████║██║  ██║    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║")
    print("╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\33[37m\n\n")  
    filename = get_file_name()                                                                             
    hash_list = load_hash_list(filename)
    print("\33[32mPasswords Loaded!!!\33[37m") 
    main()


 





                                                                                            