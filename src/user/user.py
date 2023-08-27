class User(object):
    # 생성자
    def __init__(self, email, password, nickname, money):
        # 데이터: 인스턴스 속성
        self.email = email
        self.password = password
        self.nickname = nickname
        self.money = money

    # 함수: 인스턴스 메소드
    def get_email(self):
        return self.email

    def set_email(self, new_email):
        self.email = new_email


if __name__ == "__main__":
    pass
