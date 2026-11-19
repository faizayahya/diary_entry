def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
        
    return product


#24 x 0 = 0 needs to stop before 0 

print(factorial(5))
# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 0
