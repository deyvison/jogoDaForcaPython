import bibForca
import random
a= open("dicionario.txt")
dicionario=a.readlines()

jogar = 'NÃO'
jogando= 'SIM'
cont=8
bibForca.Entrada()

while (jogar!='SIM'):
    print('Tente descobrir a palavra: \n')
    palavra = random.choice(dicionario)
    listapalavra=list(palavra)
    acertadas=[]
    jogadas=[]
    descobrir=[]
    for a in range(len(palavra)-1):
        descobrir.append('_')
    print(descobrir)
    
    while(cont>0)and(jogando=='SIM') :
        letra=str.upper(input('\ndigite uma letra: '))
        while (str.isdigit(letra)==True) or (bibForca.TestaEntrada(letra)==False):
            letra=str.upper(input('Entrada inválida, digite novamente: '))
        while ((bibForca.ValidaJogada(letra,jogadas))==True) :
            letra=str.upper(input('Você já jogou nessa letra, digite novamente: '))
        for i in range(len(palavra)):
            if palavra[i]==letra:
                descobrir[i]=letra
        print(descobrir)
        if (letra in listapalavra):
            acertadas.append(letra)
            print('\nParabéns você acertou!')
            if ('_' in descobrir):
                print("\nVocê ainda tem " , cont , "chances")
            
        elif(letra not in listapalavra):
            cont -=1
            if cont >0:
                print('\nvocê errou e agora só tem ', cont , 'chances')
            
        jogadas.append(letra)
        if ('_' not in descobrir):
            jogando = 'NÃO'
            
    if (cont <= 0):
        print('Voce perdeu, pois esgotou todas as possibilidades e a palavra era' , palavra)
    jogar=str.upper(input('Deseja sair: '))
    if (jogar!='SIM'):
        cont =8
        jogando='SIM'

print("Volte sempre!!!")
    
    

            
    
    
 
