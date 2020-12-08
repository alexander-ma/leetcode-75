# 5.15

import random

def compute_random_subset(n, k):
  s = set()
  while len(s) < k:
    x = random.randint(0, n-1)
    if x not in s:
      s.add(x)
  
  return list(s)

def compute_random_subset2(n, k):
  res = {}
  for i in range(k):
    r = random.randint(i, n-1)
    i_val = res.get(i, i)
    r_val = res.get(r, r)
    res[i] = r_val
    res[r] = i_val

  return [res[i] for i in range(k)]

print(compute_random_subset2(10, 4))