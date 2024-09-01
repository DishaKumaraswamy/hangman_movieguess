import random

print('''
 _
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                       ''')



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



word_lists = ["riverdale", "maxtonhall", "onepiece", "glory", "gameofthrones", "twilight", "eclipse", "newmoon", "neverhaveiever", "strangerthings", "theboys", "gilmoregirls",
              "chemicalhearts", "purplehearts", "dark", "emilyinparis", "moneyhiest", "peakyblinders", "squidgame", "schindlerslist", "casanova", "passengers", "friends", "suits", "you",
              "wednesday", "dexter", "bridgerton", "ginnyandgeorgia", "lordoftherings", "littlewomen", "spiderman", "superman", "xmen","batman", "alladin", "tinkerbell","toystory","gossipgirl",
              "manifest", "bigbangtheory", "houseofdragon", "notebook", "breakingbad", "thevampirediaries", "bambi", "beautyandthebeast", "iceage", "ghostbusters", "jamesbond",
              "lionking", "other", "peterpan", "pinnochio", "pocahontas", "reddwarf", "shrek", "snowwhite", "spacewalls", "starwars", "wallaceandgromit" , "littlemermaid",
              "inception", "ghostrider", "pulpfiction", "thematrix", "thegodfather", "thedarkknight", "forrestgump", "lalaland", "interstellar", "seven", "gladiator", "dune",
              "whiplash", "casablanca",  "Oppenheimer", "jurassicpark" ]


chosen_word = random.choice(word_lists)


placeholder = ""
word_length = len(chosen_word)
for i in range(word_length):
    placeholder += "_"
print(placeholder)

lives = 6

game_over = False
correct_letters = []

