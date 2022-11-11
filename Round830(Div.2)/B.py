import sys
input = sys.stdin.readline

def solution(n: int):
    print((n >> 1) + (n & 1))
    left, right = 1, 3 * n
    while left < right:
        print(left, right)
        left += 3
        right -= 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        solution(n)