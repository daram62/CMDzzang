print('학번 : 2021312602, 이름 : 김민서')
print('<절대값 출력 프로그램>\n')

def toAbs (x):
    if x>0:
        return x
    else:
        return x*-1

a= int(input('숫자 입력:'))
nw= toAbs(a)

print('=> 절대값: %d'%nw)
    
