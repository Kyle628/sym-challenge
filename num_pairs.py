A = [1, 3, 3, 4, 5, 6]

'''def solution(A):
    if not A:
        return 0
    MILLION = 1000000
    pairs_found = 0
    while pairs_found < MILLION:
        for i,num in enumerate(A):
            for j in range(i+1, len(A)):
                if num == A[j]:
                    pairs_found += 1
        break
    return pairs_found

print solution(A)'''

def faster_solution(A):
    if not A:
        return 0
    seen_before = []
    count = 0
    for num in A:
        if num in seen_before:
            count += 1
        else:
            seen_before.append(num)
    return count

print faster_solution(A)
