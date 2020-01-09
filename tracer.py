import os
import sys
import logging
import subprocess

transfer_list = []

analyst_cache = {}

def getLDDResultOf(target, level):
    if analyst_cache.get(target) is not None:
        return []
    analyst_cache[target] = True

    lvl_prompt = ['-'] * level
    lvl_prompt = ''.join(lvl_prompt)
    neededList = []

    ret = subprocess.check_output("ldd "+target, shell=True)
    splitret = str.split(ret.decode('utf-8'), '\n\t')

    for ld in splitret:
        if "=>" in ld:
            print(lvl_prompt, "ext", ld.strip(), "...")
            tmpsplit = str.split(ld, "=>")[1]
            tmpsplit = str.split(tmpsplit, "(")[0]
            # print("extracted:", tmpsplit, "from", ld)
            neededList.append(tmpsplit.strip())

    # recursive
    if len(neededList) != 0:
        tmpList = neededList
        for r in tmpList:
            r_list = getLDDResultOf(r, level+1)
            neededList.extend(r_list)

    return list(dict.fromkeys(neededList))

# folder included
#entry = "/usr/lib/aarch64-linux-gnu/"
#inputs = os.listdir(entry)
#for f in inputs:
#    if "libopencv" in f:
#        transfer_list.append(f)

group_list = []
for f in transfer_list:
    print("progress:", transfer_list.index(f), "/", len(transfer_list))
    t = getLDDResultOf(entry+f, 0)
    group_list.extend(t)

print(list(dict.fromkeys(group_list)))
