from random import *
import os
import time
import pokestats


os.system('cls')

select = int(input("Escolha seu Pokémon:\n 1 para Pikachu\n 2 para Squirtle\n 3 para Charmander\n 4 para Bulbasauro\n Digite a Escolha Aqui: "))
pokeNivelP = pokestats.level
global death
death = False
win = False
recovering = False
pokemon = ("")
pcokemon = ("")
continuar = ("")
bag = [ ]
coin = int(randrange(30,90))
bagO = ("")
merc = ("")
life = 0
superEfect = randrange(1,5)

print("--------------------------------------------------")

#Escolha de Pokémons

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


if select >= 5 or select < 1:
    select = randrange(1,4)


while (death == False):

    while(death == False and win == False):
        
        pcPokemon = int(randrange(1,5))
        chancedemerc = int(randrange(1,100))
        chancFuga = randrange(1,100)
        merc = False


        if pokeNivelP < 16:
            pcPokeNivel = int(randrange(0,14))

        elif pokeNivelP >= 16:
            pcPokeNivel = int(randrange(15,32))

#Spawn do Mercador

        while coin >= 15 and chancedemerc >= 60 and merc == False:
            print("--------------------------------------------------\n")
            print("-----------O Mercador está nas redonzas-----------\n")
            merc = input("Você quer comprar alguma coisa: ").lower()
            if merc == ("sim"):
                print(f"Você tem: $ {coin}\n")
                print("revive -> 30 golds")
                print("pokebola -> 50 golds")
                print("potion -> 15 golds")
                comprar = input("O que você quer comprar: ")
                if comprar == ("revive"):
                    if coin >= 30:
                        coin -= 30
                        bag.append("revive")
                        print(f"Você tem: $ {coin}\n")
                    else:
                        print("Você não tem dinheiro para comprar isso")

                elif comprar == ("pokebola"):
                    if coin >= 50:
                        coin -= 50
                        bag.append("pokebola")
                        print(f"Você tem: $ {coin}\n")
                    else:
                        print("Você não tem dinheiro para comprar isso")

                elif comprar == ("potion"):
                    if coin >= 15:
                        coin -= 15
                        bag.append("potion")
                        print(f"Você tem: $ {coin}\n")
                    else:
                        print("Você não tem dinheiro para comprar isso")

            elif merc == ("s"):
                print(f"Você tem: $ {coin}\n")
                print("revive -> 30 golds")
                print("pokebola -> 50 golds")
                print("potion -> 15 golds")
                comprar = input("O que você quer comprar: ")
                if comprar == ("revive"):
                    if coin >= 30:
                        coin -= 30
                        bag.append("revive")
                        print(f"Você tem: $ {coin}\n")
                    else:
                        print("Você não tem dinheiro para comprar isso")

                elif comprar == ("pokebola"):
                    if coin >= 50:
                        coin -= 50
                        bag.append("pokebola")
                        print(f"Você tem: $ {coin}\n")
                    else:
                        print("Você não tem dinheiro para comprar isso")

                elif comprar == ("potion"):
                    if coin >= 15:
                        coin -= 15
                        bag.append("potion")
                        print(f"Você tem: $ {coin}\n")
                    else:
                        print("Você não tem dinheiro para comprar isso")

            else:
                merc = True

        print("--------------------------------------------------\n")

