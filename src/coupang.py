from src.user.user import Seller

class Product(object):
    __auto_increment_number = 1

    def __init__(self, title, price, content, seller_id):
        self.productId = Product.__auto_increment_number
        self.title = title
        self.price = price
        self.content = content
        self.sellerId = seller_id
        Product.__auto_increment_number += 1

products = []

for i in range(5):
    product = Product(f"Product {i+1}", 10000, f"This is product {i+1}.", f"Seller {i+1}")
    products.append(product)

seller = Seller()


for product in products:
    seller.add_product(product)

class Buyer:
    history: list[Any]

    def __init__(self, balance=10000):
        self.balance = balance
        self.purchases = []
        self.history = []

    def buy(self, seller, product):
        if self.balance >= product.price:
            self.balance -= product.price
            seller.sell_product(product)
            self.purchases.append(product.productId)
            self.history.append(product.productId)
            return True
        else:
            return False

    def print_product_info(self, product):
        print(f"이름: {product.title}")
        print(f"가격: {product.price}원")
        print(f"상세 정보: {product.content}")

buyer = Buyer()


for product in products:
    if buyer.buy(seller, product):
        print(f"{buyer.balance}원으로 {product.title}를 구매했습니다.")
    else:
        print(f"잔액이 부족하여 {product.title} 구매에 실패했습니다.")
