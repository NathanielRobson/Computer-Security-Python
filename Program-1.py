with open('sfs.py', 'r') as fr:
    myNames = fr.readlines()
    fr.close()
    
with open('sfs.py', 'w') as fw:
    for i in range(51):
        fw.writelines(myNames[i])

    myString = myNames[51]
    s = myString[:-1]
    
    fw.writelines(s)
    fw.write("; print('Virus')")
    fw.write("\n")
    
    for i in range(52, 73):
        fw.writelines(myNames[i])

    fw.close()
        
