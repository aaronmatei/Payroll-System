# from datetime import datetime
# birthday = datetime(1992, 11, 22, 9, 30, 45)
# print(birthday.day)
# print(birthday.month)
# print(birthday.date())
# print(birthday.hour)
# print(birthday.weekday())
# print(birthday.now())

sq_iterator1 = [x**2 for x in range(0,11)]
print(sq_iterator1)

sq_iterator = (x**2 for x in range(0,11))
print(sq_iterator)

for x in sq_iterator:
    print(x)