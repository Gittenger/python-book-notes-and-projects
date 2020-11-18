def commaCode(paramList):
    str = ''
    for i in range(len(paramList) - 1):
        str = str + paramList[i] + ', '
    str = str + 'and ' + paramList[len(paramList) - 1]
    print(str)

spam = ['apples', 'bananas', 'tofu', 'test', 'cats']
commaCode(spam)
