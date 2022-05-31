class Student:
    def __init__(self, name, grade, student_number, sex, address, phone_number, year): # __init 함수는 초기화를 자동으로 시켜주는 메소드이다.
        self.name = name #매개변수인 self는 메소드를 호출한 객체가 자동으로 전달된다.
        self.grade = grade
        self.student_number = student_number
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.year = year

    def introduce(self):
        print("이름은 %s이다." % self.name)
        print("학년은 %d이다." % self.grade)
        print("학번은 %d이다." % self.student_number)
        print("성별은 %s이다." % self.sex)
        print("주소는 %s이다." % self.address)
        print("전화번호는 %s이다." % self.phone_number)
        if(self.year == "1"): #1이 입력되면 20번째 줄이,
            print("멋사 %s년차" % self.year)
            print("우와 아기사자다!")
        else: #그렇지 않으면 23번째 줄이 나오도록 입력
            print("멋사 %s년차" % self.year)
            print("우와 운영진이다!")

while True:
    Class_name = input("객체 명을 입력하시오.(단, 영문으로): ")
    if(Class_name == "종료"): #종료가 입력되면 밑에 break가 작동하도록 입력
        break #뒤에 질문을 멈추기 위해 사용
    name = input("이름을 입력하시오.(단, 한글로): ")
    grade = int(input("학년을 입력하시오.(단, 숫자로): "))
    student_number = int(input("학번을 입력하시오.(단, 숫자로): "))
    sex = input("성별을 입력하시오.(모를 때는 모른다라고 입력.): ")
    if(sex == "모른다"):
        sex = "None"
    address = input("주소를 입력하시오.(~시까지만): ")
    phone_number = input("전화번호를 입력하시오.(모를 때는 모른다라고 입력.): ")
    if(phone_number == "모른다"):
        phone_number = "None"
    year = input("멋사 몇 년차인가요?(단, 숫자로): ")