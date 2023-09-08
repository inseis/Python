from src.user.user import User


class Seller(User):
    def __init__(self, email, password, nickname, money):
        # 부모 사용
        super().__init__(email, password, nickname, money)
        self.__storage = []

    def add_product(self, product_id):
        self.__storage.append(product_id)

    def delete_product(self, product_id):
        for product in self.__storage:
            if product["product_id"] == product_id:
                self.__storage.remove(product_id)
                return True
        return False
        _

    def sell(self, item_name, item_price, product_id):
        self.__money = self.__money + item_price
        self.__history.append(product_id)
        print(f"{self.__nickname}님이 {item_name}를 판매하셨습니다.")

    def add_money(self, amount):
        self.__money += amount
        print(f"{self.__nickname}님이 {amount}만큼 계좌를 충전하셨습니다.")

    def set_account_id(self, account_id):
        self.__accountId = account_id

    def get_account_id(self):
        return self.__accountId

    def get_storage(self):
        return self.__storage


if __name__ == "__main__":
    pass
