import heapq
import sys

def solution(row, col, target, order):
    max_heap = []
    limit = row * col - 2

    for element in order:
        # Max Heap에 원소를 넣는다.
        heapq.heappush(max_heap, (-element, element))

        # Heap에 원소가 가득차서 더 이상 진행할 수 없다면 답은 없다.
        if len(max_heap) == limit:
            break
        
        # Heap에서 가장 큰 원소가 제거 가능한지 확인
        while len(max_heap) != 0 and max_heap[0][1] == target:
            target -= 1
            heapq.heappop(max_heap)

    if len(max_heap) != 0:
        return "TIDAK"
    else:
        return "YA"

if __name__ == '__main__':
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        n, m, k = tuple(map(int, input().split()))
        order = list(map(int, input().split()))
        print(solution(n, m, k, order))
