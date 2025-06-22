# Python 코딩 테스트 완벽 가이드

이 문서는 **파이썬**으로 코딩 테스트를 준비하는 데 필요한 **핵심 개념**, **자료구조**, **다양한 알고리즘 유형**, 그리고 **유용한 라이브러리 사용법**을 총정리합니다. 이 가이드가 여러분의 코딩 테스트 준비에 큰 도움이 되기를 바랍니다.

---

## 1. 기본 문법 및 입출력

코딩 테스트에서 가장 기본이 되는 입출력 및 파이썬의 핵심 문법입니다.

### 1.1. 입출력 (Input/Output)

빠른 입출력을 위해 `sys` 모듈을 사용하는 방법을 포함하여, 다양한 입력 방식을 알아봅니다.

```python
import sys

# 한 줄 입력 (문자열)
s = sys.stdin.readline().rstrip() # 개행 문자 제거
# 정수 입력
n = int(sys.stdin.readline())
# 실수 입력
f = float(sys.stdin.readline())

# 여러 정수 입력 (공백으로 구분)
a, b = map(int, sys.stdin.readline().split())

# 리스트로 여러 정수 입력
numbers = list(map(int, sys.stdin.readline().split()))

# 여러 줄 입력 (예: N줄의 입력)
# for _ in range(N):
#     line = sys.stdin.readline().rstrip()
#     # 처리 로직

# 출력
print("Hello, Python!")
print(f"결과: {a}, {b}") # f-string 활용
```

### 1.2. 자료형 (Data Types) 및 기본 연산

파이썬의 주요 **자료형**과 기본적인 **연산자**를 알아봅니다.

- **정수 (`int`)**: `10`, `-5`
- **실수 (`float`)**: `3.14`, `-0.5`
- **문자열 (`str`)**: `"hello"`, `'world'`, **슬라이싱** (`s[start:end:step]`)
- **리스트 (`list`)**: `[1, 2, 3]`, `['a', 'b']` (가변, 순서 O, 중복 O)
- **튜플 (`tuple`)**: `(1, 2)`, `('x', 'y')` (**불변**, 순서 O, 중복 O)
- **딕셔너리 (`dict`)**: `{'name': 'Alice', 'age': 30}` (키-값 쌍, 키는 고유)
- **집합 (`set`)**: `{1, 2, 3}`, `{'a', 'b'}` (중복 X, 순서 X)
- **불리언 (`bool`)**: `True`, `False`

<!-- end list -->

```python
# 문자열 슬라이싱 및 메서드
s = "Python Programming"
print(s[7:18]) # Programming
print(s.upper()) # PYTHON PROGRAMMING
print(s.count('g')) # 2

# 리스트 컴프리헨션
squares = [i*i for i in range(5)]
print(squares) # [0, 1, 4, 9, 16]

# 딕셔너리 활용
my_dict = {'apple': 1000, 'banana': 1500}
my_dict['orange'] = 2000 # 추가
print(my_dict.get('grape', 0)) # 'grape' 키가 없으면 0 반환
```

---

## 2\. 핵심 자료구조 (Data Structures)

코딩 테스트에서 효율적인 문제 해결을 위해 필수적인 자료구조들을 이해하고 활용하는 방법을 익힙니다.

### 2.1. 리스트 (List)

가장 유연하고 많이 사용되는 파이썬의 **동적 배열**입니다.

- **주요 메서드**: `append()`, `insert()`, `pop()`, `remove()`, `sort()`, `reverse()`, `count()`, `index()`.
- **정렬**: `list.sort()` (제자리 정렬), `sorted(iterable)` (새로운 정렬된 리스트 반환).
  - **`key` 매개변수**: 복잡한 기준으로 정렬할 때 `lambda` 함수와 함께 사용됩니다.

