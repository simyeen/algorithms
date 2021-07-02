# 1. 자료형

- 정수형 : 가장 기본의 자료형.
- 실수형 : 소수점이 있을지 자동으로 실수로 된다

    ex) 5. , -.7, 150.2  등등..

```python
a = 0.3 + 0.6
print(a) # 0.89999999999999

if a == 0.9:
	print(True)
else :
	print(False) # 이게 출력됨.
```

현대 컴퓨터는 실수 정보를 표현하는 정확도에 한계를 가지므로, 이럴 경우

**round()함수를 사용해야 한다.**

round함수는 첫 번째 인자는 실수형 데이터, 두 번째 인자는 반올림 하고자 하는 위치 -1이다.

그러므로 위에서 round(a, 4)를 하게 된다면 소수점 3자리에서 반올림을 해 우리가 얻고자하는 0.9를 얻는다.

# 자료형의 연산

- **/ 연산의 경우 기본적으로 실수형으로 되므로 몫을 얻고 싶다면 // 연산자를 써야한다.**
- n //= k 같은 형태로 몫을 얻어서 사용하자 (정수형이 default)
- 나머지를 얻고 싶다면 %를 사용하자.

---

# ** 리스트 자료형

### 리스트 만들기

- 리스트 만들기 대괄호 [] 안에 원소를 넣어 초기화 하고, 쉼표로 원소를 구분.

    ex) a = [1, 2, 3, 4],  a = list(),  a = []로 선언한다.

### 리스트의 인덱싱과 슬라이싱

- 인덱싱 : 인덱스값을 입력해 리스트의 특정한 원소에 접근 하는 것.

    인덱싱을 할 때 음수로 접근하면 뒤에서 부터 접근한다.

```python
a = [1,2,3,4,5,6,7]
a[-1] => 7
a[-3] => 5
a[3] => 4

# 이때 : 을 이용해서 원하는 만큼의 리스트만 발췌할 수 있다.
a[1:4] => [2,3,4]
```

### 리스트 컴프리헨션(리스트 초기화 하는 방법 중 하나)

```python
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트이다.
array = [i for i in range(20) if i % 2 == 1]

# 1부터 9까지의 수의 제곱 값으로 초기화하기.
array = [i*i for i in rage(1, 10)]

# *중요* 2차원 리스트를 초기화할 때 매우 유용하다,
n = 3(행)
m = 4(열)
array = [[0]* m for i in range(n)] 
=> [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
```

- for _ in range(n) 에서 _의 역할 :

    반복을 수행하되 반복을 위한 변수 값을 무시하고자 할 때는 언더바(_)를 사용한다.

- ** N x M 크기의 2차원 리스트 초기화 시에는 반드시 리스트 컴프리헨션을 이용해야한다

```python
n = 3
m = 4
array = [[0]* m] * n 
# 위에 처럼 2차원 배열을 초기화 하면 안된다!!

array[1][1] = 5
=> [[0,5,0,0],[0,5,0,0],[0,5,0,0]]

# array[1][1]를 하나만 바꿨을 뿐인데 3개의 리스트에서 인덱스 1인 원소들이 모두 바뀌었다.
# why? 내부적으로 포함된 3개의 리스트가 모두 동일한 객체 대한 3개의 레퍼런스로 인식되기 때문.
# 그래서 특정한 크기를 가지는 2차원리스트를 초기화할 때에는 리스트 컴프리헨션을 이용하자!
```

