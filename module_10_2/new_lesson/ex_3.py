# Реализовать класс, который будет на вход принимать какое-то число,
# и будет возвращать сколько монет может входить в эту сумму. Например:
# In: 185
# Out: {50: 3, 25: 1, 10: 1, 5: 0, 2:0, 1: 0}


class Coins:
    def __init__(self, total_sum: int) -> None:
        self._coins = (1, 2, 5, 10, 25, 50)
        self.total_sum = total_sum

    def change(self):
        result = {}
        item = len(self._coins) - 1

        while item >= 0:
            coin = self._coins[item]
            num_of_coin = self.total_sum // coin
            result[coin] = num_of_coin
            self.total_sum -= coin * num_of_coin
            item -= 1
        return result


a = Coins(185)
print(a.change())  # {50: 3, 25: 1, 10: 1, 5: 0, 2: 0, 1: 0}
