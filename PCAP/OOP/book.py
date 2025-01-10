class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        # Encapsulation: private attributes
        self.__price = price
        self.__discount = None
    def set_discount(self, discount):
        self.__discount = discount
    def get_price(self):
        if self.__discount:
            return self. __price * (1-self.__discount)
        return self.__price
    def __repr__(self):
        return "Título: {self.title}, Cantidad: {self.quantity}, " \
           "Autor: {self.author}, Precio: {round(self.get_price(), 3)} €"
