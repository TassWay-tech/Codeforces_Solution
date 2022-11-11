import sys
input = sys.stdin.readline

def solution(items: list, n: int):
    s1, s2 = (0, 0)
    for item in items:
        if item < 0:
            s2 += item
        else:
            s1 += item
    
    s1, s2 = abs(s1), abs(s2)
    return abs(s1 - s2)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        items = list(map(int, input().split()))
        print(solution(items, n))