```python
# 리스트 정렬 예제
data = [("apple", 10), ("banana", 5), ("orange", 15)]
data.sort(key=lambda x: x[1]) # 두 번째 원소(값) 기준으로 오름차순 정렬
print(data) # [('banana', 5), ('apple', 10), ('orange', 15)]

# 리스트 슬라이싱
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:7])    # [3, 4, 5, 6, 7]
print(numbers[::2])    # [1, 3, 5, 7, 9] (2칸 간격)
print(numbers[::-1])   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (역순)
```

### 2.2. 딕셔너리 (Dictionary)

**키(key)**-**값(value)** 쌍으로 이루어진 **해시 테이블** 기반 자료구조입니다. 빠른 탐색(평균 $O(1)$)이 가능합니다.

- **주요 메서드**: `keys()`, `values()`, `items()`, `get()`, `pop()`, `update()`.

```python
student_scores = {'Alice': 90, 'Bob': 85, 'Charlie': 92}

# 키-값 쌍 순회
for name, score in student_scores.items():
    print(f"{name}: {score}")
```

### 2.3. 집합 (Set)

**중복을 허용하지 않고**, **순서가 없는** 자료구조입니다. 교집합, 합집합, 차집합 등의 **집합 연산**에 유용합니다.

- **주요 메서드**: `add()`, `remove()`, `union()`, `intersection()`, `difference()`.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2) # 합집합: {1, 2, 3, 4, 5, 6}
print(set1 & set2) # 교집합: {3, 4}
print(set1 - set2) # 차집합: {1, 2}
```

---

## 3\. 알고리즘 유형별 정리 (Algorithm Types)

코딩 테스트에서 자주 등장하는 다양한 알고리즘 유형을 자세히 알아보고, 각 유형별 핵심 개념과 예시를 살펴봅니다.

---

### 3.1. 구현 (Implementation)

주어진 문제의 요구사항을 정확하고 빠르게 코드로 옮기는 능력입니다. 특별한 고차원 알고리즘 없이 조건문, 반복문, 문자열/리스트 처리 등을 통해 해결하는 문제입니다.

- **핵심**: 문제 이해력, 조건 분기 처리, 문자열/리스트/배열 조작 능력, 예외 및 **엣지 케이스** 고려.
- **주의사항**: 시간/메모리 제한, 정확한 입출력 형식 준수.

<!-- end list -->

```python
# 예제: 문자열 압축 (카카오 기출 유사)
def solution(s):
    length = len(s)
    min_compressed_len = length # 압축이 안 될 경우 원래 길이

    for unit in range(1, length // 2 + 1): # 압축 단위 (1부터 길이의 절반까지)
        compressed = ""
        prev_word = s[0:unit]
        count = 1

        for i in range(unit, length, unit):
            current_word = s[i:i+unit]
            if prev_word == current_word:
                count += 1
            else:
                compressed += (str(count) if count >= 2 else "") + prev_word
                prev_word = current_word
                count = 1
        # 마지막 남은 부분 처리
        compressed += (str(count) if count >= 2 else "") + prev_word
        min_compressed_len = min(min_compressed_len, len(compressed))

    return min_compressed_len

print(solution("aabbaccc")) # 7 (2a2ba3c)
print(solution("ababcdcdababcdcd")) # 9 (2ababcdcd)
print(solution("abcabcabcabcdededededede")) # 17 (2abcabc2dedededede)
print(solution("xababcdcdababcdcd")) # 17
```

---

### 3.2. 정렬 (Sorting)

데이터를 특정 기준에 따라 재배열하는 알고리즘입니다. 파이썬은 강력한 내장 정렬 함수를 제공합니다.

- **핵심**: `list.sort()`, `sorted()`, `key` 매개변수를 활용한 **커스텀 정렬**.
- **시간 복잡도**: 내장 정렬 (Timsort)은 평균 $O(N \\log N)$ 입니다.

```python
# 예제: 튜플 리스트 다중 조건 정렬
# (첫 번째 원소 오름차순, 첫 번째 원소가 같으면 두 번째 원소 내림차순)

points = [(1, 5), (2, 3), (1, 8), (3, 2), (2, 1)]
points.sort(key=lambda x: (x[0], -x[1])) # x[0] 오름차순, x[1] 내림차순 (음수 부호)
print(points) # [(1, 8), (1, 5), (2, 3), (2, 1), (3, 2)]
```

---

### 3.3. 이진 탐색 (Binary Search)

**정렬된 배열**에서 특정 값을 효율적으로 찾는 알고리즘입니다. 탐색 범위를 절반씩 줄여나가므로 시간 복잡도는 $O(\\log N)$입니다.

- **핵심**: 항상 **정렬된 데이터**에만 적용 가능. `bisect` 모듈 활용.
- **활용**: 특정 값 찾기, '최소/최대 \~한 값' 찾기 (**파라메트릭 서치**), 특정 범위 내 원소 개수 세기.

<!-- end list -->

```python
import bisect

# 예제: 특정 범위 내 원소 개수 구하기
def count_elements_in_range(arr, left_val, right_val):
    left_idx = bisect.bisect_left(arr, left_val)
    right_idx = bisect.bisect_right(arr, right_val)
    return right_idx - left_idx

data = [1, 2, 3, 3, 3, 3, 4, 5, 6, 7]
print(f"값이 3인 원소 개수: {count_elements_in_range(data, 3, 3)}") # 4
print(f"값이 2 이상 5 이하인 원소 개수: {count_elements_in_range(data, 2, 5)}") # 7
```

---

### 3.4. 너비 우선 탐색 (BFS, Breadth-First Search)

그래프나 트리에서 **시작 노드로부터 가까운 노드부터 차례로** 탐색하는 알고리즘입니다. 주로 **최단 거리**를 구할 때 사용됩니다. **큐(Queue)** 자료구조를 활용합니다.

- **핵심**: `collections.deque` 활용, `visited` 배열로 방문 여부 및 거리 체크.

```python
from collections import deque

# 예제: 최소 이동 횟수 (BFS) - N*M 미로 탈출
# 0은 이동 가능, 1은 벽. (0,0)에서 (N-1, M-1)까지 최소 이동 칸 수
def bfs_min_moves(graph, start_r, start_c, end_r, end_c):
    rows, cols = len(graph), len(graph[0])
    # 상, 하, 좌, 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque([(start_r, start_c)])
    # 방문 여부 및 시작점으로부터의 거리 저장
    dist = [[-1] * cols for _ in range(rows)]
    dist[start_r][start_c] = 1 # 시작점 거리 1

    while queue:
        r, c = queue.popleft()

        if r == end_r and c == end_c: # 목표 지점 도달
            return dist[r][c]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 맵 범위 내에 있고, 벽이 아니며, 아직 방문하지 않은 곳
            if 0 <= nr < rows and 0 <= nc < cols and graph[nr][nc] == 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    return -1 # 목표 지점에 도달할 수 없는 경우

maze_map = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
print(f"미로 최소 이동 칸 수: {bfs_min_moves(maze_map, 0, 0, 4, 4)}") # (0,0)에서 (4,4)까지
```

---

### 3.5. 깊이 우선 탐색 (DFS, Depth-First Search)

그래프나 트리에서 한 방향으로 최대한 **깊이 탐색**하다가 더 이상 갈 곳이 없으면 되돌아와 다른 방향으로 탐색하는 알고리즘입니다. **스택(Stack)** 또는 \*\*재귀(Recursion)\*\*를 사용합니다.

- **핵심**: 스택 또는 재귀, `visited` 배열로 방문 여부 체크.
- **활용**: 모든 경로 탐색, 사이클 찾기, 연결 요소 찾기.

```python
# 예제: 연결된 아이스크림 개수 세기 (DFS)
# N*M 얼음 틀에서 0은 구멍, 1은 막힌 칸. 연결된 0들의 덩어리 개수 세기 (재귀)

N, M = 4, 5
ice_frame = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0]
]

