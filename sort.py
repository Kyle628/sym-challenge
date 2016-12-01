A = [1, 3, 5]

def solution(A):
    if is_sorted(A):
        return True
    for i, num in enumerate(A):
        for j in range(i+1, len(A)):
            #keep original values
            OG_i = A[i]
            OG_j = A[j]
            #try swapping
            A[i] = OG_j
            A[j] = OG_i
            #worked
            print A
            if is_sorted(A):
                return True
            #didn't work swap back
            A[i] = OG_i
            A[j] = OG_j

    return False

def is_sorted(A):
    for i, num in enumerate(A):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                return False
    return True

print solution(A)
