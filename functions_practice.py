
def hello():
    print("Hello!")

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(foods):
    if len(foods) == 0:
        print('My lunchbox is empty!')
        return

    print(f'First I eat {foods[0]}')

    for food in foods[1:]:
        print(f'Next I eat {food}')

print('TESTING hello() FUNCTION:')
hello()

print('TESTING pack() FUNCTION:')
print(pack(1, 2, 3))

print('TESTING eat_lunch() FUNCTION WITH EMPTY LIST:')
foods = []
eat_lunch(foods)

print('TESTING eat_lunch() FUNCTION WITH LIST OF LENGTH 1:')
foods = ['fruit']
eat_lunch(foods)

print('TESTING eat_lunch() FUNCTION WITH LIST OF LENGTH 3:')
foods = ['fruit', 'sandwiches', 'chocolate']
eat_lunch(foods)
