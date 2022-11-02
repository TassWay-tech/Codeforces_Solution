def get_score(left, mid, right):
    return abs(left - mid) + abs(mid - right)

def solution(num_list: list, length: int):
    num_list.sort()
    left, mid, right = num_list[0], num_list[-1], num_list[1]

    for i in range(2, length - 1):
        if get_score(num_list[i], mid, right) < get_score(left, mid, num_list[i]):
            right = num_list[i]
        else:
            left = num_list[i]
    
    return get_score(left, mid, right)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ln = list(map(int, input().split()))
        print(solution(ln, n))