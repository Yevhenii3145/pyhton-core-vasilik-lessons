def taxer(base_tax): # налоги
    def calculate(money):
        nonlocal base_tax
        if money >= 10_000: # если заработали более 10_000
            base_tax = 1.5 * base_tax # увеличиваем ставку налога
        return money - base_tax * money
    return calculate

ukr = taxer(0.1)
swd = taxer(0.55)

money_ukr_1 = ukr(15000) # мутируем nonlocal base_tax
money_swd = swd(25000)
money_ukr_2 =  ukr(5000) # здесь уже base_tax = (0.1 * 1.5)

print(money_ukr_1, money_swd,money_ukr_2)