#Configurações dos Pokémons

        if pcPokemon == 1:
            print("Você esta enfrentando um Pikachu Selvagem nível", pcPokeNivel)
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

            life = randrange(30, 50)
            tipo = "elétrico"


        elif pcPokemon == 11:
            print("Você esta enfrentando um Raichu Selvagem nível", pcPokeNivel)
            print(''' 
                                                                           :--                      
                                                                   =>]][%#<+:                       
                                                              =<[]*=)#<:                            
                                                          :>#> :=#][)                               
                                                        <]-  +}>:-}-                                
                                                     =]*  -]]-  +)                                  
                                                   =[=  +}<:   +)     -})=                          
  ]#%$%#})*-:                  ::=><]]]]<*-:     :[>  +#=     =<        )=<}=                       
     -<}+<}[>+)#]-         +[<=:           :=<[==[: =}=       [:         +> :<):                    
        +]=  =<]=-<}>:  =]>:                   <)  >]:       -)           =>   +<:                  
          +}-   -]>:-][]-                     -[  -[          *<-          -<    >>                 
           :[-    -#-<<                       :}=  *%[*-:::::::::>#*        -*    -[:               
            =+     >]>                  :*<}=   +]}]<>]}|]<+--::-**-<=       ->     <=              
           -[-    =[]:                  >>-}%-       ]+        :[*-)-*        ==     <>             
          >[:  -<}*-]   :               =%@@}:       -[         ]+-=)-:=:      <:     <*            
        :[]%[<**+++<> -}:)                    -#[[%<  <=               )>+}*    ]      }+           
        <<:+>-     ** +@%$+   ]#+        :*=:<:    :]+=*                )=  +[+ *-     :}-          
        )==+:}:    )- :)%<       -+>><))<)]:+=      :]:)                :]    :<]+      =]          
        :]])[<    -)--   :  :+]<-         [ =*      -) <-                =<              ]+         
                  *<  ++ >}#:      -]#)+=>}  *)    :]: -<                 >-             :}:        
         +][]))][]}-   ->  -}-  -[*:     -[    -++=:    ]                 ->              <=        
       *):     +<==<    <:  -}+*]:       >>             >:                 ]-              +*        
      :}=       *+ +<   >:    ][        :}:             +=   ::            >*              =<        
       :}=       )  :[=)*      >#:      *>              =[%[+  :*}:        *>              -]        
         -<}> ->:     +<        -}*    <[:            >#+:        >+       +<     +:       -]        
            -][+        =*        =[)>]+            =*:)]:        =<       ><    +]<<:     -|        
              :]*         ::                       *:  >]         ]*       ]=   -|  |]-    -/        
                -}:                                   -]         =#:      :<    )|   \ =  =|        
                +]%-  ]-                              +#)*-     -]:       <-   )/      \> )|        
            -<%@   @*]+                                   :)* :>*       :]*   >/        \[/         
          +%@ @%]-  ))                                    :-[]-        -[=  =/           -          
        +%@ @[:     >=      :=                           ::}@%)-    :))-  -#/                       
       )@ @[:       ]:   =}[}:[>[-                         [@@@@@@@)-  -)_/                         
      *@ @<      :>[<))=>]  ***+>+                         |: :+<]])<<+/                            
      ]@@%      =<     =}:    ::>=                         |                                        
      >@ @[:   -]       )       <=                        -|                                        
       >@   @#$%:      :)       )-                        *|                                        
        :>}@  @}       -)       <-                        [}\                                       
             =)[       :[       >-                       **+|                                       
              :)        [:      >-                         -|                                       
               <+       >:  )*]-*=                         -]                                       
                ]:      =+  ]:=**+                    ::   +|                                       
                :]:      )- +=->+*                  :<)    )|                                       
                  <*      ): ][+=>                 <]:    :}|                                       
                   -)*    ]<    -<              *]>:      +/                                        
                      +))>*#<   :]:      :=+<[]*         =[|                                        
                           :[<: -) -=++}):              +|/                                          
                             :*>+      [*#- >:        :]/                                           
                                       ]  +<]#[-    =]</                                            
                                       <-     -[<<<*/                                               
                                       =<     :-:<+                                                 
                                        <-  +> :)=]:                                                
                                        :[- -}>)>=:                 
                 ''')
            
            life = randrange(60, 100)
            tipo = "elétrico"


        elif pcPokemon == 2:
            print("Você esta enfrentando um Squirtle Selvagem nível", pcPokeNivel)
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
            
            life = randrange(30, 50)
            tipo = "água"


        elif pcPokemon == 12:
            print("Você esta enfrentando um Wartortle Selvagem nível", pcPokeNivel)
            print(''' 
     __                                _.--'"7
    `. `--._                        ,-'_,-  ,'
     ,'  `-.`-.                   /' .'    ,|
     `.     `. `-     __...___   /  /     - j
       `.     `  `.-""        " .  /       /
         \     /                ` /       /
          \   /                         ,'
          '._'_               ,-'       |
             | \            ,|  |   ...-'
             || `         ,|_|  |   | `             _..__
            /|| |          | |  |   |  \  _,_    .-"     `-.
           | '.-'          |_|_,' __!  | /|  |  /           '
   ,-...___ .=                  ._..'  /`.| ,`,.      _,.._ |
  |   |,.. \     '  `'        ____,  ,' `--','  |    /      |
 ,`-..'  _)  .`-..___,---'_...._/  .'      '-...'   |      /
'.__' ""'      `.,------'"'      ,/            ,     `.._.' `.
  `.             | `--........,-'.            .         \     '
    `-.          .   '.,--""     |           ,'\        |      .
       `.       /     |          L          ,\  .       |  .,---.
         `._   '      |           \        /  .  L      | /   __ `.
            `-.       |            `._   ,    l   .    j |   '  `. .
              |       |               `"' |  .    |   /  '      .' |
              |       |                   j  |    |  /  , `.__,'   |
              `.      L                 _.   `    j ,'-'           |
               |`"---..\._______,...,--' |   |   /|'      /        j
               '       |                 |   .  / |      '        /
                .      .              ____L   ''  j    -',       /
               / `.     .          _,"     \   | /  ,-','      ,'
              /    `.  ,'`-._     /         \  i'.,'_,'      .'
             .       `.      `-..'             |_,-'      _.'
             |         `._      |            ''/      _,-'
             |            '-..._\             `__,.--'
            ,'           ,' `-.._`.            .
           `.    __      |       "'`.          |
             `-"'  `""""'            7         `.
                                    `---'--.,'"`' 
                 ''')
            
            life = randrange(60, 100)
            tipo = "água"


        elif pcPokemon == 3:
            print("Você esta enfrentando um Charmander Selvagem nível", pcPokeNivel)
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

            life = randrange(30, 50)
            tipo = "fogo"


        elif pcPokemon == 13:
            print("Você esta enfrentando um Charmeleon Selvagem nível", pcPokeNivel)
            print(''' 
                      ,-'`'
                  _,"'    j
           __....+       /               .
       ,-'"             /               ; `-._.'.
      /                (              ,'       .'
     |            _.    \             \   ---._ `-.
     ,|    ,   _.'  Y    \             `- ,'   \   `.`.
     l'    \ ,'._,\ `.    .              /       ,--. l
  .,-        `._  |  |    |              \       _   l .
 /              `"--'    /              .'       ``. |  )
.\    ,                 |                .        \ `. '
`.                .     |                '._  __   ;. ''
  `-..--------...'       \                  `'  `-"'.  '
      `......___          `._                        |  '
               /`            `..                     |   .
              /|                `-.                  |    L
             / |               \   `._               .    |
           ,'  |,-"-.   .       .     `.            /     |
         ,'    |     '   \      |       `.         /      |
       ,'     /|       \  .     |         .       /       |
     ,'      / |        \  .    +          \    ,'       .'
    .       .  |         \ |     \          \_,'        / j
    |       |  L          `|      .          `        ,' '
    |    _. |   \          /      |           .     .' ,'
    |   /  `|    \        .       |  /        |   ,' .'
    |   ,-..\     -.     ,        | /         |,.' ,'
    `. |___,`    /  `.   /`.       '          |  .'
      '-`-'     j     ` /."7-..../|          ,`-'
                |        .'  / _/_|          .
                `,       `"'/"'    \          `.
                  `,       '.       `.         |
             __,.-'         `.        ''       |
            /_,-'\          ,'        |        _.
             |___.---.   ,-'        .-':,-"`\,' .
                  L,.--"'           '-' |  ,' `-..
                                        `.' 
                 ''')
            
            life = randrange(60, 100)
            tipo = "fogo"


        elif pcPokemon == 4:
            print("Você esta enfrentando um Bulbasauro Selvagem nível", pcPokeNivel)
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

            life = randrange(30, 50)
            tipo = "planta"


        elif pcPokemon == 14:
            print("Você esta enfrentando um Ivysaur Selvagem nível", pcPokeNivel)
            print(''' 
                               ,'"`.,./.
                             ,'        Y',"..
                           ,'           \  | '
                          /              . |  `
                         /               | |   '
            __          .                | |    .
       _   \  `. ---.   |                | j    |
      / `-._\   `Y   \  |                |.     |
     _`.    ``    \   \ |..              '      |,-'""7,....
     l     '-.     . , `|  | , |`. , ,  /,     ,'    '/   ,'_,.-.
     `-..     `-.  : :     |/ `   ' "\,' | _  /          '-'    /___
      '""' __.,.-`.: :        /   /._    l'.,'
       `--,   _.-' `".           /__ `'-.' '         .
       ,---..._,.--"""""""--.__..----,-.'   .  /    .'   ,.--
       |                          ,':| /    | /     ;.,-'--      ,.-
       |     .---.              .'  :|'     |/ ,.-='"-.`"`' _   -.'
       /    \    /               `. :|--.  _L,"---.._        "----'
     ,' `.   \ ,'           _,     `''   ``.-'       `-  -..___,'
    . ,.  .   `   __     .-'  _.-           `.     .__    '
    |. |`        "  ;   !   ,.  |             `.    `.`'---'
    ,| |C\       ` /    | ,' |(]|            -. |-..--`
   /  "'--'       '      /___|__]        `.  `- |`.
  .       ,'                   ,   /       .    `. '
    \                      .,-'  ,'         .     `-.
     x---..`.  -'  __..--'"/"""""  ,-.      |   |   |
    / \--._'-.,.--'     _`-    _. ' /       |     -.|
   ,   .   `-..__ ...--'  _,.-' | `   ,.-.  ;   /  '|
  .  _,'         '"-----""      |    `   | /  ,'    ;
  |-'  .-.    `._               |     `._// ,'     /
 _|    `-'   _,' "`--.._________|        `,'    _ /.
//\   ,-._.'"/\__,.   _,"     /_\__/`. /'.-.'.-/_,`-' 
`-"`"' v'    `"  `-`-"              `-'`-`  `'
                 ''')
            
            life = randrange(60, 100)
            tipo = "planta"
            

        print("--------------------------------------------------")

