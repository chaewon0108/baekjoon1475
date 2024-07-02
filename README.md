# baekjoon1475

> 1일차 목표 마지막! 하루동안 잘 버텼다. 마지막까지 화이팅이당


---
# 문제
다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

## 입력
첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.

## 출력
첫째 줄에 필요한 세트의 개수를 출력한다.

---

# 내 생각 💡
## 처음
📌 출력해야 하는 것 = 최소 몇 세트가 필요한지
📌 6이나 9는 호환 가능

1. 방번호 N 입력받기

2. 방 번호에 같은 숫자가 들어가는지 판별
- 6,9를 제외한 숫자가 나오면 그냥 count, 함

3. 6과 9가 포함된 경우
- 6이나 9가 N에 짝수만큼 포함되어 해당 짝수-1만큼 count
- 6과 9중가 나올 때 나오는 숫자 중에서 적은 숫자를 count로 사용
- 66, 99, 69, 96는 한 세트로 가능
- 666, 669, 699, 966, 996, 999은 한세트로 불가능

4. 최종적으로 max count가 출력되어야함 !!

---

# 결과

틀린 코드
```
N = input()
num_list = list(map(int, N))
count = 0

for i in range(len(N)):
  six_cnt = num_list.count(6)
  nine_cnt = num_list.count(9)
  cnt = num_list.count(i)
  
  if num_list[i] == 6 or num_list[i] == 9:
    if six_cnt <= nine_cnt:
      six_cnt += 1
      count = six_cnt
    else:
      nine_cnt += 1
      count = nine_cnt

  else:
    count += cnt

print(count)
```

최종 통과 코드
```
N = input()
num_list = list(map(int, N))
count = [0]*10

for i in str(N):
  if i == '6' or i == '9':
    if count[6] <= count[9]:
      count[6] += 1
    else:
      count[9] += 1
      
  else:
    count[int(i)] += 1

print(max(count))
```

<img width="698" alt="image" src="https://github.com/chaewon0108/baekjoon1475/assets/174469937/b6c20225-487d-479c-939b-0801888d549f">

음...
- for i in str(N):
- if i == '6' or i == '9':
- if count[6] <= count[9]:

이 부분을 바꿨는데 됐다
내가 너무 복잡하게 생각한 것 같다..
이 문제 아직 좀 헷갈린다 나중에 다시 봐야 할 것 같다 ㅠㅠ..


---

# 참고 사이트
- https://soopeach.tistory.com/15
- https://velog.io/@hrzo1617/%EB%B0%B1%EC%A4%80-1475-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%A9-%EB%B2%88%ED%98%B8
