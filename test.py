# 인사하는 함수

# 1. 이름과 나이를 받는다
# 2. 나이가 10살 미만이면 "안녕"이라고 인사한다
# 3. 나이가 10살 이상 20살 미만이면 "안녕하세요"라고 인사한다
# 4. 그 외에는 "안녕하십니까"라고 인사한다

def Greet(name, age):
    if age < 10:
        print("안녕, " + name + "야~")
    elif 10 <= age < 20:
        print(name + "님, " "안녕하세요!")
    else:
        print(name + "님, " + "안녕하십니까?")
        
Greet("Dev", 9) # 안녕, Dev야~
Greet("Honing", 10) # Honing님, 안녕하세요!
Greet("BHN", 21) # BHN님, 안녕하십니까?