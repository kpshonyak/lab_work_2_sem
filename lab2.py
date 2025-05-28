def custom_max(arr, index):
    max_val = arr[0][index]
    for el in arr:
        if el[index] > max_val:
            max_val = el[index]
    return max_val 

def custom_min(arr, index):
    min_val = arr[0][index]
    for el in arr:
        if el[index] < min_val:
            min_val = el[index]
    return min_val 

def counting_sort(matrix, index):
    if not matrix or len(matrix) == 1:
        return matrix
    
    max_value = custom_max(matrix, index)
    min_value = custom_min(matrix, index)
    count_range = max_value - min_value + 1
    count = [0] * count_range
    output_matrix = [None] * len(matrix)
    
    for row in matrix:
        count[row[index] - min_value] += 1
    
    for i in range(1, count_range):
        count[i] += count[i - 1]
    
    for row in reversed(matrix):
        value = row[index] - min_value
        count[value] -= 1
        output_matrix[count[value]] = row
    
    return output_matrix

def max_hamsters(S, C, hamsters):
    hamsters = counting_sort(hamsters, 0) 
    
    def can_feed(n):
        food_needed = [[H + G * (n - 1)] for H, G in hamsters[:n]]
        food_needed = counting_sort(food_needed, 0)
        total_food = sum(x[0] for x in food_needed)
        
        if total_food > S:
            print(f' ПОМИЛКА: {n} хомяків вимагають {total_food} пакетів корму,ліміт — {S}')
        else:
            print(f'{n} хомяків: {food_needed}, Всього корма: {total_food}, Ліміт: {S}')
        
        return total_food <= S
    
    left, right = 0, C
    best_case = 0
    while left <= right:
        mid = (left + right) // 2
        if can_feed(mid):
            best_case = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return best_case
