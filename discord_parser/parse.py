
import os
import json
from time import sleep

names = []

filename = "example.json"
currentDirectory = ""

os.chdir(currentDirectory)

with open(filename, encoding="utf8") as f:
   data = json.load(f)

for i in data:
   if i == "messages":
      msg = data[i]

      for element in msg:
        for index in element:
           
            if index == "content":
                words = element[index]
                
                if len(words) == 0:
                    print("Not Useful Empty")
                elif words[0] == "▬" or words[0] == '`':
                    print("Not Useful")
                else:
                    #sleep(0.1)
                    newWords = words.split('\n')

                    names.append(newWords[0])

                  
                   
shrunkList = []

def nameSynthesizer(entry):
    if entry == "" or entry[0] == "▬":
        names.remove(entry)
        return
    
    replaceSection = entry.replace("**ACCOUNT HAS SINCE BEEN BANNED**", "")
    replaceBold = entry.replace("*","")

    if replaceSection != entry:
        names.remove(entry)
        names.append(replaceSection)
        return
    
    if replaceBold != entry:
        names.remove(entry)
        names.append(replaceBold)
        return
    
    commas = entry.find(",")   
    if commas != -1:
        newWords = entry.split(",")
        names.append(newWords[0])
        names.remove(entry)
        return
    
    slash = entry.find("/")

    if slash != -1:
        newWords = entry.split("/")
        names.remove(entry)
        for nam in newWords:
            names.append(nam)
            return
        
    parenthesis = entry.find("(")
    if parenthesis != -1:
        if parenthesis == 0:
            names.remove(entry)
            return

    
    link = entry.find("http")

    if link != -1:
        if link == 0:
            names.remove(entry)
            return

            
    space = entry.find(" ")
    if space != -1:
        newWords = entry.split(" ")
        print(newWords)
        names.remove(entry)
        for nam in newWords:
            names.append(nam)
            return
        
for entry in names:
    nameSynthesizer(entry)

                    