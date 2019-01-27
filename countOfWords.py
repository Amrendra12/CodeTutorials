#Count the number of words in a file

with open("messages.txt","r") as doc1:
    countUpper = 0
    countLower = 0
    text= doc1.readlines()
    for line in text:
        words=line.split()
        #if words.islower()
		#count+=1
        for abc in words:
            #count12=0
            if (abc.isupper())==True:
                countUpper+=1
            if (abc.islower())==True:
                countLower+=1

print "Upper letter count in a file:",countUpper
print "Lower letter count in a file:",countLower
        