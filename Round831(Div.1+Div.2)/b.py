def solution(ln: list, length: int):
    max_height = 0
    total_width = 0

    for item in ln:
        if item[1] > item[0]:
            item = item[1], item[0]

        if item[0] > max_height:
            max_height = item[0]
        total_width += item[1]
    
    return 2 * (max_height + total_width);

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        ln = [tuple(map(int, input().split())) for x in range(n)]
        print(solution(ln, n))