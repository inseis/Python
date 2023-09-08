class Product(object):
    # 클래스 속성
    __auto_increment_number = 1

    # 클래스 메소드
    @classmethod
    def increment_product_id(cls):
        cls.__auto_increment_number += 1

    def __init__(self, title, price, content, seller_id):
        self.__product_id = Product.__auto_increment_number
        self.__title = title
        self.__price = price
        self.__content = content
        self.__seller_id = seller_id
        Product.increment_product_id()

    def get_product_id(self):
        return self.__product_id

    def get_price(self):
        return self.__price


if __name__ == "__main__":
    pass
