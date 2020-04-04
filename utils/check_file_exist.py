import os


def file_exist(file):
    if not os.path.isfile(file):
        return True
    else:
        op = input(
            '\nArquivo já existe, deseja sobreescrever [y/n]: ')
        if op.lower().strip() == 'y':
            return True
        elif op.lower().strip() == 'n':
            return False
        else:
            print('Opção incorreta.')
            return False
