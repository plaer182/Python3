salary = int(input('Введите сумму зарплаты за месяц> '))
credit = int(input('Введите сумму ежемесячного кредита> '))
utilities = int(input('Введите сумму задолженности за коммунальные услуги> '))
result = salary - credit - utilities
print('У вас останется\t' + str(result))
