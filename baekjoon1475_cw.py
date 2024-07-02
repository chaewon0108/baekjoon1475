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