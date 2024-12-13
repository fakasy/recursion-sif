


def tri_recursion(n):
    if n > 0:
        return n + tri_recursion(n - 1)
    else:
     return 0
 
print("Tri Recursion Result:", tri_recursion(10))
def tri_recursion(y):
  if y > 0:
    result = y + tri_recursion(y - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results: ", tri_recursion(10))


number = int(input("Masukkan angka: "))
print("Tri Recursion Result:", tri_recursion(number))

def tri_recursion_f(n):
    if n <= 0:
        return 0
    return n + tri_recursion_f(n - 1)

def tri_recursive_f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return tri_recursive_f(n-1) + tri_recursive_f(n-2) + tri_recursive_f(n-3)

number = int(input("Masukkan angka: ")) 
print("Tri Recursion Result:", tri_recursion_f(number))
print("Tri Recursive Result:", tri_recursive_f(number))


# faktorial saya bikin gabut aja sih
# faktorial saya bikin gabut aja sih
# faktorial saya bikin gabut aja sih
# faktorial saya bikin gabut aja sih

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)
    
number = int(input("Masukkan angka: "))
print("Faktorial:", faktorial(number))

def tri_recursion_result(n):
    result = 0
    for i in range(n+1):
        result += tri_recursion(i)
    return result

number = int(input("Masukkan angka: ")) 
print("Tri Recursion Result:", tri_recursion_result(number))


# def tri_recursion(n):
#     if n > 0:
#         return n + tri_recursion(n - 1)
#     else:
#         return 0


# number = int(input("Masukkan angka: "))
# print("Tri Recursion Result:", tri_recursion(number))     

