
fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

txtList = []

for file in fileList:
    if file.endswith('.txt'):
        txtList.append(file)


print("This is a test: {}, and then {}".format(txtList[0],txtList[1]))
         

    
