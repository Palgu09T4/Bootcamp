def series_22(N):
    series = [1, 4, 7]
    
    if N < 1:
        return
    
    for num in series:
        if num <= N:
            print(num, end=" ")
    
    i = 3
    while True:
        next_val = series[i - 1] + (series[i - 1] - series[i - 2]) + 2
        if next_val > N:
            break
        print(next_val, end=" ")
        series.append(next_val)
        i += 1

# Driver code
N = int(input("Enter the value of N: "))
series_22(N)