#Código para tentativa de fuga do combate

        fuga = input("Você quer fugir?: ").lower()
        if fuga == ("sim"):
            if chancFuga >= 60:
                print("Você conseguiu fugir")
                continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ").lower()
                break

            else:
                print("Você não conseguiu fugir")
                pass

        elif fuga == ("s"):
            if chancFuga >= 60:
                print("Você conseguiu fugir")
                continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ").lower()
                break

            else:
                print("Você não conseguiu fugir")
                pass

        elif fuga == ("não"):
            pass

        else:
            pass

        while win == False or recovering == False:

#Verificação de Quem Ganhou o Combate e Recuperação de seu Pokémon

            if pokestats.current_life == 0:
                if bag != []:
                    bagO = input("Você quer abrir a mochila? sim ou não: ").lower()
                    if bagO == ("sim"):
                        print("Mochila:", bag)
                        rem = input("Qual item você quer usar: ").lower()
                        if rem == ("revive"):
                            bag.remove(rem)
                            print("Mochila:", bag)
                            recovering = False
                            pokestats.current_life = pokestats.base_life + pokestats.bonus_life
                            time.sleep(1)

                        elif rem == ("potion"):
                            print("potion não pode ser usado em Pokémons desacordados\n")
                            print(f"Seu {pokemon} esta se recuperando do combate")
                            print("Aguarde enquanto seu pokémon se recupera")
                            recovering == True
                            time.sleep(15)
                            recovering == False
                            pokestats.current_life = pokestats.base_life + pokestats.bonus_life
                            break

                        else:
                            print(f"Seu {pokemon} esta se recuperando do combate")
                            print("Aguarde enquanto seu pokémon se recupera")
                            recovering == True
                            time.sleep(15)
                            recovering == False
                            pokestats.current_life = pokestats.base_life + pokestats.bonus_life
                            break
                            

                    elif bagO == ("s"):
                        print("Mochila:", bag)
                        rem = input("Qual item você quer usar: ").lower()
                        if rem == ("revive"):
                            bag.remove(rem)
                            print("Mochila:", bag)
                            recovering = False
                            pokestats.current_life = pokestats.base_life + pokestats.bonus_life
                            time.sleep(1)

                        elif rem == ("potion"):
                            print("potion não pode ser usado em Pokémons desacordados\n")
                            print(f"Seu {pokemon} esta se recuperando do combate")
                            print("Aguarde enquanto seu pokémon se recupera")
                            recovering == True
                            time.sleep(15)
                            recovering == False
                            pokestats.current_life = pokestats.base_life + pokestats.bonus_life
                            break

                        else:
                            print(f"Seu {pokemon} esta se recuperando do combate")
                            print("Aguarde enquanto seu pokémon se recupera")
                            recovering == True
                            time.sleep(15)
                            recovering == False
                            pokestats.current_life = pokestats.base_life + pokestats.bonus_life
                            break
                            

                    elif bagO == ("não"):
                        print(f"Seu {pokemon} esta se recuperando do combate")
                        print("Aguarde enquanto seu pokémon se recupera")
                        recovering == True
                        time.sleep(15)
                        recovering == False
                        pokestats.current_life = pokestats.base_life + pokestats.bonus_life
                        break

                    else:
                        print(f"Seu {pokemon} esta se recuperando do combate")
                        print("Aguarde enquanto seu pokémon se recupera")
                        recovering == True
                        time.sleep(15)
                        recovering == False
                        pokestats.current_life = pokestats.base_life + pokestats.bonus_life
                        break
                else:
                    print(f"Seu {pokemon} esta se recuperando do combate")
                    print("Aguarde enquanto seu pokémon se recupera")
                    recovering == True
                    time.sleep(15)
                    recovering == False
                    pokestats.current_life = pokestats.base_life + pokestats.bonus_life
                    break
                        

            if life <= 0:
                win = True
                coin += randrange(1,35)
                pokestats.update_exp(int(randrange(15,45)))
                print(f"Seu {pokemon} ganhou o combate")
                print(f"Ele esta no nível: {pokestats.level}")
                print(f"Com: {pokestats.current_xp} de experiência")
                for i in range(6):
                    os.system('color 2')
                    time.sleep(0.2)
                    os.system('color f')
                    time.sleep(0.2)
                continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ").lower()
                if continuar == ("sim"):
                    if bag != []:
                        bagO = input("Você quer abrir a mochila? sim ou não: ").lower()
                        if bagO == ("sim"):
                            print("Mochila:", bag)
                            rem = input("Qual item você quer usar: ").lower()
                            if rem == ("potion"):
                                bag.remove(rem)
                                print("Mochila:", bag)
                                pokestats.current_life + 10
                                time.sleep(1)
                                break
                            elif rem == ("revive"):
                                print("revive não pode ser utilizado em Pokémons que estão acordados")
                                break
                            else:
                                break

                        elif bagO == ("s"):
                            print("Mochila:", bag)
                            rem = input("Qual item você quer usar: ").lower()
                            if rem == ("potion"):
                                bag.remove(rem)
                                print("Mochila:", bag)
                                pokestats.current_life + 10
                                time.sleep(1)
                                break
                            elif rem == ("revive"):
                                print("revive não pode ser utilizado em Pokémons que estão acordados")
                                break
                            else:
                                break

                        elif bagO == ("não"):
                            break

                        else:
                            break

                    else:
                        break

                elif continuar == ("s"):
                    if bag != []:
                        bagO = input("Você quer abrir a mochila? sim ou não: ").lower()
                        if bagO == ("sim"):
                            print("Mochila:", bag)
                            rem = input("Qual item você quer usar: ").lower()
                            if rem == ("potion"):
                                bag.remove(rem)
                                print("Mochila:", bag)
                                pokestats.current_life + 10
                                time.sleep(1)
                                break
                            elif rem == ("revive"):
                                print("revive não pode ser utilizado em Pokémons que estão acordados")
                                break
                            else:
                                break

                        elif bagO == ("s"):
                            print("Mochila:", bag)
                            rem = input("Qual item você quer usar: ").lower()
                            if rem == ("potion"):
                                bag.remove(rem)
                                print("Mochila:", bag)
                                pokestats.current_life + 10
                                time.sleep(1)
                                break
                            elif rem == ("revive"):
                                print("revive não pode ser utilizado em Pokémons que estão acordados")
                                break
                            else:
                                break

                        elif bagO == ("não"):
                            break

                        else:
                            break

                    else:
                        break

                else:
                    break
                

