def solution(arr):
    tmp = arr[0]
    
    if len(arr) == 1:
        return [-1]
    else:
        for i in arr:
            if tmp > i:
                tmp = i
        arr.remove(tmp)
        return arr