import myproject

def main():
    print('Running ...')
    result = myproject.inc(3)
    print(f'inc(3)={result}')
    print('done.')

if __name__ == '__main__':  # pragma: no cover
    main()  # pragma: no cover