[리스트 관련 메서드](https://www.notion.so/910cfe0c768340d28d1b314d62c91136)

append함수는 O(1)인 것에 비해 insert와 remove는 O(N)이므로 신중히 사용해야한다!!

이때 **특정한 값의 원소를 모두 제거**하려면 리스트 컴프리헨션을 사용하는 것이 좋다.

```python
array = [1,2,3,4,5,5,5]
remove_set = {3,5}

#remove_set에 포함되지 않은 값만을 저장하자.
result = [i for i in array if i not in remove_set]
=> [1,2,4]를 가진다.
```

---

# 문자열 자료형

- 문자열 내에서 "나 '를 사용하기 위해선 앞에 \를 붙여야 한다.
- 문자열 끼리 더할때 + 연산과, 문자열 * 3(상수) 등의 연산이 가능하다.
- 문자열 슬라이싱도 가능하다. a = 'ABCDEF' 에서 a[2:4]는 CD를 의미한다.

---

# ** 튜플 자료형

### 튜플과 리스트의 차이점 :

- 튜플은 한 번 선언된 값을 변경할 수 없다.
- 리스트는 []를 이용하지만 튜플은 ()를 이용한다.

```python
a = (1,2,3,4)
print(a)

a[2] = 7 
=> TypeError : 'tuple' object does not support item assignment의 오류가 발생한다.
```

### 튜플을 사용하는 이유:

- 리스트에 비해 상대적으로 공간 효율적이다.
- 변경해서는 안 되는 값을 보존하다.
- 각 원소의 성질 서로 다를 때 주로 사용한다

    ex) 그래프에서 '비용', '노드 번호'라는 서로 다른 성질의 데이터를 (비용, 노드 번호)라는 형태의 튜플로 묶어서 사용한다.

---

# ** 사전 자료형

- 사전 자료형은 key와 value를 쌍으로 가지는 자료형이다.
- random access가 가능하다.
- dictionary자료형은 해쉬 테이블을 이용해 기본적으로 데이터의 검색 및 수정을

    O(1)의 시간에 처리 할 수 있다.

```python
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

=> {'사과' : 'Apple', '바나나' : 'Banana', '코코넛' : 'Coconut'}

if '사과' in data :
	print('사과'를 키로 가지는 데이터가 존재합니다.)
# dict뿐 아니라 리스트와 튜플에서도 사용해보자
# 단, 사전자료형은 해쉬 테이블이기때문에 더 효율적일 것이다.
```

### 사전 자료형 관련 함수

- 위의 data dict를 사용할 시
- key_list = **data.keys()**
- values_list = **data.values()**
- print(key_list) ⇒ dict_keys(['사과', '바나나', '코코넛'])
- print(values_list) = dict_values(['Apple', 'Banana', 'Coconut'])

- 활용법

    ```python

    # 각 키에 따른 값을 하나씩 출력한다.
    for key in key_list : 
    	print(data[key]) 
    => Apple
    	 Banana
    	 Coconut
    ```

---

# 집합 자료형

- 집합 자료형의 특징
    1. 중복을 허용하지 않는다. ⇒ set함수를 통해 list에서 중복을 제거 할 수 있다.
    2. 순서가 없다. ⇒ 인덱싱으로 접근이 불가능 하다.

### 집합 자료형 초기화

```python
data = set([1,1,2,3,4,4,5])
print(data)
=> {1,2,3,4,5} # 집합은 중복을 허용하지 않으므로 중복값은 모두 제거된다.

data = {1,1,2,3,4,4,5}
print(data)
=> {1,2,3,4,5} # 집합은 {}를 사용해 초기화 할 수 있다.
```

### 집합 자료형의 연산

- 합집합, 교집합, 차집합이 존재한다.

```python
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a | b) # 합집합 {1,2,3,4,5,6,7}
print(a & b) # 교집합 {3,4,5}
print(a - b) # 차집합 {1,2}
```

### 집합 자료형 관련 함수

```python
data = set([1,2,3])

# 새로운 원스 추가
data.add(4) => {1,2,3,4}

# 새로운 원소 여러 개 추가
data.updata([5,6]) => {1,2,3,4,5,6}

# 특정한 값을 갖는 원소 삭제
data.remove(3)=> {1,2,4,5,6}
```

이때 add()와 remove() 함수는 O(1)의 시간 복잡도를 가져서 매우 효율적이다!

---

# 2. 조건문

- in 연산자와 not in 연산자를 사용해보자.
- pass 문

