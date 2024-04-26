import random

menu = """

[r] - Pedra                        
[p] - Papel                        
[t] - Tesoura                 

"""

def jogar():
    jogador = input(menu)

    if(jogador != 'r') and (jogador != 'p') and (jogador != 't'):
        return "Opção inválida"
    else:
        computador = random.choice(['r', 'p', 't'])

        #empate
        if(jogador == computador):
            return "Empate!"

        #vitória
        if(ganhou(jogador,computador)):
            return f"Escolha do computador: {computador}\nVocê GANHOU!"
        #derrota
        else:
            return f"Escolha do computador: {computador}\nVocê PERDEU!"

#ganhou ou perdeu
def ganhou(p1,p2):
    if(p1 == 'r' and p2 == 't') or (p1 == 'p' and p2 == 'r') or (p1 == 't' and p2 == 'p'):
        return True
    else:
        return False


print(jogar())