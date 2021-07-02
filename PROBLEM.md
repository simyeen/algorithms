# 프로그래머스

---

# Level 1

- 소문자 - 대문자 변경

[https://blockdmask.tistory.com/416](https://blockdmask.tistory.com/416)

- set함수 쓰는데 원하는데로 순서정렬가능

- 리스트 컴프리헨션을 물음표 연산자 할때 많이 사용해보자!

ex) [https://programmers.co.kr/learn/courses/30/lessons/72410/solution_groups?language=python3&type=all](https://programmers.co.kr/learn/courses/30/lessons/72410/solution_groups?language=python3&type=all)

- 행렬의 덧셈 : zip과 numpy를 다뤄보자.
  [https://programmers.co.kr/learn/courses/30/lessons/12950/solution_groups?language=python3](https://programmers.co.kr/learn/courses/30/lessons/12950/solution_groups?language=python3)

- join 함수 "이 값을 넣어서 문자열로 합치기".join(arr)

- ** 리스트에서 순서 안바뀌고 중복 제거하기. **
  인덱스값 초과할 때 오류나는 것들 인덱스 슬라이싱 잘 쓰면 범위넘어서도 오류안뜬다!
  [https://programmers.co.kr/learn/courses/30/lessons/12906/solution_groups?language=python3](https://programmers.co.kr/learn/courses/30/lessons/12906/solution_groups?language=python3)
- index slicing에서 del a[4:10]하면 4에서 10까지 삭제됨.

- 문자열내에서 .count함수 사용하기
  [https://programmers.co.kr/learn/courses/30/lessons/12916/solution_groups?language=python3](https://programmers.co.kr/learn/courses/30/lessons/12916/solution_groups?language=python3)

- 10진법 ⇒ n진법 : 나온 나머지들을 $n^0$부터 차례로 $n^n$까지 써주면 된다.(몫이 0이 될때 까지)

  n진법 ⇒ 10진법 : int(문자열, base) 이때 주의 할 점은 꼭 안에 문자열로 넣어주어야 convert가 된다.
  **bin(), oct(), hex() 으로 2, 8, 16진수 변환가능.**

```
def solution(n):
answer = 0

strings = ''
while n != 0 :
    strings += str(n % 3)
    n //= 3

base = 3
answer = int(strings, base) # 10진법으로 변환댐

return answer
```

- 약수 구하기

```python
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5: # 루트로 소수점 날려버린게 같으면 약수 개수가 홀수이다!!
            answer -= i
        else:
            answer += i
    return answer
```

- 제곱근 확인하기

```python
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0: # 정수면 sqrt % 1 => 0.0이 나오고, 아니면 소수점이 나온다.
        return (sqrt + 1) ** 2
    return 'no'
```

- 비밀지도 문제 (카카오) [https://www.crocus.co.kr/1660](https://www.crocus.co.kr/1660)(just함수 참고)

```python
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:]) # 비트 연산자 '|'를 활용
        a12=a12.rjust(n,'0') # rjust, ljust를 사용해서 원하는 길이만큼 조정하기
        a12=a12.replace('1','#') # 힘들게 slicing말고 replace를 사용해보자.
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
```

- target = target[:index-1] + '1' + target[index:] 이렇게 하면 딱 index하나만 교체가능.

# Level 2

- enumerate : 열거하다라는 뜻으로 보통 for in range에 같이 쓴다. 이걸 사용해서 편하게 index를 같이 리턴 할 수 있다.  
  **(예시) queue = [(i,p) for i,p in enumerate(priorities)]
  queue = [ i for i in enumerate(priorities)]와 동일한 결과이다. (값 앞에 index가 순서대로 붙음.)**

      [https://programmers.co.kr/learn/courses/30/lessons/42587/solution_groups?language=python3](https://programmers.co.kr/learn/courses/30/lessons/42587/solution_groups?language=python3)

- !! 아래처럼 하면 동일한 key에 여러개의 value를 []로 넣어 줄 수있다!

```python
def solution(clothes):
	answer = 0

	d = dict()
	for value, key in clothes:
	    d.setdefault(key, []).append(value)

	return d
```

[https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-a-dictionary](https://stackoverflow.com/questions/3199171/append-multiple-values-for-one-key-in-a-dictionary)

- for-else 구문 for 문이 전부다 돌아갔을 때만 실행된다

```
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        **for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1**

    return answer
```

- 왼쪽부터 찾을거면 find함수 오른쪽 부터 찾을거면 rfind함수를 사용하자
  [https://hyunssssss.tistory.com/365](https://hyunssssss.tistory.com/365)
