import sys

def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:  # with-block
        return [int(line.strip()) for line in f]            # list comprehension

def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == '__main__':
    main(filename=sys.argv[1])