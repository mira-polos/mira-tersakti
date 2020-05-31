#import module
import os
import requests
os.system('clear')
banner = """
\033[1;91m           |------------------------------------------|
\033[1;93m           |  SELAMAT DATANG DI TOOLS MIRA TERSAKITI  |
\033[1;91m           |------------------------------------------|
\033[1;92m    UNTUK MENGGUNAKAN TOOLS INI GUNAKAN http/https jangan www
"""


os.system('toilet -f mono9 X-Target')
print banner
#input target
target = raw_input('[Web Target]>  ')


#open wordlist
f = open('wordlist.txt','r')
kontent = f.read()
x = kontent.split('\n')


for i in x:
     url = target+"/"+i
     code = requests.get(str(url)).status_code
     if code == 200:
             print "[+]BERHASIL | url : "+url
else :
             print "[-]GAGAL | url : "+url
