#!/Users/aavaniskakangas/Documents/projects/brasilia/package_example/.venv/bin/python3
from dev_aberto import hello

if __name__ == '__main__':
    date, name = hello()
    print('Último commit feito em:', date, ' por', name)