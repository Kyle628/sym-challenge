A = []

def solution(A):
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

print solution(A)
