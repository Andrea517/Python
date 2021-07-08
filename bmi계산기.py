"""
bmi 지수 측정기 (비만)
함수 이름 : bmi
bmi = 몸무게 / (키X키)
18.5이하 = 저체중
18.5 ~ 23 = 정상
23 ~ 25 = 과체중
25 ~ 30 = 비만
30이상 = 고도비만
bmi(키,몸무게) = 호출
"""
name = input("안녕하세요. 당신의 이름은 무엇인가요? ")
print("반갑습니다. %s님." %name[1:3])
height = float(input("당신의 키는 몇입니까? "))
weight = float(input("당신의 몸무게는 몇인가요? "))
print("키 : %s" %height)
print("몸무게 : %s" %weight)
