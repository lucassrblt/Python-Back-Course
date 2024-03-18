def get_fibonacci(n: int) -> int:
    fibonacci_array = [0, 1]
    for i in range(0, n - 2):
        fibonacci_array.append(fibonacci_array[len(fibonacci_array) - 2] + fibonacci_array[len(fibonacci_array) - 1])        
    
    print(fibonacci_array[len(fibonacci_array) - 1])

user_value = input('Entrer un entier N : ')
get_fibonacci(int(user_value))


# Correction suite 

def get_fibonacci(n: int) -> int:
    if n <= 0: # Si n = 0 on renvoie 0
        return 0
    elif n == 1: # Si n = 1 on renvoie 1
        return 1
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    
    return b