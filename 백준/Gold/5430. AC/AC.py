# 테스트 케이스 개수 T
# 함수 p 가 RDD 인 경우 R 뒤집고 D 첫번째 수 버리기 두번
# 배열이 비어있는데 D를 사용하면 에러가 발생
from collections import deque
import sys

input = sys.stdin.readline  # 빠른 입력

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr_str = input().strip()
    
    # 빈 배열 처리
    if n == 0:
        arr = deque()
    else:
        arr = deque(map(int, arr_str[1:-1].split(",")))
    
    reversed_flag = False
    error_flag = False

    for cmd in p:
        if cmd == "R":
            reversed_flag = not reversed_flag
        elif cmd == "D":
            if not arr:
                print("error")
                error_flag = True
                break
            if reversed_flag:
                arr.pop()
            else:
                arr.popleft()

    if not error_flag:
        if reversed_flag:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")
