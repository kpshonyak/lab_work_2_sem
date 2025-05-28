
def find_kth_mth(arr,k, mode="k"):
    if len(arr)<k:
        raise ValueError("Розмір масиву меньше за k")
    arr_copy =arr.copy()
    for i in range(k):
        if mode == "k":
            element = max(arr)
        elif  mode == "m":
            element = min(arr)
        else:
            raise ValueError("Неправиоьний ввід")

        if i == k-1:
            index =arr.index(element)
            descriptor = "найбільший" if mode =="k" else "найменший"
            return descriptor ,element, index 
        arr.remove(element)
def my_max(arr):
    max_val = arr[0]
    for el in arr:
        if el > max_val:
            max_val = el
    return max_val
            


    
    
array =[15, 7, 22, 9, 36, 2, 42, 18]    
print(find_kth_mth(array,2,"m"))