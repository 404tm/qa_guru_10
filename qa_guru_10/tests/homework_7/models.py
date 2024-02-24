class Product:
    """
    Класс продукта
    """
    name: str
    price: 5
    description: str
    quantity: 15

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:

        for quantity in Product:
            if quantity >= 10:
                return True



        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        raise NotImplementedError

    def buy(self, quantity):

        if self.check_quantity(quantity) < 10:
            raise ValueError

        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        raise NotImplementedError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс продукта
    """

    def __init__(self, card, items, description, quantity):
        self.card = card
        self.items = items
        self.description = description
        self.quantity = quantity
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {0}

    def add_product(self, product: Product, buy_count=1):

        for items in self.card:
            if items.product == product:
                items.quntity += buy_count
                return items

        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):

        for item in self.card:
            if item.product == product:
                if remove_count is None or remove_count >= item.quantity:
                    self.card.remove(item)
                else:
                    item.quantity -= remove_count
                return
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def get_total_price(self) -> float:
        raise NotImplementedError

    def buy(self):
        for item in self.card:
            if item.product.stock < item.quantity:
                raise ValueError(f"Недостаточно товара '{item.product.name}' на складе")
            item.product.stock -= item.quantity
        self.card.clear()
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        raise NotImplementedError