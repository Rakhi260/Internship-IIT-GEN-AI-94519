'''Q2:

Count Even and Odd Numbers

Take a list of numbers as input (comma-separated).

Count how many are even and how many are odd.

Print results.

Example Input:
10, 21, 4, 7, 8'''
def even_odd(numbers):
    even_count = 0
    odd_count = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count, odd_count

user_input = input("Enter list of numbers separated by commas: ")
number_list = [int(num.strip()) for num in user_input.split(',')]

even_count, odd_count = even_odd(number_list)

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
