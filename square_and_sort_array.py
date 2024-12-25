def square_and_sort(arr):
    n = len(arr)
    result = [0] * n
    left, right = 0, n-1
    pos = n-1
    
    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2
        
        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        pos -= 1
    return result

input_array = [-3, -2, -1, 3, 34, 72, 87]
result_array = square_and_sort(input_array)
print(result_array)