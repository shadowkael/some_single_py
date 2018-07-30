def searchMatrix(matrix, target):
    # write your code here
    if not matrix:
        return False
    if target < matrix[0][0]:
        return False
    if target > matrix[-1][-1]:
        return False
    for item in matrix:
        if item[-1] >= target:
            for num in item:
                if num == target:
                    return True
            else:
                return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7))
