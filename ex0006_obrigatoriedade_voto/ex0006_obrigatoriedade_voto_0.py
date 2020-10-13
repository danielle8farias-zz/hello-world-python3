########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
# Descrição: Usuário informa a idade e programa retorna se o voto é obrigatório.
########

idade = int(input('Digite sua idade: '))

if idade < 16:
    print(f'Com {idade} anos: NÃO VOTA')
#else if
elif 16 <= idade <18 or idade > 65:
    print(f'Com {idade} anos: VOTO OPCIONAL')
else:
    print(f'Com {idade} anos: VOTO OBRIGATÓRIO\n')
