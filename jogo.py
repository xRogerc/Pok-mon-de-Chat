from random import *
import os
import time

os.system('cls')
select = int(input("Escolha seu Pokémon:\n 1 para Pikachu\n 2 para Squirtle\n 3 para Charmander\n ainda não adicionado: 4 para Bulbasauro\n Digite a Escolha Aqui: "))
pokeNivelP = 1
death = False
win = False
pokemon = ("")
pcokemon = ("")
continuar = ("")


print("--------------------------------------------------")

if select == 1:
    print("Você Escolheu o Pikachu")
    pokemon = ("Pikachu")

elif select == 2:
    print("Você Escolheu o Squirtle")
    pokemon = ("Squirtle")

else:
    print("Você Escolheu o Charmander")
    pokemon = ("Charmander")


while (death == False):
    if select >= 5:
        death = True


    while(death == False and win == False):
        pcPokemon = int(randrange(1,5))
        pcPokeNivel = int(randrange(0,5))
        print("--------------------------------------------------\n")

        if pcPokemon == 1:
            print("Você esta enfrentando um Pikachu Selvagem")
            print('''
quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     '
        :##.       ==             .###.       `.      `.    `
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                   `:.:'
                  ''')
            pcokemon = ("Pikachu")

        elif pcPokemon == 2:
            print("Você esta enfrentando um Squirtle Selvagem")
            print(''' 
               _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        
      ,'                           .
      .'\               ,"".       `
     ._.'|             / |  `       
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | 
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \  .     `
`."""""'-.`-...,---------','         `. `....__.
.'        `"-..___      __,'\          \  \     
\_ .          |   `""""'    `.           . \     
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'"""`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              
               \/    `"" """""""`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         ."     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'
                 ''')
            pcokemon = ("Squirtle")

        else:
            print("Você esta enfrentando um Charmander Selvagem")
            print(''' 
              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         """"'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,
   -" /`.         _,'     | _  _  _.|
    ""--'---"""""'        `' '! |! /
                            `" " -' 
                 ''')
            pcokemon = ("Charmander")

        print("--------------------------------------------------")

        if pcPokemon == select:
            print(f"Seu", pokemon, "empatou no combate ele será resolvido pelo nivel")
            if pcPokemon + pcPokeNivel > select + pokeNivelP:
                print(f"Você Perdeu seu", pokemon, "Morreu")
                death = True
                for i in range(6):
                  os.system('color c')
                  time.sleep(0.2)
                  os.system('color f')
                  time.sleep(0.2)

            else:
                print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
                pokeNivelP = pokeNivelP + 1
                print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
                continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                win = True
            

        elif pcPokemon == 1 and select == 2:
            print(f"Você Perdeu seu", pokemon, "Morreu")
            death = True
            for i in range(6):
                  os.system('color c')
                  time.sleep(0.2)
                  os.system('color f')
                  time.sleep(0.2)

        elif pcPokemon == 1 and select == 3:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
            win = True
                    

        elif pcPokemon == 2 and select == 1:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
            win = True

        elif pcPokemon == 2 and select == 3:
            print(f"Você Perdeu seu", pokemon, "Morreu")
            death = True
            for i in range(6):
                  os.system('color c')
                  time.sleep(0.2)
                  os.system('color f')
                  time.sleep(0.2)

        elif pcPokemon == 3 and select == 1:
            print(f"Você Perdeu seu", pokemon, "Morreu")
            death = True
            for i in range(6):
                  os.system('color c')
                  time.sleep(0.2)
                  os.system('color f')
                  time.sleep(0.2)

        elif pcPokemon == 3 and select == 2:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ".lower())
            win = True


    if continuar == ("sim"):
      win = False

    elif continuar == ("s"):
        win = False

    elif continuar == ("não"):
      death = True

    else:
        death = True