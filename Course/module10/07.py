# iterators and next
from random import randint

class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)

if __name__ == '__main__':
    my_random_list = RandIterator(1, 20, 5)

    for rn in my_random_list:
        print(rn, end=' ')


#  generator
from random import randint

def rand_generator(start, end, quantity):
    count = 0
    while count < quantity:
        yield randint(start, end)
        count += 1

if __name__ == '__main__':
    for rn in rand_generator(1, 20, 5):
        print(rn, end=' ')
