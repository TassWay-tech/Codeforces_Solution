from math import sqrt
def is_prime(num: int):
    if num <= 1:
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

def solution(n: int):
    i = 2
    while True:
        if is_prime(i + n):
            pass
        else:
            return i
        i += 1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        x = int(input())
        print(solution(x))
    # print(is_prime(24))