while not game_over :
 
    print(f"--------------------{lives}/6 lives left--------------------")
 
    guess = input("Enter a letter").lower()

    display = ""

    if guess in correct_letters :
        print("You've already guessed the letter! ") 

    for i in chosen_word :

        if i == guess:
            display += i
            correct_letters.append(guess)

        elif i in correct_letters:
            display += i
                    
        else :
            display += "_"
                

    print(display)

    if guess not in chosen_word :
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
            print("It was " + chosen_word)
        if chosen_word == "riverdale" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''
                                
                           _,..._  ,d$$ccc_
                          d$$$$$$hc$$$$$$$$h.
                        ,d$$$$$$$$$$$$$$$O$$$.
                       ,$$$$h$$$$$FF$$$$$$$$$|
                      ,d$$$$$h$$F;' `F$$;':?$'
                      d$$F?$$$F'      ',c. +'
                     d$$h     c$$h    $$$$'|
                    d$$$h    $$F'     `' ' |
                    $$$$$L   `',-.    ,`.  |
                    $$$$$$h   .'  `      | |
                    d$$$$$$   |        O ' `.
                     $$$$$F   | O  , __. , | |
                      Y$FF'      ,' '  )"  |_|
                      ;"'      "'   __/    |'
                     |,`.        /      ,  |
                     |  |      .'`--..-'   |
                     `. `       (.___,/    |
                       `._,.     \   .'   |
                            \     \_,'    |
                             \           /
                              `.        /
                                `-....-'

                      ''')

                
        elif chosen_word == "spiderman" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''                                                                         
                                   z@d                               
                                    0@@.                z@.          
                                   z1jd01j".          j11j           
                                  110jd@z@000@jjjjjz@1jd.            
                                zj@j @jd    "zzzzzj@0dz0             
                            "zj@d@.   00z       .jjd1 @@             
                    .zzzz"zjj00@1z.   .111@01jz".zj10.110            
         """j1j1jzzz10j11z""      .zj@0@0@j1j@1@1@j   .@1@           
             .j@@""j1000@11111111@0@11@1j@00@@@01@0     1d0"         
              "@d.     jjd11@0@@dd@1@dd1jd0@1d0@zj10z    z@@0z       
               z00      00"   @1d110@d0@0@1@@j@j0@1@d@11111@1@@111@@@
                1@j     j0.   "@d   "j0@01j0jjjd1@@dddjzzzzz0@dj"    
                j@@     j0.   11d"j10@@@1d@1dz10?zz00.     z@0j      
                j@d"   z?0. .j@100@j   j11 jj0?@1"@d"     .@@"       
                z01   z1@jj@@d@1.     "@0z  "z1@0d1j      011        
               1z0. "@0d@@@110z"      d@d    .@j@d0j     j1@         
              0@0 .j@1jjj"  "zj@11"  .d?zzj10@@@0@jd     0@z         
            "??d1j@@0@1.       .z@@010@00@1".    @@@0.   @d          
           1@000@11j100dd0@11z.    z1@d0111@01111j0@0d   @d          
        .j@0@?0@zzz.      "zz@d1"   1ddd0@""""""zzj@00d. d?          
     zj0d011111jzj0000@11z.   z0d0" 0z10.           .100"0dj         
                      .zz10@1   "0d?zj1               j@dd@@         
                          z10dj   00@1    ..zj"1@zzzj".j@000z        
                            zdd@  11@  "z001jjjjjjzzj1100111d        
                             .1??j0@1z0d@.               zzzj@       
                               j?d1010@.                   .1@@"     
                                jz00j                        jd?"    
                                jj@                              
                               .11j                              
                                       ''')

                
        elif  chosen_word == "superman" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''

                                  ________________
                                 /.,------------,.\
                                ///  .=^^^^^^^\__|\\
                                \\\   `------.   .//
                                 `\\`--...._  `;//'
                                   `\\.-,___;.//'
                                     `\\-..-//'
                                       `\\//'
                                         ""

                      ''')
                

        elif chosen_word == "batman" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''          _,    _   _    ,_
                              .o888P     Y8o8Y     Y888o.
                             d88888      88888      88888b
                            d888888b_  _d88888b_  _d888888b
                            8888888888888888888888888888888
                            8888888888888888888888888888888
                            YJGS8P"Y888P"Y888P"Y888P"Y8888P
                             Y888   '8'   Y8P   '8'   888Y
                              '8o          V          o8'
                                `                     `
                     ''')
                

        elif chosen_word == "alladin" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''
                                    _.---.__
                                  .'        `-.
                                 /      .--.   |
                                 \/  / /    |_/
                                  `\/|/    _(_)
                               ___  /|_.--'    `.   .
                               \  `--' .---.     \ /|
                                )   `       \     //|
                                | __    __   |   '/||
                                |/  \  /  \      / ||
                                ||  |  |   \     \  |
                                \|  |  |   /        |
                               __\\@/  |@ | ___ \--'
                              (     /' `--'  __)|
                             __>   (  .  .--' &"\
                            /   `--|_/--'     &  |
                            |                 #. |
                            |                 q# |
                             \              ,ad#'
                              `.________.ad####'
                                `#####""""""''
                                 `&#"
                                  &# "&
                                  "#ba"

                                  ''')

        
        elif chosen_word == "toystory" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print(''' 
                                      O
                             _|_
                       ,_.-_' _ '_-._,
                        \ (')(.)(') /
                     _,  `\_-===-_/`  ,_
                    >  |----"""""----|  <
                    `""`--/   _-@-\--`""`
                         |===L_I===|
                          \       /
                          _\__|__/_
                     jgs `""""`""""`

                     ''')
                

        elif chosen_word == "wallaceandgromit" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''

                                    __
                                   /  \     ,    ,
                         _._     _ |oo| _  / \__/ \
                        _||||   ((/ () \))   /  \
                        |||||/|  ('====')    |oo|
                         \____/  _`\  /'_    /  \
                         /   /.-' /\<>/\ `\.( () )_._
                         |    `  /  \/  \  /`'--'////)
                          \__,-'`|  |.  |\/ |/^^\|"\"` 
                             jgs |  |.  | \___/\___/
                ''')
                

        elif chosen_word == "iceage" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''

                                                         .-.
                                                        |/`\\.._
                                     _..._,,--.         `\ /.--.\ _.-. 
                                  ,/'  ..:::.. \     .._.-'/    \` .\/ 
                                 /       ...:::.`\ ,/:..| |(o)  / /o)|
                                |:..   |  ..:::::'|:..  ;\ `---'. `--'
                                ;::... |   .::::,/:..    .`--.   .:.`\_
                                 |::.. ;  ..::'/:..   .--'    ;\   :::.`\
                                 ;::../   ..::|::.  /'          ;.  ':'.---.
                                  `--|    ..::;\:.  `\,,,____,,,/';\. (_)  |)
                                     ;     ..::/:\:.`\|         ,__,/`;----'
                                     `\       ;:.. \: `-..      `-._,/,_,/
                                       \      ;:.   ). `\ `>     _:\
                                        `\,  ;:..    \ \ _>     >'

                                        ''')

                
        elif chosen_word == "jamesbond" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''            .-.  .-.  --..::==
                                    (   )(   )  //"
                                     '-'  '-'  /

                                     ''')

                
        elif chosen_word == "littlemermaid" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''   


                              , __
                                \`\\"._     _,
                                / _  |||;._/ )
                              _/@ @  ///  | (
                             ( (`__,     ,`\|
                              '.\_/ |\_.'
                        jgs     `""```


                ''')

        elif chosen_word == "peterpan" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''


                                            __
                                            ",'.
                                              ",\
                                              / Y
                             ,             _,'--.\
                             \_-(         ;--(/\ )
                               \'.         )6,6 /)
                                \ \_       \ _, |_
                                 ', '--/'---'- /_/'-._
                                   '-'-L._  -|/      /-._     /
                                          |      |-~'--._'-._/(,
                                         ,_/>   /         ''--~
                                         /\<_ _/
                                        // "-'-'\
                                       ,~-.   ._ )
                                       /   \_/  '\
                                      /   /   \   |
                                     /  /`    _\  |
                                    ( ,/  _.-' __.'
                                   / /  [((---'
                                  / /   ) )
                                 / /    \/
                                K=/
                        snd    / _>
                              )_/


                          ''')


        
        elif chosen_word == "starwars" :
            hint= input("Need hint? y/n ").lower()
            if hint == 'y':
                print('''


                                __.-._
                                '-._"7'
                                 /'.-c
                                 |  /T
                            snd _)_/LI

                            ''')

                        

    if "_" not in display :
        game_over = True
        print("You win!")
        

    print(stages[lives])



