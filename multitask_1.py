import multiprocessing
import argparse
import random


def create_matrix(i, j):
    """This function creates ixj matrix with random float numbers"""
    matrix = [[random.random()*100 for x in range(j)] for y in range(i)]
    return matrix


def sum_row(i, mat):
    """This function summs all elements in a row in the matrix"""
    if i<=len(mat):
        sum = 0
        for i in range(len(mat)):
            sum += mat[i]
    return sum


if __name__ == "__main__":
    """This soft summs all elements in the matrix by using multiprocessing"""
    parser = argparse.ArgumentParser(description='Input number of rows and columns')
    parser.add_argument('--rows', type=int,default="10000", help='Input number of rows')
    parser.add_argument('--columns',type=int,default="10000" ,help='Input number of columns')
    args = parser.parse_args()
    matrix = create_matrix(args.rows, args.columns)
    result = 0
    index = []
    for i in range(args.rows):
        index += ((i, matrix[i]),)
    with multiprocessing.Pool(multiprocessing.cpu_count()*2) as p:
        r = p.starmap(sum_row, index)
    for j in range(len(r)):
        result += r[j]
    print("sum of all elements = ", result)