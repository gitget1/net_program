from socket import *

def calculate(expr):
    expr = expr.replace(' ', '') #공백유무 따지지 않고 계산가능하게 처리함
    operators = ['+', '-', '*', '/'] #사칙연산
    for op in operators: #연산자를 순차적으로 확인해서 그에 맞는 계산을함
        if op in expr:
            try:
                left, right = expr.split(op) 
                a = int(left)
                b = int(right) #좌측과 우측을 정수로 변환해서 a,b에 저장
                if op == '+':
                    return str(a + b) # '+'일경우  a + b값을 더해서 문자열값으로 변환
                elif op == '-':
                    return str(a - b)# '-'일경우  a - b값을 빼서 문자열값으로 변환
                elif op == '*':
                    return str(a * b)# '*'일경우  a x b값을 곱해서 문자열값으로 변환
                elif op == '/':# '/'일경우  a / b값을 나눠서 문자열값으로 변환, 만약 0일경우 오류 메세지로 변환함
                    if b == 0:
                        return '오류!!!(나눌수없습니다!!!)'
                    return f'{a / b:.1f}' #나눈값을 소수점 1의 자리까지 출력
            except:
                return 'Error' # 계산식 잘못될경우 error출력
    return 'Invalid expression' # 계산식에 연산자나 잘못된 형식일경우 invalid expression 반환

s = socket(AF_INET, SOCK_STREAM) #ipv4 주소 사용, tcp소켓 사용
s.bind(('', 3333))#localhost의 3333번 포트 사용 및 네트워크 인터페이스 연결 허용
s.listen(5)#서버 최대 대기 큐 길이 (5개연결)

while True:
    client, addr = s.accept() #클라이언트와 통신할 client소캣,주소를 반환
    print('Connected from', addr) #연결된 주소 출력
    while True:
        data = client.recv(1024) #최대 1024바이트 데이터 수신가능
        if not data:
            break # 만약 데이터를 보내지 않거나 중간에 끊을 경우 break
        expr = data.decode()#수신된 바이트 데이터를 문자열로 변환
        if expr == 'q': # 만약 q를 입력할경우 break
            break
        result = calculate(expr) #계산식을 calculate 함수에 넘겨 계산결과를 받는다 
        client.send(result.encode()) #결과값을 바이트로 인코딩 해서 클라이언트에 다시 보낸다.
    client.close()