#Os combates Acontecem aqui
            
            chancedeacerto = randrange(1,100)

            if chancedeacerto >= 30:
                pcdano = randrange(10,15 + pcPokeNivel)
                pokestats.update_healt(pcdano)
                print(f"Seu {pokemon} Tomou {pcdano} de Dano")
                print(f"Seu {pokemon} esta com {pokestats.current_life} de vida\n")
                for i in range(6):
                    os.system('color c')
                    time.sleep(0.2)
                    os.system('color f')
                    time.sleep(0.2)

            else:
                print(f"O {pcokemon} inimigo errou o ataque\n")

            chancedeplacert = randrange(1,100)

            if pokestats.current_life > 0:
                if chancedeplacert >= 30:
                    if select == pcPokemon:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 1 and pcPokemon == 2 or select == 11 and pcPokemon == 12:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 1 and pcPokemon == 3 or select == 11 and pcPokemon == 13:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 1 and pcPokemon == 4 or select == 11 and pcPokemon == 14:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 2 and pcPokemon == 1 or select == 12 and pcPokemon == 11:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 2 and pcPokemon == 3 or select == 12 and pcPokemon == 13:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 2 and pcPokemon == 4 or select == 12 and pcPokemon == 14:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 3 and pcPokemon == 1 or select == 13 and pcPokemon == 11:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 3 and pcPokemon == 2 or select == 13 and pcPokemon == 12:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 3 and pcPokemon == 4 or select == 13 and pcPokemon == 14:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 4 and pcPokemon == 1 or select == 14 and pcPokemon == 11:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 4 and pcPokemon == 2 or select == 14 and pcPokemon == 12:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP + superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                    elif select == 4 and pcPokemon == 3 or select == 14 and pcPokemon == 13:
                        print("Seu Pokémon vai atacar")
                        if pokestats.level < 4:
                            dano = randrange(8,13 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 8:
                            dano = randrange(10,15 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 12:
                            dano = randrange(12,17 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        elif pokestats.level < 16:
                            dano = randrange(14,19 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")
                        else:
                            dano = randrange(16,21 + pokeNivelP - superEfect)
                            life -= dano
                            if life < 0:
                                life = 0
                            print(f"O {pcokemon} inimigo tomou {dano} de dano ele esta com {life} de vida\n")

                else:
                    print(f"Seu {pokemon} errou o ataque\n")
            else:
                pass


#Verificação de Continuidade para o Game

    if continuar == ("sim"):
        win = False

    elif continuar == ("s"):
        win = False

    elif continuar == ("não"):
        death = True

    else:
        death = True

#Sistema de Evolução dos Pokémons

    if pokeNivelP == 16:
        os.system('cls')
        pokeNivelP = 17

        for eve in range(9):
            if eve == 0:
                print("Seu", pokemon, "está evoluindo.")
                time.sleep(0.5)
                os.system('cls')
            elif eve == 1:
                print("Seu", pokemon, "está evoluindo..")
                time.sleep(0.5)
                os.system('cls')
            elif eve == 2:
                print("Seu", pokemon, "está evoluindo...")
                time.sleep(0.5)
                os.system('cls')
            elif eve == 3:
                print("Seu", pokemon, "está evoluindo.")
                time.sleep(0.5)
                os.system('cls')
            elif eve == 4:
                print("Seu", pokemon, "está evoluindo..")
                time.sleep(0.5)
                os.system('cls')
            elif eve == 5:
                print("Seu", pokemon, "está evoluindo...")
                time.sleep(0.5)
                os.system('cls')
            elif eve == 6:
                print("Seu", pokemon, "está evoluindo.")
                time.sleep(0.5)
                os.system('cls')
            elif eve == 7:
                print("Seu", pokemon, "está evoluindo..")
                time.sleep(0.5)
                os.system('cls')
            else:
                print("Seu", pokemon, "está evoluindo...")
                time.sleep(0.5)
                os.system('cls')

        if select == 1: 
            pokemon = ("Raichu")
            print("Agora seu pokémon é um", pokemon)
            if select == 1:
                select = 11

        elif select == 2:
            pokemon = ("Wartortle")
            print("Agora seu pokémon é um", pokemon)
            if select == 2:
                select = 12

        elif select == 3:
            pokemon = ("Charmeleon")
            print("Agora seu pokémon é um", pokemon)
            if select == 3:
                select = 13

        elif select == 4:
            pokemon = ("Ivysaur")
            print("Agora seu pokémon é um", pokemon)
            if select == 4:
                select = 14

    if pcPokeNivel >= 16:
        if pcPokemon == 1: 
            pcokemon = ("Raichu")
            pcPokemon = 11

        elif pcPokemon == 2:
            pcokemon = ("Wartortle")
            pcPokemon = 12

        elif pcPokemon == 3:
            pcokemon = ("Charmeleon")
            pcPokemon = 13

        elif pcPokemon == 4:
            pcokemon = ("Ivysaur")
            pcPokemon = 14
