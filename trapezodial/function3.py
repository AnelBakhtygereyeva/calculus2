#3
def function(x):
    return x**2 + 1

def compositeTrapezodial(function, a, b, n):

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
        sum += 2 * value      

    total = (d/2) * (first + sum + last)
    return total

print(compositeTrapezodial(function, -1, 1, 4))