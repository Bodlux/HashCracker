filename = "combo.txt"
hash_list = []
with open(filename, "r", encoding='ISO-8859-1') as file:
    f = file.read().split("\n")

for item in f:
    if ":" in item:
        hash = item.split(":")[1] + "\n"
        hash_list.append(hash)


file = open("hash.txt", "w")
for hash in hash_list:
    file.write(hash)
file.close()