from PIL import Image
import os
#Define Variables
key = "abcdefghijklmnopqrstuvwxyz" #Key for naming variables
VarKey = {}

for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    ConvertedList = []
    Values = []
    FinalOutput = []
    vars = ""
    filename = os.fsdecode(file)
    if filename.endswith(".png"):
        im = Image.open(file).convert("RGB")
        pic = im.load()
        assert pic is not None
        width,height = im.size

        #Add all RGB Values to a list
        for y in range(width):
            for i in range(height):
                ConvertedList.append(pic[i,y])
                
        #Add each value only once   
        for i in ConvertedList:
            if not i in Values:
                Values.append(i)

        #Assign values to variables
        x = 0
        for i in Values:
            vars = vars + key[x] + " = " + str(i) + "\n"
            #key
            if not str(i) in VarKey:
                VarKey[str(i)] = str(key[x])
            
            x += 1

        #Make final list
        x = 0
        for i in ConvertedList:
            FinalOutput.append(VarKey.get(str(i)))
            
        print("")
        print(f"[{(', ').join(FinalOutput)}]")
for i in VarKey:
    print(f"{VarKey[i]} = {i}")
