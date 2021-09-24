# 문자열에서 이미지 태그를 찾아서 소스 경로를 변경 한다.
def replaceSRC(str1, newUrl) :
    #str1 = '''@@##<a href="asfasdfasf">@@@<a href="bsfasdfasfsdfsa">@@@<a href="sdfasdfsdafasdfc">@@@'''
    #newUrl = ["http://naver.com","http://daum.net","http://google.com"]

    lis = []
    startIdx = 0
    while True :
        try :
            startIdx = str1[startIdx:].index("<img") + startIdx +1
            endIdx = str1[startIdx+1:].index(">") + 1
            lis.append((startIdx-1, startIdx+endIdx) )
        except :
            break

    strSaver = []
    cnt = 0
    start = 0
    for i, point in enumerate(lis) :
        strSaver.append(str1[start:point[0]])
        strSaver.append('<img src="{}">'.format(newUrl[i] ) )
        cnt +=1
        if i < len(lis)-1 :
            start = point[1] + 1
        else :
            strSaver.append(str1[point[1]+1:])

    newStr = ""
    for s in strSaver :
        newStr += s

    return newStr


# 문자열에서 링크 태그를 찾아서 href 경로를 변경 한다.
def replaceHREF(str1, newUrl) :
    lis = []
    startIdx = 0
    while True :
        try :
            startIdx = str1[startIdx:].index("<a") + startIdx +1
            endIdx = str1[startIdx+1:].index(">") + 1
            lis.append((startIdx-1, startIdx+endIdx) )
        except :
            break

    strSaver = []
    cnt = 0
    start = 0
    for i, point in enumerate(lis) :
        strSaver.append(str1[start:point[0]])
        strSaver.append('<a href="{}">'.format(newUrl[i] ) )
        cnt +=1
        if i < len(lis)-1 :
            start = point[1] + 1
        else :
            strSaver.append(str1[point[1]+1:])

    newStr = ""
    for s in strSaver :
        newStr += s

    return newStr


if __name__ == '__main__':
   #print( replaceSRC("", []) )
   print( replaceHREF("", []) )