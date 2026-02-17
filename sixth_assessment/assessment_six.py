# =========================
# BASIC SECTION
# =========================

def sum_list(numbers):
    """
    Return the sum of all numbers in a list.
    """
    return sum(numbers)


def count_even(numbers):
    """
    Return the count of even numbers in a list.
    """
    return sum(1 for n in numbers if n % 2 == 0)


def capitalize_sentence(sentence):
    """
    Return the sentence with the first letter of each word capitalized.
    """
    return " ".join(word.capitalize() for word in sentence.split())


def reverse_string(s):
    """
    Return the reversed string.
    """
    return s[::-1]


def max_in_list(numbers):
    """
    Return the maximum number in a list.
    """
    return max(numbers) if numbers else None


# =========================
# INTERMEDIATE SECTION
# =========================

def factorial(n):
    """
    Return the factorial of a non-negative integer n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def remove_duplicates(lst):
    """
    Return a list with duplicates removed while preserving order.
    """
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


def sum_of_squares(numbers):
    """
    Return the sum of squares of all numbers in a list.
    """
    return sum(n ** 2 for n in numbers)


def sort_dict_by_values(d):
    """
    Return a list of tuples sorted by dictionary values.
    """
    return sorted(d.items(), key=lambda x: x[1])


def print_multiplication_table(n):
    """
    Return a 2D list representing the multiplication table up to n.
    """
    return [[(i+1)*(j+1) for j in range(n)] for i in range(n)]


# =========================
# ADVANCED SECTION
# =========================

def rotate_list(lst, k):
    """
    Rotate the list to the right by k steps.
    """
    if not lst:
        return []
    k %= len(lst)
    return lst[-k:] + lst[:-k]


def fibonacci_list(n):
    """
    Return a list of Fibonacci numbers up to index n.
    """
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    prev = fibonacci_list(n - 1)
    next_value = prev[-1] + prev[-2]
    return prev + [next_value]


def flatten_list(lst):
    """
    Recursively flatten a nested list of integers.
    """
    if not lst:
        return []
    first, rest = lst[0], lst[1:]
    if isinstance(first, list):
        return flatten_list(first) + flatten_list(rest)
    else:
        return [first] + flatten_list(rest)


def is_palindrome(s):
    """
    Recursively determine whether a string is a palindrome.
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:])


def count_inversions(lst):
    """
    Return the number of inversions in a list (pairs where a[i] > a[j] for i < j).
    """
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_split = merge_count(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge_count(left, right):
        result = []
        i = j = inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inv += len(left) - i
                j += 1
        result += left[i:] + right[j:]
        return result, inv

    _, inversions = merge_sort(lst)
    return inversions
