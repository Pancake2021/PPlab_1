from time import sleep

from main import run

if __name__ == '__main__':
    run('cat')
    sleep(10)
    print('\n\n')
    run('dog')
    print('the end')