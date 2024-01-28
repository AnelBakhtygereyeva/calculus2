#8
def function(x):
    return 1/(x-1)**2

def compositeSimpsons(function, a, b, n):

    if n % 2 != 0:
        return None

    d = (b - a)/n 
    first = function(a)
    last = function(b)

    x = a #increment size
    sum = 0 
    for i in range(n - 1): #we don't calculate the last number
        x += d
        value = function(x)
        if i % 2 == 0:
            sum += 4 * value
        else:
            sum += 2 * value       

    total = (d/3) * (first + sum + last)
    return total

print(compositeSimpsons(function, 2, 4, 4))