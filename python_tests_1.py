import random

#this function returns a random number between 1 and 100
def random_number():
   return random.randint(1, 100)

if __name__ == "__main__":
    print(f'random number :{random_number()}')
