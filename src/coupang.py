from src.product.product import Product
from src.user.buyer import Buyer
from src.user.seller import Seller

if __name__ == "__main__":
    seller = Seller("seller@gmail.com", 1234, "seller", 0)

    products = []
    for i in range(5):
        product = Product(f"신상 맥북 에어 15인치", 10000, f"애플에서 내놓은 신형 노트북 맥북 에어입니다.", f"{seller.get_user_id()}")
        products.append(product)

    for product in products:
        seller.add_product(product.get_product_id())

    buyer = Buyer("buyer@gmail.com", 1234, "buyer", 10000)

    # 상품 5개의 총 금액 구하기
