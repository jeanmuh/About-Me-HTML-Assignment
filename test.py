def filter_numbers(numbers):
    for num in numbers:
        if num < 0:
            continue 
        if num > 100:
            break  
        print(num)