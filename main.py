from PIL import Image

#Define Variables
key = "abcdefghijklmnopqrstuvwxyz" #Key for naming variables
ConvertedList = []
Values = []
VarKey = {}
FinalOutput = []
vars = ""

#Image stuff
im = Image.open('picture.png').convert("RGB")
pix = im.load()
width,height = im.size

#Add all RGB Values to a list
for y in range(width):
    for i in range(height):
        ConvertedList.append(pix[i,y])
        
#Add each value only once   
for i in ConvertedList:
    if not i in Values:
        Values.append(i)

#Assign values to variables
x = 0
for i in Values:
    vars = vars + key[x] + " = " + str(i) + "\n"
    #key
    VarKey[str(i)] = str(key[x])
    
    x += 1

#Make final list
x = 0
for i in ConvertedList:
    FinalOutput.append(VarKey.get(str(i)))
    
#Print everything
print("#Colors")
print(vars)
print("#Picture")
print("["+(', ').join(FinalOutput)+"]")

