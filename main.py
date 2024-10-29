import datetime
print("Task 1-3".center(60, "="))

print("Without @:".center(60, "#"))

def my_decorator(f):
    def wrappper():
        print("*" * 20)
        f()
        print("*" * 20)
    return wrappper
def current_time():
    current_time = datetime.datetime.now()
    print(f"{current_time:%H:%M}")

dec_func = my_decorator(current_time)
dec_func()

def my_decorator_decorator(f):
    def wrappper():
        print("~" * 20)
        f()
        print("~" * 20)
    return wrappper
dec_dec_func = my_decorator_decorator(dec_func)
print("dec_dec_func:".center(60))
dec_dec_func()

print("With @:".center(60, "#"))

def my_decorator1(f):
    def wrapper():
        print("*"*20)
        f()
        print("*"*20)
    return wrapper
def my_decorator2(f):
    def wrapper():
        print("#"*20)
        f()
        print("#"*20)
    return wrapper
@my_decorator1
@my_decorator2
def current_time():
    current_time = datetime.datetime.now()
    print(f"{current_time:%H:%M}")

current_time()

print("Task 4".center(60, "="))
class Pizza:
    def __init__(self):
        self.__ingr__ = ['pizza base', 'cheese', 'tomato sauce']

    def show_info(self):
        print(", ".join(self.__ingr__))

def add_ingredient(ingredient):
    def decorator(f):
        def wrapper(pizza):
            pizza.__ingr__.append(ingredient)
            return f(pizza)
        return wrapper
    return decorator
@add_ingredient('basil')
@add_ingredient('mozzarella')
def marherita(pizza):
    return pizza.show_info()

print("Margarita ingredients: ", end="")
pizza1 = Pizza()
marherita(pizza1)

@add_ingredient('ham')
@add_ingredient('pineapple')
def hawaiian(pizza):
    return pizza.show_info()
print("Hawaiian ingredients: ", end="")
pizza2 = Pizza()
hawaiian(pizza2)

@add_ingredient('blue cheese')
@add_ingredient('parmesan')
@add_ingredient('gorgonzola')
@add_ingredient('mozzarella')
def four_cheese(pizza):
    return pizza.show_info()
print("Four Cheese ingredients: ", end="")
pizza3 = Pizza()
four_cheese(pizza3)


@add_ingredient('ham')
@add_ingredient('mushrooms')
@add_ingredient('artichokes')
@add_ingredient('olives')
def capricciosa(pizza):
    return pizza.show_info()
print("Capricciosa ingredients: ", end="")
pizza4 = Pizza()
capricciosa(pizza4)
'''
def add_ingredient(ingredient):
    def decorator(pizza_class):
        def wrapper(*args, **kwargs):
            pizza = pizza_class(*args, **kwargs)
            pizza.__ingr__.append(ingredient)
            return pizza
        return wrapper
    return decorator


@add_ingredient('basil')
@add_ingredient('mozzarella')
class Margarita(Pizza):
    pass


@add_ingredient('ham')
@add_ingredient('pineapple')
class Hawaiian(Pizza):
    pass


@add_ingredient('blue cheese')
@add_ingredient('parmesan')
@add_ingredient('gorgonzola')
@add_ingredient('mozzarella')
class FourCheese(Pizza):
    pass


@add_ingredient('ham')
@add_ingredient('mushrooms')
@add_ingredient('artichokes')
@add_ingredient('olives')
class Capricciosa(Pizza):
    pass


margarita = Margarita()
hawaiian = Hawaiian()
four_cheese = FourCheese()
capricciosa = Capricciosa()


print("Margarita ingredients:")
margarita.show_info()
print("\nHawaiian ingredients:")
hawaiian.show_info()
print("\nFour Cheese ingredients:")
four_cheese.show_info()
print("\nCapricciosa ingredients:")
capricciosa.show_info()
'''