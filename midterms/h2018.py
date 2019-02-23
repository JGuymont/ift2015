# question 2 a)
def max(S, curr_max=0, i=0):
    if i + 1 > len(S):
        return curr_max
    curr_max = S[i] if S[i] > curr_max else curr_max
    return max(S, curr_max, i+1)

def natural_join(A, B):
    join = []
    for i, j in A:
        for k, l in B:
            if j == k:
                join.append((i, j, l))
    return join

if __name__ == '__main__':
    A = [(1,1), (2,3), (2,4), (3,1)]
    B = [(1,2), (4,1)]
    A.sort(key=lambda x: x[1])
    print(A)
    #print(natural_join(A,B))