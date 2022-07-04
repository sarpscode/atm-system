def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

usernumber = int(input())

def callcollatz(usernumber):
    collatznumber = collatz(int(usernumber))
    print(collatznumber)
    if collatznumber != 1:
        callcollatz(collatznumber)

callcollatz(usernumber)