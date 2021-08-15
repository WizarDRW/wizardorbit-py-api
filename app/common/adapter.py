class Target:
    """
    Hedef, istemci kodu tarafından kullanılan alan spesifik arayüzünü tanımlar.
    """

    def request(self) -> str:
        return "Hedef: Varsayılan hedefin davranışı."


class Adaptee:
    """
    Adapte, bazı faydalı davranışlar içeriyor, ancak arayüzü uyumsuz
    Mevcut müşteri koduyla.Adapte, önce biraz adaptasyona ihtiyacı var.
    İstemci kodu kullanabilir.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    Adaptör, Adapte'nin arayüzünü hedefle uyumlu hale getirir
    Birden fazla miras yoluyla arayüz.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    Müşteri kodu, hedef arayüzü takip eden tüm sınıfları destekler.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Müşteri: Hedef nesnelerle gayet iyi çalışabilirim:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Müşteri: Adaptee sınıfının garip bir arayüzü var."
          "Bak, anlamıyorum:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Müşteri: Ama adaptör aracılığıyla onunla çalışabilirim:")
    adapter = Adapter()
    client_code(adapter)