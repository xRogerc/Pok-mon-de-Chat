from random import *
import os
import time

os.system('cls')
select = int(input("Escolha seu Pokémon:\n 1 para Pikachu\n 2 para Squirtle\n 3 para Charmander\n 4 para Bulbasauro\n Digite a Escolha Aqui: "))
pokeNivelP = 1
death = False
win = False
pokemon = ("")
pcokemon = ("")
continuar = ("")
bag = [ ]
coin = int(randrange(30,90))
bagO = ("")
merc = ("")

print("--------------------------------------------------")

if select == 1:
    print("Você Escolheu o Pikachu")
    pokemon = ("Pikachu")

elif select == 2:
    print("Você Escolheu o Squirtle")
    pokemon = ("Squirtle")

elif select == 3:
    print("Você Escolheu o Charmander")
    pokemon = ("Charmander")

else:
    print("Você Escolheu o Bulbasauro")
    pokemon = ("Bulbasauro")


while (death == False):
    if select >= 5:
        death = True


    while(death == False and win == False):
        pcPokemon = int(randrange(1,5))
        pcPokeNivel = int(randrange(0,5))
        chancedemerc = int(randrange(1,100))

        if chancedemerc >= 60:
            print("--------------------------------------------------\n")
            print("-----------O Mercador está nas redonzas-----------\n")
            merc = input("Você quer comprar alguma coisa: ").lower()
            if merc == ("sim"):
                print("Você tem: $",coin,"\n")
                print("revive -> 30 golds")
                print("pokebola -> 50 golds")
                comprar = input("O que você quer comprar: ")
                if comprar == ("revive"):
                    coin -= 30
                    bag.append("revive")
                    print("Você tem: $",coin,"\n")

                elif comprar == ("pokebola"):
                    coin -= 50
                    bag.append("pokebola")
                    print("Você tem: $",coin,"\n")

            elif merc == ("s"):
                print("Você tem: $",coin,"\n")
                print("revive -> 30 golds")
                print("pokebola -> 50 golds")
                comprar = input("O que você quer comprar: ")
                if comprar == ("revive"):
                    coin -= 30
                    bag.append("revive")
                    print("Você tem: $",coin,"\n")

                elif comprar == ("pokebola"):
                    coin -= 50
                    bag.append("pokebola")
                    print("Você tem: $",coin,"\n")

            else:
                pass

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

        elif pcPokemon == 3:
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

        else:
            print("Você esta enfrentando um Bulbasauro Selvagem")
            print(''' 
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                        .
       ____      |___._.  |       __                 `.
     .'    `---""       ``"-.--"'`  '               .  
    .  ,            __               `              |   .
    `,'         ,-"'  .               '             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .' '   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / ' `        `.    .      .'/
 j|:D  '          `--'  ' ,'_  . .         `.__, '   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  """""'                    V
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) '`._        ___....----"'  ,'   .'  \ |   '     .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'' ____.___.'
 `"^--'..'   '-`-^-'"--    `-^-'`.''"""""`.,^.`.--' 
                 ''')
            pcokemon = ("Bulbasauro")
            

        print("--------------------------------------------------")

        if pcPokemon == select:
            print(f"Seu", pokemon, "empatou no combate ele será resolvido pelo nivel")
            if pcPokemon + pcPokeNivel > select + pokeNivelP:
                print(f"Você Perdeu seu", pokemon, "Desmaiou")
                death = True
                for i in range(6):
                    os.system('color c')
                    time.sleep(0.2)
                    os.system('color f')
                    time.sleep(0.2)

                if bag == []:
                  pass

                else:
                  bagO = input("Você quer abrir a mochila? sim ou não: ").lower()
                  if bagO == ("sim"):
                      print("Mochila:", bag)
                      rem = (input("Qual item você quer usar: "))
                      if rem == ("revive"):
                          bag.remove(rem)
                          print("Mochila:", bag)
                          death = False
                          break

                  elif bagO == ("s"):
                      print("Mochila:", bag)
                      rem = (input("Qual item você quer usar: "))
                      if rem == ("revive"):
                          bag.remove(rem)
                          print("Mochila:", bag)
                          death = False
                          break

                  elif bagO == ("não"):
                      break

                  else:
                      break

            else:
                print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
                pokeNivelP = pokeNivelP + 1
                print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
                continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                win = True
                coin += 15
            

        elif pcPokemon == 1 and select == 2:
            print(f"Você Perdeu seu", pokemon, "Desmaiou")
            death = True
            for i in range(6):
                os.system('color c')
                time.sleep(0.2)
                os.system('color f')
                time.sleep(0.2)

            if bag == []:
              pass

            else:
              bagO = input("Você quer abrir a mochila? sim ou não: ").lower()
              if bagO == ("sim"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      break

              elif bagO == ("s"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      break

              elif bagO == ("não"):
                  break

              else:
                  break

        elif pcPokemon == 1 and select == 3:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
            win = True
            coin += 15

        elif pcPokemon == 1 and select == 4:
            print(f"Você Perdeu seu", pokemon, "Desmaiou")
            death = True
            for i in range(6):
                os.system('color c')
                time.sleep(0.2)
                os.system('color f')
                time.sleep(0.2)

            if bag == []:
              pass

            else:
              bagO = input("Você quer abrir a mochila? sim ou não: ").lower()
              if bagO == ("sim"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      break

              elif bagO == ("s"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      break

              elif bagO == ("não"):
                  break

              else:
                  break

        elif pcPokemon == 2 and select == 1:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
            win = True
            coin += 15

        elif pcPokemon == 2 and select == 3:
            print(f"Você Perdeu seu", pokemon, "Desmaiou")
            death = True
            for i in range(6):
                os.system('color c')
                time.sleep(0.2)
                os.system('color f')
                time.sleep(0.2)

            if bag == []:
              pass

            else:
              bagO = input("Você quer abrir a mochila? sim ou não: ").lower()
              if bagO == ("sim"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      break

              elif bagO == ("s"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      break

              elif bagO == ("não"):
                  break

              else:
                  break

        elif pcPokemon == 2 and select == 4:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
            win = True
            coin += 15

        elif pcPokemon == 3 and select == 1:
            print(f"Você Perdeu seu", pokemon, "Desmaiou")
            death = True
            for i in range(6):
                os.system('color c')
                time.sleep(0.2)
                os.system('color f')
                time.sleep(0.2)

            if bag == []:
              pass

            else:
              bagO = input("Você quer abrir a mochila? sim ou não: ").lower()
              if bagO == ("sim"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      break

              elif bagO == ("s"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      break

              elif bagO == ("não"):
                  break

              else:
                  break

        elif pcPokemon == 3 and select == 2:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ").lower()
            win = True
            coin += 15

        elif pcPokemon == 3 and select == 4:
            print(f"Você Perdeu seu", pokemon, "Desmaiou")
            death = True
            for i in range(6):
                os.system('color c')
                time.sleep(0.2)
                os.system('color f')
                time.sleep(0.2)

            if bag == []:
                pass
            
            else:
                bagO = input("Você quer abrir a mochila? sim ou não: ").lower()
                if bagO == ("sim"):
                    print("Mochila:", bag)
                    rem = (input("Qual item você quer usar: "))
                    if rem == ("revive"):
                        bag.remove(rem)
                        print("Mochila:", bag)
                        death = False
                        break

                elif bagO == ("s"):
                    print("Mochila:", bag)
                    rem = (input("Qual item você quer usar: "))
                    if rem == ("revive"):
                        bag.remove(rem)
                        print("Mochila:", bag)
                        death = False
                        break

                elif bagO == ("não"):
                    break

                else:
                    break

        elif pcPokemon == 4 and select == 1:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ").lower()
            win = True
            coin += 15

        elif pcPokemon == 4 and select == 2:
            print(f"Você Perdeu seu", pokemon, "Desmaiou")
            death = True
            for i in range(6):
                os.system('color c')
                time.sleep(0.2)
                os.system('color f')
                time.sleep(0.2)

            if bag == []:
              pass

            else:
              bagO = input("Você quer abrir a mochila? sim ou não: ").lower()
              if bagO == ("sim"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      break

              elif bagO == ("s"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      break

              elif bagO == ("não"):
                  break

              else:
                  break

        elif pcPokemon == 4 and select == 3:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ").lower()
            win = True
            coin += 15


    if continuar == ("sim"):
      win = False

    elif continuar == ("s"):
        win = False

    elif continuar == ("não"):
      death = True

    else:
        death = True
