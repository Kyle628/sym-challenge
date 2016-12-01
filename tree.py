#dang this wasn't actually my solution. This is what I was working on before I realized
#that they said they defined a tree class and I forgot to copy what I actually submitted back into here
T = (5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
def solution(T):
    root_value = T[0]
    count = traverse(T, root_value, 0)

def traverse(node, root_value, count=0):
    print node[0]
    if node[0] > root_value:
        count += 1
    print node[1]
    if node[1] != None:
        count += traverse(node[1], root_value, count)
    print node[2]
    if node[2] != None:
        count += traverse(node[2], root_value, count)
    else:
        return count


'''def solution(T):
    print T[0]
    num_visible = traverse(T, T[0], 0)
    return num_visible

def traverse(T, root_value, count=0):
    if T:
        if T[0] < root_value:
            count += 1
        traverse(T[1][1], root_value, count)
        traverse(T[1][2], root_value, count)
    return count'''

'''def solution(T):
    count = 1
    root_value = T[0]
    for node in T[1:]:
        if node[0] < root_value:
            count += 1
        if node[1] != None:
            if node[1] < root_value:
                count += 1
        if node[2] != None:
            if node[1] < root_value:
                count += 1'''



print solution(T)
