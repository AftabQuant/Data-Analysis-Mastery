def fun(x):
    if x%2 == 0 : return x

arr = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(fun, arr))
print(even)