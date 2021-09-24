def replaceSRC(str1, srcList) :
    #str1 = """$#@#aa<img src="aaa">@@@<img src="bbbb">@@@<img src="cc">@@@"""
    #srcList = ["img/aa.jpg","img/bb.jpg","img/cc.jpg"]
    if len(srcList) == 0 :
        return str1

    newList = []
    findWord = 'src="'
    str2 = str1
    i = 0
    while str2.find(findWord) != -1  :
        if i<len(srcList) :
            startIdx = str2.find(findWord) + len(findWord);  # atart
            newList.append(str2[:startIdx])
            newList.append(srcList[i])
            str2 = str2[startIdx:]
            endIdx = str2.find('"'); # end
            str2 = str2[endIdx:]
        i+=1

    newList.append(str2)

    return "".join(newList)