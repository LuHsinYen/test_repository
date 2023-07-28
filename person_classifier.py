#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os
import re

from pprint import pprint

##20230728


personPatLIST = ["^{}，{{0,1}}[^a-zA-Z。]+人\b",
                 "^{}，{{0,1}}[^a-zA-Z。]+人+[，|。]",
                 "^{}，(別名|本名|原名|字|男|女|現任|時任)"
                 ]

# personPatLIST = ["^{}，現任"]

dataDIR = "./data/test"

def main(entryDIR):
    """
    分辨 fileLIST 中的每一個 json 檔，看它是不是屬於「人類」。如果是的話，就加入列表 [PersonLIST] 中
    """
    personLIST = []
    for json_f in os.listdir(entryDIR):
        # print(json_f)
        try:
            with open("{}/{}".format(entryDIR, json_f), encoding="utf-8") as f:
                topicSTR = json_f.replace(".json", "")
                entrySTR = json.load(f)["abstract"]
            for p in personPatLIST:
                pat = re.compile(p.format(topicSTR))
                if len(list(re.finditer(pat, entrySTR))) > 0:
                    personLIST.append(topicSTR)
                else:
                    pass
        except IsADirectoryError:
            pass
    return personLIST


if __name__ == "__main__":
    
    personLIST = []
    for init_s in os.listdir(dataDIR)[:]:
        if init_s.startswith("._"):
            pass
        else:
            personLIST.extend(main("{}/{}".format(dataDIR, init_s)))

    with open("人物.txt","w",encoding = 'utf-8') as f:
        f.write(str(personLIST))
        
    pprint(personLIST)