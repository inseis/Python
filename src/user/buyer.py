from src.user.user import User


class Buyer(User):
    def __init__(self, email, password, nickname, money):
        # 부모 사용
        super().__init__(email, password, nickname, money)
        self.__history = []

    def buy(self, item_name, item_price, product_id):
        if self.__money >= item_price:
            self.__money -= item_price  # 상품 가격만큼 돈을 차감
            self.__history.append(product_id)
            print(f"{self.__nickname}님이 {item_name}를 구매하셨습니다.")
        else:
            print(f"{self.__nickname}님의 잔액이 부족합니다.")

    def add_money(self, amount):
        self.__money += amount
        print(f"{self.__nickname}님이 {amount}만큼 계좌를 충전하셨습니다.")

    def use_coupon(self, code):
        if code == "Ahssadassa":
            discount = self.__money * 0.1
            self.__money -= discount
            print(f"{self.__nickname}님의 계좌에서 {discount}만큼 할인되었습니다.")

    def add_to_cart(self, item_name, item_price):
        self.__cart.append({"name": item_name, "price": item_price})
        print(f"{self.__nickname}님의 장바구니에 {item_name}를 추가하였습니다.")

    def showcart(self):
        print(f"{self.__nickname}님의 장바구니 속")
        for item in self.__cart:
            print(f"{item['name']}, {item['price']}원")


if __name__ == "__main__":
    pass
