class Student:
    def __init__(self, name, grade, student_number, sex, address, phone_number, year): # __init 함수는 초기화를 자동으로 시켜주는 메소드이다.
        self.name = name #매개변수인 self는 메소드를 호출한 객체가 자동으로 전달된다.
        self.grade = grade
        self.student_number = student_number
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.year = year

while Student:
    str(input("객체 명을 입력하시오.(단, 영문으로): "))
    if input == "종료": #종료가 입력되면 밑에 break가 작동하도록 입력
        break #뒤에 질문을 멈추기 위해 사용

    def introduce_name(self):
        str(print("이름을 입력하시오.(단, 한글로): "))

    def introduce_grade(self):
        int(print("학년을 입력하시오.(단, 숫자로): "))

    def introduce_student_number(self):
        int(print("학번을 입력하시오.(단, 숫자로): "))

    def introduce_sex(self):
        str(print("성별을 입력하시오.(모를 때는 모른다 라고 입력.): "))
        if introduce_sex == "모른다":
            introduce_sex == "None"

    def introduce_address(self):
        str(print("주소를 입력하시오.(~시까지만): "))

    def introduce_phone_number(self):
        str(print("전화번호를 입력하시오.(모를 때는 모른다 라고 입력.): "))
        if Student.phone_number == "모른다":
           Student.phone_number == "None"

    def introduce_year(self):
        int(print("멋사 몇년차인가요?(단, 숫자로): "))
        if introduce_year == 1: #1이 입력되면 41번째 줄이,
            print("멋사 1년차 우와 아기사자다!")
        else: #그렇지 않으면 43번째 줄이 나오도록 입력
            print("멋사 n년차 우와 운영진이다!")

eunji = Student("이은지", "2학년", "202111048", "여자", "까치산", "010-6284-4144", "20020817") #name 매개변수의 값을 eunji.name인 인스턴스 변수에 저장(다른 변수도 동일)

eunji.introduce_name() #인스턴스 변수나 메소드 사용하기 위해 객체.인스턴스 변수 입력
eunji.introduce_grade()
eunji.introduce_student_number()
eunji.introduce_sex()
eunji.introduce_address()
eunji.introduce_phone_number()
eunji.introduce_year()