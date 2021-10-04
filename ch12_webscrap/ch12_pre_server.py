from socket import * #소켓 라이브러리 임포트

server = socket(AF_INET, SOCK_STREAM) #소켓 생성
server.bind(('127.0.0.1', 8088)) #서버 바인드
server.listen(1)

connection, addr = server.accept() #접속 허가

print(str(addr),'에서 접속이 확인되었습니다.') #접속되었을때 확인문


while True :
    data = connection.recv(1024) #데이터를 받을 준비
    print('받은 데이터 : ', data.decode('utf-8')) #데이터를 받는다

    send_data = '''{"direction":"L",
               "angle":90,
               "length": 60
            }'''.encode("utf-8")

    connection.send(send_data) #클라이언트쪽으로 보내는 문구
    print('메시지를 보냈습니다.') #문구가 보내진것을 확인하는 출력