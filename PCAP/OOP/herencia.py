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
class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return f"Título: {self.title}, Género: {self.branch}, Cantidad: {self.quantity}, Autor: {self.author}, Precio: {round(self.get_price(), 3)} €"

novela1 = Novel('La Comunidad del anillo', 30, 'J.R.R. Tolkien', 30, 560)
novela1.set_discount(0.20)

ensayo1 = Academic('Modernidad líquida', 12, 'Z. Bauman', 18, 'Sociología')

print(novela1)
print(ensayo1)