```python
score = 85

if score >= 80:
	pass # 나중에 작성할 소스코드이다.
else :
	print('성적이 80점 미만입니다.')
```

```python
score = 85 
result = 'Scuccess' if score >= 80 else 'Fail'
# 이렇게 ? 연산자처럼 조건부 표현식으로 대입문도 가능하다.
```

---

# 3. 반복문

1. whlie문 (생략)
2. for문 

```python
for 변수 in 리스트 :
	실행할 소스코드

# in뒤에 오는 데이터로는 리스트, 튜플, 문자열 등이 사용될 수 있다.

for i in range(1, 10):
	result += i

#range(시작 값, 끝 값 +1)의 형태로 쓰인다.
# 만약 range()의 값으로 하나의 값만 넣으면 시작 값은 자동으로 0이 된다.
```

---

# 4. 함수

```python

def 함수명(매개변수):
	실행할 소스코드
	return 반환 값 
```

```python
def add(a, b):
	print('함수의 결과:', a+b)

add(b=3, a=7
```

```python
def add(a, b):
	print('함수의 결과:', a+b)

add(3,7) => 10
```

```python
def add(a, b):
	print('함수의 결과:', a+b)

add(b=3, a=7)
# 함수를 호출하는 과정에서 파라미터의 변수를 직접 지정해서 값을 넣을 수 있다.
# 이때 매개변수의 순서가 달라도 상관없다.
# 즉, 함수안에 a-b가 있었다면 -6(= 3-7)가 아닌 4(7-3)가 나온다. 
```

- 람다표현식 : 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다.

```python
def add(a, b):
	return a+b
print(add(3,7)) # 이 함수를 

print((lambda a, b: a+b)(3, 7))
```

- 전역변수를 사용하기 위해선 선언은 블락 밖에서 하고 함수 내부에서 global 선언을 해주자.

---

# 5. ***입출력

## 입력

- 여러 개의 데이터를 공백으로 구분해서 입력받을 때

```python
data = list(map(int, input().split())
n, m, k = map(int, input().split())
```

1. input() 문자열 한 줄을 입력받는다.
2. split() 공백으로 문자열을 나눠준다.
3. map() 모든 원소에 int()를 적용 시켜준다.
4. list()로 적용된 원소들을 하나의 리스트로 바꿔준다.

- 줄 바꿈으로 입력받을 때 → int(input())을 여러번 써주자.
- 입력의 개수가 많을 때는 sys 라이브러리를 쓰자

```python
import sys
sys.stdin.readline().rstrip()

# input() = sys.stdin.readline()
# rstrip()을 해주는 이유는 readline()으로 입력하면 입력 후 엔터가 줄바꿈 기호로 입력된다.
# 그래서 이 공백 문자를 제거하는 rstrip()함수를 꼭 써주자.
```

## 출력

- 문자열 사이에 변수를 출력하고 싶을 때

```python
answer = 7
print("정답은 " + answer + "입니다.")

# TypeError : can only concatenate str (not "int") to str
# 문자열 자료형끼리만 더하기 연산이 가능해서 오류가 발생한다.

### 해결방법 3가지 존재

#1
answer = 7
print("정답은 " + str(answer) + "입니다.")
# 변수를 문자열로 변환해서 출력한다.

#2
answer = 7
print("정답은 ", str(answer), "입니다.")
# 각 변수를 콤마로 구분해서 출력한다 -> 의도치 않은 공백삽입에 주의해서 사용할 것.

#3
answer = 7
print(f"정답은 {answer}입니다.")
# Js의 백틱 template처럼 사용하자!
```

---

# 6. 주요 라이브러리의 문법과 유의점

### 내장함수

- input(), print()
- sum()
- min, max
- eval : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환하다.

    ```python
    result = eval("(3+5)*7")
    print(result)
    ```

