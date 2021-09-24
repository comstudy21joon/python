from phonebook.phonebook_menu import *


# 메인함수 선언
def main():
    while True:
        print("{:=^40}".format(" 주소록 "))
        no = menu();

        run(no)
        print("\n")

if __name__ == '__main__':
    main()