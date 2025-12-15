# w, a, r+

# with open('file.txt','w') as f: # the write mode will delete the old data nad write new data 
#     # data = f.read()
#     f.write('hello there\nWelcome to my tutorial')
    # print(data)


# with open('file.txt','a') as f:
#     f.write('\nplease do it')  # By using you can write new data without deleting old data
#     # This method also creal file if it not exist.abs

# 'r+' ,method is use if you want ot wread and write at the same moment. 
# 'r+' method will create error if the fiel dosent exist

with open('file.txt','r+') as f:
    f.seek(len(f.read()))
    f.write("Please do it")