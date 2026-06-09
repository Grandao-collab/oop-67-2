rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency.upper()

    def convert_to_kgs(self) -> float:
        if self.currency in rates:
            return self.amount * rates[self.currency]
        else:
            raise ValueError(f"Валюта {self.currency} не поддерживается.")

    def __str__(self) -> str:
        return f"{round(self.amount, 2)} {self.currency}"

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        total_kgs = self.convert_to_kgs() + other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        total_kgs = self.convert_to_kgs() - other.convert_to_kgs()
        return Money(total_kgs, "KGS")

    def __mul__(self, number: float):
        if not isinstance(number, (int, float)):
            return NotImplemented
        return Money(self.amount * number, self.currency)

    def __truediv__(self, number: float):
        if not isinstance(number, (int, float)):
            return NotImplemented
        if number == 0:
            raise ZeroDivisionError("Деление на ноль.")
        return Money(self.amount / number, self.currency)


ashe_money = Money(100, "USD")
gangplank_money = Money(5000, "KGS")

result_add = ashe_money + gangplank_money
print(result_add)

daven_money = gangplank_money - ashe_money
print(daven_money)

camille_money = Money(75, "EUR")
result_mul = camille_money * 2
print(result_mul)

tf_money = Money(150, "RUB")
result_div = tf_money / 2
print(result_div)