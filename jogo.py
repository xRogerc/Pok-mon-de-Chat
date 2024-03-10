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


if select >= 5:
    select = 4


while (death == False):


    while(death == False and win == False):
        
        pcPokemon = int(randrange(1,5))
        chancedemerc = int(randrange(1,100))
        chancFuga = randrange(1,100)


        if pokeNivelP < 16:
            pcPokeNivel = int(randrange(0,14))

        elif pokeNivelP >= 16:
            pcPokeNivel = int(randrange(15,32))

        if coin < 30:
            pass

        else:
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
            fuga = input("Você quer fugir do combate?: ")
            if fuga == ("sim"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("s"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("não"):
                pass

            else:
                pass

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
            fuga = input("Você quer fugir?: ")
            if fuga == ("sim"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("s"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("não"):
                pass

            else:
                pass

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
            fuga = input("Você quer fugir?: ")
            if fuga == ("sim"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("s"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("não"):
                pass

            else:
                pass

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
            fuga = input("Você quer fugir?: ")
            if fuga == ("sim"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("s"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("não"):
                pass

            else:
                pass

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
            fuga = input("Você quer fugir?: ")
            if fuga == ("sim"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("s"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("não"):
                pass

            else:
                pass

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
            fuga = input("Você quer fugir?: ")
            if fuga == ("sim"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("s"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("não"):
                pass

            else:
                pass

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
            fuga = input("Você quer fugir?: ")
            if fuga == ("sim"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("s"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("não"):
                pass

            else:
                pass

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
            fuga = input("Você quer fugir?: ")
            if fuga == ("sim"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("s"):
                if chancFuga >= 65:
                    continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
                    break

                else:
                    print("Você não conseguiu fugir")
                    pass

            elif fuga == ("não"):
                pass

            else:
                pass
            

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
                          time.sleep(1)
                          break

                  elif bagO == ("s"):
                      print("Mochila:", bag)
                      rem = (input("Qual item você quer usar: "))
                      if rem == ("revive"):
                          bag.remove(rem)
                          print("Mochila:", bag)
                          death = False
                          time.sleep(1)
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
            

        elif pcPokemon == 1 and select == 2 or pcPokemon == 11 and select == 12:
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
                      time.sleep(1)
                      break

              elif bagO == ("s"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      time.sleep(1)
                      break

              elif bagO == ("não"):
                  break

              else:
                  break

        elif pcPokemon == 1 and select == 3 or pcPokemon == 11 and select == 13:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
            win = True
            coin += 15

        elif pcPokemon == 1 and select == 4 or pcPokemon == 11 and select == 14:
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
                      time.sleep(1)
                      break

              elif bagO == ("s"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      time.sleep(1)
                      break

              elif bagO == ("não"):
                  break

              else:
                  break

        elif pcPokemon == 2 and select == 1 or pcPokemon == 12 and select == 11:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
            win = True
            coin += 15

        elif pcPokemon == 2 and select == 3 or pcPokemon == 12 and select == 13:
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
                      time.sleep(1)
                      break

              elif bagO == ("s"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      time.sleep(1)
                      break

              elif bagO == ("não"):
                  break

              else:
                  break

        elif pcPokemon == 2 and select == 4 or pcPokemon == 12 and select == 14:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ")
            win = True
            coin += 15

        elif pcPokemon == 3 and select == 1 or pcPokemon == 13 and select == 11:
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
                      time.sleep(1)
                      break

              elif bagO == ("s"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      time.sleep(1)
                      break

              elif bagO == ("não"):
                  break

              else:
                  break

        elif pcPokemon == 3 and select == 2 or pcPokemon == 13 and select == 12:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ").lower()
            win = True
            coin += 15

        elif pcPokemon == 3 and select == 4 or pcPokemon == 13 and select == 14:
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
                        time.sleep(1)
                        break

                elif bagO == ("s"):
                    print("Mochila:", bag)
                    rem = (input("Qual item você quer usar: "))
                    if rem == ("revive"):
                        bag.remove(rem)
                        print("Mochila:", bag)
                        death = False
                        time.sleep(1)
                        break

                elif bagO == ("não"):
                    break

                else:
                    break

        elif pcPokemon == 4 and select == 1 or pcPokemon == 14 and select == 11:
            print(f"Você Ganhou seu", pokemon, "Subiu de Nivel")
            pokeNivelP = pokeNivelP + 1
            print(f"Esse é o Nivel de seu", pokemon, pokeNivelP)
            continuar = input("Digite Sim para Continuar e Não para Encerrar o Jogo: ").lower()
            win = True
            coin += 15

        elif pcPokemon == 4 and select == 2 or pcPokemon == 14 and select == 12:
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
                      time.sleep(1)
                      break

              elif bagO == ("s"):
                  print("Mochila:", bag)
                  rem = (input("Qual item você quer usar: "))
                  if rem == ("revive"):
                      bag.remove(rem)
                      print("Mochila:", bag)
                      death = False
                      time.sleep(1)
                      break

              elif bagO == ("não"):
                  break

              else:
                  break

        elif pcPokemon == 4 and select == 3 or pcPokemon == 14 and select == 13:
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
