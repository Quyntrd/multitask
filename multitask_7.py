from concurrent.futures import ProcessPoolExecutor
import random
import argparse


def point(iter):
    """This function checks if the point inside the circle or not"""
    x = random.random()
    y = random.random()
    k = (x**2 + y**2 < 1.0)
    return k


if __name__ == "__main__":
    """This soft finds number pi with Monte-Carlo's method by using multiprocessing"""
    parser = argparse.ArgumentParser(description='Input number of points')
    parser.add_argument('--points', type=int,default="100000", help='Input number of point')
    args = parser.parse_args()
    iter = [i for i in range(args.points)]
    sum_k = 0
    with ProcessPoolExecutor(max_workers=4) as p:
        r = list(p.map(point, iter))
        for j in range(len(r)):
            sum_k += r[j]
        result = (4*sum_k/args.points)
        print(result)