import math

def add(a=0, b=0):
    """
    Return the sum of a and b.
    arguments: a: int, b: int
    """
    return a + b

def is_prime(n):
    """
    Check if a number is a prime.
    arguments: n: int
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """
    Return the factorial of a number.
    arguments: n: int
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """
    Return the nth Fibonacci number.
    arguments: n: int
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def reverse_string(s):
    """
    Return the reversed string.
    arguments: s: str
    """
    return s[::-1]

def find_max(lst):
    """
    Return the maximum value in a list.
    arguments: lst: list
    """
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def count_vowels(s):
    """
    Return the number of vowels in a string.
    arguments: s: str
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def merge_sort(arr):
    """
    Sort an array using the merge sort algorithm.
    arguments: arr: list
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def gcd(a, b):
    """
    Return the greatest common divisor of a and b.
    arguments: a: int, b: int
    """
    while b:
        a, b = b, a % b
    return a

def is_palindrome(s):
    """
    Check if a string is a palindrome.
    arguments: s: str
    """
    return s == s[::-1]
