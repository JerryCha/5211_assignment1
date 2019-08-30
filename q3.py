import numpy

def createMatrix(A):
    #TODO write your program below.
    #Use numpy to create the matrix B.
    #return B
    n = len(A)
    B = numpy.zeros((n, n))
    
    # Approach 1
    '''
    for j in range(n):
        for i in range(j):
            for k in range(i,j+1):
                B[i,j] += A[k]
    '''
    
    # Approach 2
    # The matrix has a characteristic that all the elements on diagonal and below
    # are zero.
    # Based on approach 1, the iteration of i is vertical increase, from the top to 
    # the bottom each with each increment of j.
    # Therefore, there is a relation: B[i,j] = B[i-1, j] - A[i-1], where 0 ≤ i < j < n
    
    # Specify the first non-zero element.
    B[0, 1] = A[0] + A[1]
    # Initialize the first row's value
    for j in range(2, n):
        B[0, j] = B[0, j-1] + A[j]

    # Calculate the remaining values based on the previous iteration
    for j in range(1, n):
        for i in range(1, j):
            B[i,j] = B[i-1, j] - A[i-1]
    return B

def checkResult(B, correctB):
    assert numpy.equal(B, correctB).all()

checkResult(createMatrix([0,0,0,0]), [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
checkResult(createMatrix([1,2,3]), [[0,3,6],[0,0,5],[0,0,0]])
checkResult(createMatrix([-1,2,-3]), [[0,1,-2],[0,0,-1],[0,0,0]])
checkResult(createMatrix([10,1,-2,12,4,-100]), [[0,11,9,21,25,-75],[0,0,-1,11,15,-85],[0,0,0,10,14,-86],[0,0,0,0,16,-84],[0,0,0,0,0,-96],[0,0,0,0,0,0]])