visited = [[False] * M for _ in range(N)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs_ice(r, c):
    visited[r][c] = True # 현재 위치 방문 처리
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        # 맵 범위 내에 있고, 얼음(0)이며, 아직 방문하지 않은 곳
        if 0 <= nr < N and 0 <= nc < M and ice_frame[nr][nc] == 0 and not visited[nr][nc]:
            dfs_ice(nr, nc) # 재귀적으로 탐색

ice_cream_count = 0
for i in range(N):
    for j in range(M):
        if ice_frame[i][j] == 0 and not visited[i][j]:
            dfs_ice(i, j) # 새로운 아이스크림 덩어리 발견 및 탐색
            ice_cream_count += 1

print(f"아이스크림 개수: {ice_cream_count}") # 3
```

---

### 3.6. 그리디 (Greedy)

현재 상황에서 **가장 최적의 선택**을 하는 알고리즘입니다. "지금 당장 최선"의 선택이 전체적인 최적해로 이어지는 경우에만 사용 가능합니다.

- **핵심**: 탐욕적인 선택이 항상 최적해를 보장하는지 **증명**할 수 있어야 합니다.

<!-- end list -->

```python
# 예제: 큰 수의 법칙
# N개의 숫자로 이루어진 배열에서 M번 더하여 가장 큰 수를 만드는데,
# 특정 숫자를 K번까지만 연속해서 더할 수 있을 때 최댓값 구하기

N, M, K = 5, 8, 3 # 배열 크기, 더하는 횟수, 연속 허용 횟수
data = [2, 4, 5, 4, 6]

data.sort(reverse=True) # 내림차순 정렬
first = data[0] # 가장 큰 수
second = data[1] # 두 번째로 큰 수

result = 0
count = 0 # 연속 더한 횟수

for _ in range(M):
    if count < K:
        result += first
        count += 1
    else:
        result += second
        count = 0 # 연속 횟수 초기화
print(f"큰 수의 법칙 결과: {result}") # 46 (6+6+6+5+6+6+6+5)

# 더 효율적인 풀이 (수학적 접근)
# (K번 반복 + 1번 다른 수) 패턴이 몇 번 반복되는지 계산
count_first = (M // (K + 1)) * K + (M % (K + 1))
count_second = M - count_first
result_optimized = first * count_first + second * count_second
print(f"최적화된 큰 수의 법칙 결과: {result_optimized}")
```

---

### 3.7. 동적 계획법 (Dynamic Programming, DP)

큰 문제를 작은 문제로 나누어 해결하고, 작은 문제의 결과를 \*\*저장(메모이제이션)\*\*하여 재활용하는 기법입니다. 중복 계산을 피하여 효율성을 높입니다.

- **핵심**: **점화식** 찾기, **메모이제이션(하향식)** 또는 **테이블 채우기(상향식)**.
- **활용**: 피보나치 수열, 최장 공통 부분 수열, 배낭 문제, 경로의 수 등.

```python
# 예제: 1로 만들기 (DP)
# 정수 X가 주어졌을 때, 5로 나누거나, 3으로 나누거나, 2로 나누거나, 1을 빼는 연산을 통해
# 1을 만드는 최소 연산 횟수

X = 26
# DP 테이블 초기화 (dp[i]는 i를 1로 만드는 최소 연산 횟수)
dp = [0] * (X + 1)

for i in range(2, X + 1):
    dp[i] = dp[i-1] + 1 # 1을 빼는 경우

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(f"{X}를 1로 만드는 최소 연산 횟수: {dp[X]}") # 26 -> 25 -> 5 -> 1 (3회)
```

---

### 3.8. 그래프 이론 (Graph Theory)

\*\*정점(node)\*\*과 \*\*간선(edge)\*\*으로 이루어진 자료구조를 다루는 분야입니다. 최단 경로, 최소 신장 트리, 위상 정렬 등 다양한 알고리즘이 있습니다.

- **핵심**: **인접 리스트** 또는 **인접 행렬**로 그래프 표현. BFS/DFS 기반 탐색, 다익스트라, 플로이드-워셜, 크루스칼/프림.

```python
import heapq

# 예제: 다익스트라 최단 경로 (우선순위 큐 활용)
# 하나의 시작 노드로부터 다른 모든 노드까지의 최단 거리
INF = int(1e9) # 무한대 값

def dijkstra(n_nodes, graph_adj, start_node):
    distances = [INF] * (n_nodes + 1) # 최단 거리 테이블
    pq = [] # 우선순위 큐 (거리, 노드)

    heapq.heappush(pq, (0, start_node)) # (시작 노드까지 거리 0)
    distances[start_node] = 0

    while pq:
        dist, current_node = heapq.heappop(pq)

        # 이미 처리된 노드 (더 짧은 경로가 발견됨)
        if distances[current_node] < dist:
            continue

        # 현재 노드와 연결된 인접 노드들을 확인
        for neighbor, weight in graph_adj[current_node]:
            cost = dist + weight
            if cost < distances[neighbor]:
                distances[neighbor] = cost
                heapq.heappush(pq, (cost, neighbor))
    return distances

# 그래프 예시 (인접 리스트): {노드: [(인접 노드, 가중치), ...]}
# 6개의 노드, 11개의 간선
n_nodes = 6
graph_adj = [[] for _ in range(n_nodes + 1)]
edges = [
    (1, 2, 2), (1, 3, 5), (1, 4, 1),
    (2, 3, 3), (2, 4, 2),
    (3, 2, 3), (3, 6, 5),
    (4, 3, 3), (4, 5, 1), (4, 6, 5),
    (5, 6, 2)
]
for u, v, w in edges:
    graph_adj[u].append((v, w))

start_node = 1
result_distances = dijkstra(n_nodes, graph_adj, start_node)

print(f"시작 노드 {start_node}로부터의 최단 거리:")
for i in range(1, n_nodes + 1):
    if result_distances[i] == INF:
        print(f"  {i}번 노드: 도달할 수 없음")
    else:
        print(f"  {i}번 노드: {result_distances[i]}")
```

---

## 4\. 유용한 라이브러리 (Useful Libraries)

파이썬의 풍부한 라이브러리는 코딩 테스트에서 시간을 절약하고 효율적인 코드를 작성하는 데 큰 도움이 됩니다.

### 4.1. `collections`

자료구조를 보강하는 모듈입니다.

- **`deque` (데크)**: 양방향 큐. `appendleft()`, `popleft()` 등을 통해 큐와 스택의 기능을 모두 수행하며, BFS 구현에 필수적입니다.
- **`Counter`**: iterable의 해시 가능한 객체 수를 세는 데 사용됩니다.
- **`defaultdict`**: 존재하지 않는 키에 접근 시 기본값을 자동으로 생성하는 딕셔너리입니다.

```python
from collections import deque, Counter, defaultdict

# deque 활용 예시
q = deque([1, 2, 3])
q.appendleft(0) # deque([0, 1, 2, 3])
print(q.pop())      # 3 (오른쪽에서 제거)
print(q.popleft())  # 0 (왼쪽에서 제거)
print(q) # deque([1, 2])

# Counter 활용 예시
text = "hello world"
counts = Counter(text)
print(counts) # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# defaultdict 활용 예시
d = defaultdict(int) # int는 기본값 0을 의미
d['apple'] += 1
d['banana'] += 2
print(d) # defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})
```

### 4.2. `heapq`

**힙(Heap)** 자료구조를 제공합니다. \*\*우선순위 큐(Priority Queue)\*\*를 구현할 때 사용되며, 항상 가장 작은 요소가 루트에 오는 **최소 힙**입니다. (최대 힙은 원소에 -를 붙여 저장하고 꺼낼 때 다시 -를 붙여 사용)

```python
import heapq

min_heap = []
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 3)

print(f"힙: {min_heap}") # 내부적으로 힙 속성을 유지하며 정렬된 것처럼 보이지 않을 수 있음

print(f"가장 작은 값: {heapq.heappop(min_heap)}") # 1
print(f"다음 작은 값: {heapq.heappop(min_heap)}") # 3
```

### 4.3. `itertools`

반복자(iterator)를 생성하는 함수들을 제공하여 효율적인 반복 처리를 돕습니다. **순열**, **조합** 등을 구할 때 유용합니다.

- **`permutations(iterable, r)`**: r 길이의 순열 (순서 O, 중복 X)
- **`combinations(iterable, r)`**: r 길이의 조합 (순서 X, 중복 X)
- **`product(iterable, repeat)`**: 중복 순열 (순서 O, 중복 O)

<!-- end list -->

```python
from itertools import permutations, combinations, product

items = ['A', 'B', 'C']

print(f"순열 (2개): {list(permutations(items, 2))}")
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

print(f"조합 (2개): {list(combinations(items, 2))}")
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

print(f"중복 순열 (2개): {list(product(items, repeat=2))}")
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
```

### 4.4. `math`

수학 관련 함수들을 제공합니다.

- `sqrt()`, `ceil()`, `floor()`, `factorial()`, `gcd()`, `lcm()` (Python 3.9 이상).

```python
import math

print(f"16의 제곱근: {math.sqrt(16)}")     # 4.0
print(f"3.14 올림: {math.ceil(3.14)}")    # 4
print(f"3.99 내림: {math.floor(3.99)}")   # 3
print(f"12와 18의 최대공약수: {math.gcd(12, 18)}") # 6
# print(f"12와 18의 최소공배수: {math.lcm(12, 18)}") # 36 (Python 3.9 이상)
```

---

## 5\. 코딩 테스트 실전 팁 (Coding Test Tips)

성공적인 코딩 테스트를 위한 추가적인 조언들입니다.

- **시간/공간 복잡도 분석**: 작성한 코드가 제한 시간 및 메모리 내에 동작하는지 항상 분석하고 예측하세요.
- **제한 사항 확인**: 문제의 입력 값 범위, 시간/메모리 제한 등을 꼼꼼히 확인하고, 이에 맞춰 자료구조나 알고리즘을 선택해야 합니다.
- **엣지 케이스 고려**: 문제의 일반적인 경우뿐만 아니라, 가장자리 값 (0, 음수, 최대값, 빈 리스트/문자열 등)에 대해서도 코드가 올바르게 동작하는지 확인하세요.
- **테스트 케이스 직접 작성**: 예제 외에 다양한 상황을 가정한 테스트 케이스를 직접 만들어 검증하는 습관을 들이세요.
- **디버깅 연습**: `print()` 문을 활용한 디버깅에 익숙해지세요. 중간 값을 출력해보면서 로직의 흐름을 파악하는 것이 중요합니다.
- **클린 코드**: 가독성 좋고 유지보수하기 쉬운 코드를 작성하는 연습을 하세요. 의미 있는 변수명, 함수명, 적절한 주석 등을 활용합니다.
- **주석 활용**: 복잡한 로직이나 중요한 부분에는 주석을 달아 코드의 이해를 돕습니다. 특히 알고리즘 설명이나 시간 복잡도 등을 명시하는 것이 좋습니다.
- **문제 유형 파악**: 문제가 요구하는 것이 단순히 구현인지, DP, 그리디, 그래프 (BFS/DFS), 이진 탐색 등 특정 알고리즘 유형을 요구하는지 빠르게 파악하는 것이 중요합니다.

```

```
