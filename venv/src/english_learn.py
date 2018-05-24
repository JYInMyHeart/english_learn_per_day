import json

def loadFile():
    file = open("./english_words/2018_05_25.json","r",encoding="utf-8")
    jsonFile = json.load(file)
    i = 0
    total = len(jsonFile)
    way = input("1.zh->en 2.en->zh:")
    if(way == "2"):
        for b in jsonFile:
            print(b)
            i = i + 1
            answer = input()
            if (answer == jsonFile[b]):
                print("The answer is Correct!", i,"(", "/", total,")")
            else:
                print("The answer wrong! The correct answer is ", jsonFile[b],"(", i, "/", total,")")
    else:
        for b in jsonFile:
            print(jsonFile[b])
            i = i + 1
            answer = input()
            if(answer == b):
                print("The answer is Correct!","(",i,"/",total,")")
            else:
                print("The answer wrong! The correct answer is ",b,"(",i,"/",total,")")
loadFile()
