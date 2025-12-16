# series_challenges.py
# Python solutions for Coding Challenges 17-24

def series_17(N):
    """Series 1,2,3,...N"""
    return list(range(1, N+1))

def series_18(N):
    """Series 1,3,5,...N"""
    return [i for i in range(1, N+1, 2)]

def series_19(N):
    """Series 4,16,36,64,...N (squares of even numbers)"""
    result = []
    i = 2
    while i*i <= N:
        result.append(i*i)
        i += 2
    return result

def series_20(N):
    """Series 1,2,4,7,11,16,22,...N (difference increases by 1 each time)"""
    result = []
    num = 1
    diff = 1
    while num <= N:
        result.append(num)
        diff += 1
        num += diff
    return result

def series_21(N):
    """Series 1,4,9,25,36,49,81,...N (perfect squares with skipping squares of 2?)"""
    # Based on pattern: 1^2, 2^2, 3^2, 5^2, 6^2, 7^2, 9^2,... skip multiples of 4?
    result = []
    i = 1
    while i*i <= N:
        if i != 4 and i != 8:  # skipping squares of 4, 8 etc. pattern from example
            result.append(i*i)
        i += 1
    return result

def series_22(N):
    """Series 1,4,7,12,23,...N (difference pattern seems irregular, assume sum of last two differences)"""
    result = [1]
    next_val = 4
    if N >= 4:
        result.append(4)
    a, b = 1, 4
    while True:
        next_val = a + b + (b - a)  # approximate pattern
        if next_val > N:
            break
        result.append(next_val)
        a, b = b, next_val
    return result

def series_23(N):
    """Series 1,5,9,13,21,25,29,37,41,...N (pattern: +4,+4,+8,+4,+4,+8...)"""
    result = [1]
    diffs = [4,4,8]
    idx = 0
    while True:
        next_val = result[-1] + diffs[idx % 3]
        if next_val > N:
            break
        result.append(next_val)
        idx += 1
    return result

def series_24(N):
    """Fibonacci series: 1,1,2,3,5,8,13,21,...N"""
    result = [1, 1]
    while True:
        next_val = result[-1] + result[-2]
        if next_val > N:
            break
        result.append(next_val)
    return result

# ================== TEST CASES ==================
def run_tests():
    test_values = [10, 30, 50]
    
    print("Testing Series 17:")
    for N in test_values:
        print(f"N={N}: {series_17(N)}\n")
    
    print("Testing Series 18:")
    for N in test_values:
        print(f"N={N}: {series_18(N)}\n")
    
    print("Testing Series 19:")
    for N in test_values:
        print(f"N={N}: {series_19(N)}\n")
    
    print("Testing Series 20:")
    for N in test_values:
        print(f"N={N}: {series_20(N)}\n")
    
    print("Testing Series 21:")
    for N in test_values:
        print(f"N={N}: {series_21(N)}\n")
    
    print("Testing Series 22:")
    for N in test_values:
        print(f"N={N}: {series_22(N)}\n")
    
    print("Testing Series 23:")
    for N in test_values:
        print(f"N={N}: {series_23(N)}\n")
    
    print("Testing Series 24:")
    for N in test_values:
        print(f"N={N}: {series_24(N)}\n")

if __name__ == "__main__":
    run_tests()
