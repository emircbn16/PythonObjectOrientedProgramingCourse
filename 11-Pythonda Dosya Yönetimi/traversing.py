with open("NewFile.txt","r") as file:
    content = file.read(10)
    print(content)
    file.seek(0)
    print(file.tell())
    content2 = file.read(10)
    print(content2)

    