- sorted()

    ```python
    #튜플의 경우 key 속성을 이용해 정렬 기준을 명시할 수 있다.
    result = sorted([('홍길동',35),('이순신',75),('이무개',50)] key = lambda x : x[1], 
    reverse = True)
    => [('이순신',75),('이무개',50),('홍길동',35)]이 된다.
    ```

### itertools : 파이썬에서 반복되는 데이터를 처리하는 기능을 포함한 라이브러리

- parmutions 순열
- combinations 조합
- product 중복순열
- combinations_with_replacement 중복조합

```python
data = ['A', 'B', 'C'] # 이 배열을 사용할 시

from itertools import permutions, combination

result = list(permutions(data,3)) 
=> 6가지 경우의 수

result = list(combination(data, 2))
=> 3가지 경우의 수

from itertools import product, combinations_with_replacement

result = list(product(data,**repeat=2**)) # 중복순열만 repeat로 명시를 해주자.

result = list(combinations_with_replacement(data,2))
```

### heapq

- heapq
- heapq.heappush()
- heapq.heappop()

```python
import heapq

def heapsort(iterable):
	h = []
	result = []
	
	# 모든 원소를 차례대로 힙에 삽입.
	for value in iterable:
		**heapq.heappush(h, value)**
	# 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
	for i in range(len(h))
		**result.append(heapq.heappop(h))**
	return result

result = heapsort(1,3,5,7,9,2,4,6,8,0)
=> [0 ... 9]까지 오름차순으로 정렬된다.

# 파이썬에서는 최대 합을 제공하지 않으므로
# 1. 힙에 원소를 삽입하기 전 부호 뒤집기
# 2. 힙에서 원소를 꺼낸 뒤에 다시 원소 부호를 바꾸기

	**heapq.heappush(-h,value)
	result.append(-heapq.heappop(h))

# 위와 같이 해주면 내림차순으로 힙정렬 할 수 있다.**
```

### bisect : 파이썬에서 제공하는 이진 탐색 라이브러리

- 정렬된 배열에서 특정한 원소 찾기에 매우 효율적.
- **bisect_left(arr, x)** : 정렬된 순서를 유지하면서 리스트 arr에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
- **bisect_right(arr, x)** : 정렬된 순서를 유지하면서 리스트 arr에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

```python
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left) => 2 (1,2,(여기),4,4,8)
print(bisect_right) => 4 (1,2,4,4,(여기),8)

def count_by_range(arr, left_value, right_value):
	right_index = bisect_right(a, right_value)
	left_index = bisect_left(a, left_value)
	return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(**count_by_range(a, 4, 4)**)  => 2 (4,4)를 셈
print(**count_by_range(a, -1, 3)**) => 6 (1,2,3,3,3,3)를 셈
```

- **위에서 구현한 임의의 함수** **count_by_range(arr, left_value, right_value)** : [left_value, right_value]에 속하는 데이터의 개수를 반환한다. 즉 left ≤ x ≤ right인 원소의 개수를 O(logN)으로 빠르게 계산할 수 있다.

## collections(deque와 count)

1. deque : 보통 파이썬에서는 deque를 사용해 큐를 구현한다. Queue 라이브러리가 있긴한데 일반적인 큐 자료구조를 구현하는 라이브러리는 아니다. 따라서 deque를 이용해 큐를 구현해야 한다!

    [deque와 리스트의 시간복잡도 비교](https://www.notion.so/7b318d2b682443a4bb1d76773ff91627)

- 하지만 deque는 리스트처럼 인덱싱, 슬라이싱 등의 기능은 사용할 수 없음에 유의하자.

 2.  Counter : 등장 횟수를 세는 기능을 제공한다. 

```python
from colletions import Counter

counter = Counter(['red','blue','red','grenn','blue','blue',])

print(counter['blue']) => 3
print(counter['red']) => 2
print(dict(counter)) => {'red':2, 'blue':3,'green':1}
```

### math

- factorial(x)
- sqrt(x)
- gcd(a, b)

answer = sorted(list(set(answer)))
