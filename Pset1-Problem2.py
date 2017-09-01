s = 'azcbobobegghakl' #won't exist in the final problem solution
bobCounter = 0;
for index, item in enumerate(s):  #note the absence of "while" loop, I'm using enumerate()
    if (index<=len(s)-3):
        if (s[index] == 'b' and s):
            if (s[index+1] == 'o'):
                if (s[index+2] == 'b'):
                    bobCounter = bobCounter + 1
print ("Number of times bob occurs is: "+str(bobCounter))
