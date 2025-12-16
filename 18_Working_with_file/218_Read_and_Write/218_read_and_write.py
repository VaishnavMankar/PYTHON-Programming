# This code read data from file2.txt and write in file1.txt
with open('file2.txt','r') as rf:
    with open('file1.txt','w') as wf:
        wf.write(rf.read())    