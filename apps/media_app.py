def apps(settings, validate, type_midia, directory='', midia='', op=True):
    """Direciona para ações de de input se o diretorio for o de origem e 
       para as ações de output se o diretório for de destino
    """

    # Ações de input (diretório de origem)
    if op:
        while True:
            input_video_format = input(
                f'\nDigite o formato do {midia}(s) de {directory}: ')
            if validate.validate_midia(input_video_format.lower().strip(), type_midia):
                settings.format_input(input_video_format.lower().strip())
                return True
            else:
                continue
            print()

    # Ações de output (diretório de destino)
    else:
        while True:
            output_audio_format = input(
                f'\nDigite o formato do {midia}(s) de {directory}: ')
            if validate.validate_midia(output_audio_format.lower().strip(), type_midia):
                settings.format_output(output_audio_format.lower().strip())
                return True
            else:
                continue
            print()


def app_cut(settings, validate):
    """Executa a funcao de recotar o vídeo"""

    while True:
        op = input('\nDeseja recortar o vídeo [y/n]? ')
        if op.lower() == 'y':
            while True:
                duration_time = input(
                    'Digite o tempo do(s) áudio(s) de saída [HH:MM:SS]: '
                )
                # Vetifica se o formato passado é válido
                if validate.validate_time_midia(duration_time.strip()):
                    settings.time_midia(duration_time.strip())
                    settings.execute()
                    return True
                else:
                    continue
        elif op.lower() == 'n':
            settings.execute()
            print(f'\n{"#" * 20} FIM {"#" * 20}')
            return True
        else:
            print('INFO: Opção incorreta.')
            continue
