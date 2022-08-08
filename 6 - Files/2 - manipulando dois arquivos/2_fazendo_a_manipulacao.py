# Verificando quem mora no guara

with open('nomes_e_cidade.txt', 'r') as arquivo:
    for linha in arquivo:
        if 'guara' in linha:
            with open('moradores_do_guara.txt', 'a') as arquivo_guara:
                arquivo_guara.write(linha)