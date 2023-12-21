import random

def nimgame(n):
    # цикл, в котором по очереди в случайном порядке игроки убирают камни
    while n > 0:
        # случайным образом убирается до 3-х камней
        you = random.randint(1, min(3, n))
        n -= you
        # если камни закончились после того как вы убрали камни выводится True
        if n == 0:
            return True

        friend_move = random.randint(1, min(3, n))
        n -= friend_move
        # если камни закончились после того как друг убрал камни выводится False
        if n == 0:
            return False

print(nimgame(4))
print(nimgame(1))