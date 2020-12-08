# 5.10

def apply_perm(a, p):
  res = [0] * len(a)
  for i in range(len(a)):
    res[p[i]] = a[i]
  return res

a = [1,2,3,4,5,6]
p = [0,2,1,4,3,5]

def apply_permutation(perm, A):
  print("Original array:", A)
  print("perm:", perm)
  for i in range(len(A)):
    next = i
    print("Setting i=next=", next)
    while perm[next] >= 0:
      print("Swapping...")
      A[i], A[perm[next]] = A[perm[next]], A[i]
      print("Result after swap:", A)
      temp = perm[next]
      print("temp=", temp)
      perm[next] -= len(perm)
      print("perm=", perm)
      next = temp
      print("next=", next)
  perm[:] = [a + len(perm) for a in perm]
  print(perm)
  return A


print(apply_permutation(p, a))
