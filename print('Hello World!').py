name = 'Yevhen'
age = 33
if name and age >=18:
    print('alles gut')
else:
    print('try again')


class Animals:

    def __init__(self, name, age, rod) -> None:
        self.name = name
        self.age = age
        self.rod = rod


class Cat(Animals):

    def say_someone(self):
        return 'cat say meou'
    

cat = Cat('Tom', 6, 'kot')

print(cat.say_someone())
print(cat.age)