from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
        The Creator Class
    """

    @abstractmethod
    def factory_method(self):
        """Note that the Creator"""
        pass

    def some_operation(self) -> str:
        """Also note that, despite its name, the Creator's primary responsibility is not creating products."""
        product = self.factory_method()

        result = f"Creator: {product.wizard()}"

        return result


class ConcreteCreator1(Creator):
    """Note that the signature of the method still uses the abstract product type."""

    def factory_method(self) -> Product:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()

class Product(ABC):
    """The Product interface declares the operations that all concrete product must implement"""

    @abstractmethod
    def operation(self) -> str:
        pass

    @abstractmethod
    def wizard(self) -> str:
        pass

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"
    def wizard(self) -> str:
        return "{Result of the ConcreteProduct1 Wizard}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"
    def wizard(self) -> str:
        return "{Result of the ConcreteProduct2 Wizard}"

def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works. {creator.some_operation()}")

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1")
    result = ConcreteCreator2()
    client_code(result)