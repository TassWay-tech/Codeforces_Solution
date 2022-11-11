def get_score(one, two, three):
    return abs(one - two) + abs(two - three)

def solution(num_list: list, length: int):
    num_list.sort()
    high = 0
    
    for i in range(length - 2):
        value = num_list[i + 1] - num_list[i] + num_list[-1] - num_list[i]
        if value > high:
            high = value

    for i in range(1, length - 1):
        value = num_list[i + 1] - num_list[i] + num_list[i + 1] - num_list[0]
        if value > high:
            high = value
    
    return high

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ln = list(map(int, input().split()))
        print(solution(ln, n))
