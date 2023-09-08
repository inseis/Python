class User(object):
    # 클래스 속성
    __auto_increment_number = 0

    # 클래스 메소드
    @classmethod
    def increment_user_id(cls):
        cls.__auto_increment_number += 1

    # 생성자
    def __init__(self, email, password, nickname, money):
        # 클래스 속성 초기화
        User.increment_user_id()

        # 인스턴스 속성 초기화
        self.__user_id = User.__auto_increment_number
        self.__email = email
        self.__password = password
        self.__nickname = nickname
        self.__money = money

    # 인스턴스 메소드
    def get_user_id(self):
        return self.__user_id

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


if __name__ == "__main__":
    pass
