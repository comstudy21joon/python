import os

os_name = os.name
print("os name : ", os_name)

cwd = os.getcwd()
print("현재 폴더 위치 : ", cwd)

list_dir = os.listdir()
print("하위 파일 및 디렉토리 : ")
for file_name in list_dir :
    print(file_name)

# 디렉토리 생성
#os.mkdir("new_dir", mode=0o777);

# 디렉토리 이름 변경
#os.rename("new_dir", "dir2")

# 지정된 디렉토리 삭제하기
#os.rmdir("new_dir")

# 지정된 파일 삭제하기
#os.unlink("test.txt")