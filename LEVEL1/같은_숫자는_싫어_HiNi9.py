def solution(arr):
    answer = [arr[0]]
    i = 1
    while i < len(arr):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
        i = i + 1
    return answer