class User(object):
    # 생성자
    def __init__(self, email, password, nickname, money, coupon):
        # 데이터: 인스턴스 속성
        self.__email = email
        self.__password = password
        self.__nickname = nickname
        self.__money = money
        self.__coupon = coupon

    # 함수: 인스턴스 메소드
    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def get_nickname(self):
        return self.__nickname

    def set_nickname(self, new_nickname):
        self.__nickname = new_nickname

    def get_money(self):
        return self.__money

    def set_money(self, new_money):
        self.__money = new_money

    def get_coupon(self):
        return self.__coupon

    def set_coupon(self, new_coupon):
        self.__coupon = new_coupon


if __name__ == "__main__":
    pass
