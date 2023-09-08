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

# 5. buyer가 seller의 product 5개를 모두 구매하세요 (잔액 부족으로 구매가 실패해야 합니다)
for product in products:
    if buyer.buy(seller, product):
        print(f"{buyer.balance}원으로 {product.title}를 구매했습니다.")
    else:
        print(f"잔액이 부족하여 {product.title} 구매에 실패했습니다.")

if buyer.buy(seller, products[0]):
    print(f"{buyer.balance}원으로 {products[0].title}를 구매했습니다.")
else:
    print(f"잔액이 부족하여 {products[0].title} 구매에 실패했습니다.")

print(f"Seller의 storage: {[product.title for product in seller.storage]}")
print(f"Seller의 잔액: {seller.balance}원")
print(f"Buyer의 purchases: {buyer.purchases}")


print("구매 내역:")
for product_id in buyer.history:
    for product in products:
        if product.productId == product_id:
            print(f" {product_id}:")
            buyer.print_product_info(product)
            print()
            break
