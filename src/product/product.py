class Product(object):
    __auto_increment_number = 1

    def __init__(self, title, price, content, seller_id):
        self.productId = Product.__auto_increment_number
        self.title = title
        self.price = price
        self.content = content
        self.sellerId = seller_id
        self.__class__.__auto_increment_number += 1


if __name__ == "__main__":
    pass
