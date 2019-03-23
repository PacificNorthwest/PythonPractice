from time import time
import concurrent.futures


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [(11963309, 22615973), (20304677, 38142172),
           (1551645, 2229620), (2039045, 2020802)]


def main():
    print('Starting processing')
    start = time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
        list(pool.map(gcd, numbers))
    end = time()

    print(f'Took {round(end - start, 3)} seconds')

if __name__ == '__main__':
    main()
