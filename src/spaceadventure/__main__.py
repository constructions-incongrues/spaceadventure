from asciimatics.event import KeyboardEvent
from asciimatics.effects import Stars, Cycle, Print
from asciimatics.exceptions import NextScene, ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.renderers import FigletText, SpeechBubble
from frame import SpaceAdventureFrame
import transition
import sys

def _unhandled_input(event):
    if (event is not None and isinstance(event, KeyboardEvent) and event.key_code == 10):
        raise NextScene
    else:
        return event

def title(screen):
    effects = [
        Cycle(
            screen,
            FigletText("OPERATION", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("EDENA", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, screen.width),
        Print(screen,
              SpeechBubble("Press space to see it again"),
              y=screen.height - 3,
              start_frame=300)
    ]

    return Scene(effects, -1)

def run(screen, scene):
    scenes = [
        # title
        transition.noise(screen, duration=10),
        title(screen),

        # 01
        Scene([
            SpaceAdventureFrame(
                screen,
                image=r'''
                         _______________________
                       //   __..--~~~~--..__    \\
                      ||___/  |  |   |  |   \ __/ |
                      ||  /   ___________    \    |
                      ||_/   /.......... \    |   |
                      | |   /..........   \   |   |
 _____________________| |  /...........    \  |   |________________
  ;   . . .   .       |_| |...........      | |   | .''."...  ... .
 ___   ..~.         _.' | |..........       | |   |         . ~
  .      '     .   / \_.| |..........       | |   |\ ~.   ._..---._
                  |. /| \ \............     / /   |/ .    /\      /\
    '... ... ~~~  | \|| _\ \............   / /-.__|      // ~-._./ -\
  ..~             |  |_.~\\ \_____________/ /// '.|     /__       __.\
  ___   ..~.      |_.~   .\\_______________//   _ ~-.  ~~~~..  ~~~~~.
                 .~ -.     \__.---.________/   ______\.
 .''."...  ... ./\        _|      |---|  = |__ \__\===\   '"""     ~~~
               /  '.  .  |_|=     |---|    | _| \======\ ___   ..~.
   ..~        / .   \      |=     |___|    ||       __. \
             /           _ |_______________|   _.        \
 .''."...  ./                /   \___    ~~  \            \  '" ..   ~~
           /          '' /   \      /         \           /\
 ___   .  /     -- .   /'   __\____/       ____\___.'   --  \ ___   ..~.
         /            /    / \\ --  _____//          ~ - .   \
  ..--  /_..-       ./.   /  _/   _|___  \\       .     -   _/)
       /   ___     ./|__  / _/   (_____ / \\  .          \ ~ /   .
   .  /___////_   /  |   / _/    (_____ \  \\       _./ ..__/
     /___/__/_ \ /  _|  /__/ _-- (_____  \:_\\_____________/      ._
 _  /         \ /_.' | /  /       (_________/ ~~-|
                ''',
                message="""
Salut inconnu.e, soit le bienvenu dans le jeu Space Adventure.
Nous comptons sur ton courage, ta coopération et ta réfléxion pour avancer dans les différentes quêtes.
Je vois que tu es prêt à relever ce défi.

> Quel est ton nom, cosmonaute ?
                """,
                answers=["jimmy"]
            ),
            Stars(screen, screen.width)
        ]),
        transition.noise(screen, duration=5),

        # 02
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""

     .  . '    .
      '   .            . '            .                +
              `                          '    . '
        .                         ,'`.                         .
   .                  .."    _.-;'    `.              .
              _.-"`.##%"_.--" ,'        `.           "#"     ___,,od000
           ,'"-_ _.-.--"\   ,'            `-_       '%#%',,/////00000HH
         ,'     |_.'     )`/-     __..--""`-_`-._    J L/////00000HHHHM
 . +   ,'   _.-"        / /   _-""           `-._`-_/___\///0000HHHHMMM
     .'_.-""      '    :_/_.-'                 _,`-/__V__\0000HHHHHMMMM
 . _-""                         .        '   _,////\  |  /000HHHHHMMMMM
_-"   .       '  +  .              .        ,//////0\ | /00HHHHHHHMMMMM
       `                                   ,//////000\|/00HHHHHHHMMMMMM
.             '       .  ' .   .       '  ,//////00000|00HHHHHHHHMMMMMM
     .             .    .    '           ,//////000000|00HHHHHHHMMMMMMM
                  .  '      .       .   ,///////000000|0HHHHHHHHMMMMMMM
  '             '        .    '         ///////000000000HHHHHHHHMMMMMMM
                    +  .  . '    .     ,///////000000000HHHHHHHMMMMMMMM
     '      .              '   .       ///////000000000HHHHHHHHMMMMMMMM
   '                  . '              ///////000000000HHHHHHHHMMMMMMMM
                           .   '      ,///////000000000HHHHHHHHMMMMMMMM
       +         .        '   .    .  ////////000000000HHHHHHHHMMMMMMhs
                """,
                message="""
Au-dessus de votre planète se dessine l'ombre inquiétante d'un vaisseau spatial.

> Quel est son matricule ?
> X-Wing | NCC-1701-J | Odysseus | Ariane | Enterprise | Arwing | Vandervecken | Nebuchadnezzar
                """,
                answers=["vandervecken"]
            ),
            Stars(screen, screen.width)
        ]),
        transition.noise(screen, duration=5),

        # 02
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
                        .-.      .-.
                  _..--'`;;`-..-';;'`--.._
                .';,    _   `;;'   _    ,;`.
               ;;'  `;;' `;.`;;'.;' `;;'  `;;
              .;;._.;'`;.   `;;'   .;'`;._.;;.
            ;'      '`;;`   `;;'   ';;'`      `;
           ;:     .:.  `;;. `--' .;;'  .:.     :;
            ;.   .:|:.     `;;;;'     .:|:.   .;
             `;  `:|:'    .;;'`;;.    `:|:'  ;'
              `;. `:'  .;;'.::::.`;;.  `:' .;'
                `;._.;;' .:`::::':. `;;._.;'
           .::::. `::   (:._.::._.:)   ::' .::::.
      .:::::'  `::.`:_.--.`:::::. .--._:'.::'  `:::::.
    .::'     `:.    `::-.:::....:::.-::'   `::      `::.
  .::'      .::'      | /.^^^..^^^.\ |      `::        `:.
  :::      .:'::.     \( `;;;..;;;' )/     .::::       :::
  ::  :  .:':.  `::.   \            /   .::'  .:     .  ::
  :  ::  .   :     `::.              .::'     :  :   ::  :
                """,
                message="""
À son bord, le savant dément, se prépare à soumettre à ses effroyables expériences.

> Découvre l'identité du commandant et communique son nom à ton équipage.
                """,
                answers=["cyrus"]
            ),
            Stars(screen, screen.width)
        ]),
        transition.noise(screen, duration=5),

        # 03
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
              .+.
          _.-//_\\-._
        .'.-' XII '-.'.
      /`.'*         *'.`\\
     / /*        /    *\\ \\
    | ;        _/       ; |
    | |IX     (_)    III| |
    | ;         \       ; |
     \ \*        \    */ /
      \ '.*       \ *.'./
       '._'-.__VI_.-'_.'
          '-.,___,.-'
                """,
                message="""
ll n'y a plus un instant à perdre !
Les autorités ont fait appel à la Guilde des Mercenaires de l'espace
pour mettre un terme aux sombres machinations de Cyrus

> Souhaites-tu intégrer la Guilde des Mercenaires ?
                """,
                answers=["oui"]
            ),
            Stars(screen, screen.width)
        ]),

        # 04
        Scene([
            SpaceAdventureFrame(
                screen,
                image=r'''
                           __.--|~|--.__                              ,,;/;
                         /~     | |    ;~\                          ,;;;/;;'
                        /|      | |    ;~\\                      ,;;;;/;;;'
                       |/|      \_/   ;;;|\                    ,;;;;/;;;;'
                       |/ \          ;;;/  )                 ,;;;;/;;;;;'
                   ___ | ______     ;_____ |___....__      ,;;;;/;;;;;'
             ___.-~ \\(| \  \.\ \__/ /./ /:|)~   ~   \   ,;;;;/;;;;;'
         /~~~    ~\    |  ~-.     |   .-~: |//  _.-~~--,;;;;/;;;;;'
        (.-~___     \.'|    | /-.__.-\|::::| //~     ,;;;;/;;;;;'
        /      ~~--._ \|   /          `\:: |/      ,;;;;/;;;;;'
     .-|             ~~|   |  /V....V\ |:  |     ,;;;;/;;;;;' \
    /                   \  |  ~`^~~^'~ |  /    ,;;;;/;;;;;'    ;
   (        \             \|`\._____./'|/    ,;;;;/;;;;;'      '\
  / \        \                             ,;;;;/;;;;;'     /    |
 |            |                          ,;;;;/;;;;;'      |     |
|`-._          |                       ,;;;;/;;;;;'              \
|             /                      ,;;;;/;;;;;'  \              \__________
(             )                 |  ,;;;;/;;;;;'      |        _.--~
 \          \/ \              ,  ;;;;;/;;;;;'       /(     .-~_..--~~~~~~~~~~
 \__         '  `       ,     ,;;;;;/;;;;;'    .   /  \   / /~
 /          \'  |`._______ ,;;;;;;/;;;;;;'    /   :    \/'/'       /|_/|   ``|
| _.-~~~~-._ |   \ __   .,;;;;;;/;;;;;;' ~~~~'   .'    | |       /~ (/\/    ||
/~ _.-~~~-._\    /~/   ;;;;;;;/;;;;;;;'          |    | |       / ~/_-'|-   /|
(/~         \| /' |   ;;;;;;/;;;;;;;;            ;   | |       (.-~;  /-   / |
|            /___ `-,;;;;;/;;;;;;;;'            |   | |      ,/)  /  /-   /  |
                ''',
                message="""
Félicitation !
Tu es dorénavant un "Mercenaire de l'espace".
Tu vas devoir t'introduire dans le Vandervecken.
Pour y affronter Cyrus et les créatures qui le protègent.

> Quel équipement choisiras-tu pour t'aider dans ta mission ?

                """,
                answers=False
            ),
            Stars(screen, screen.width)
        ]),

        # 05
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
      ______                  ______
   ,-' ;  ! `-.            ,-' ;  ! `-.
  / :  !  :  . \\          / :  !  :  . \\
 |_ ;   __:  ;  |        |_ ;   __:  ;  |
 )| .  :)(.  !  |        )| .  :)(.  !  |
 |"   (NOIRE)_  |        |"  (BLANCHE)_ |
 |  :  ;`'  (_) (        |  :  ;`'  (_) (
 |  :  :  .     |        |  :  :  .     |
 )_ !  ,  ;  ;  |        )_ !  ,  ;  ;  |
 || .  .  :  :  |        || .  .  :  :  |
 |" .  |  :  .  |        |" .  |  :  .  |
 |_____;----.___|        |_____;----.___|

                """,
                message="""
Tu arpentes la coursive et découvre deux portes. 
L'une est noire, comme on en voit au plus profond des galaxies.
L'autre brille d'un blanc éclatant, presque aveuglant..

> De quelle couleur est la porte que tu décides d'ouvrir ?
                """,
                answers=["noire", "blanche"]
            ),
            Stars(screen, screen.width)
        ]),

        # 06
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
   -. -. `.  / .-' _.'  _
     .--`. `. `| / __.-- _' `
    '.-.  \\  \\ |  /   _.' `_
    .-. \\  `  || |  .' _.-' `.
  .' _ \\ '  -    -'  - ` _.-.
   .' `. %%%%%   | %%%%% _.-.`-
 .' .-. ><(@)> ) ( <(@)>< .-.`.
   (("`(   -   | |   -   )'"))
  / \\\\#)\\    (.(_).)    /(#//\\
 ' / ) ((  /   | |   \\  )) (`.`.
 .'  (.) \\ .md88o88bm. / (.) \\)
   / /| / \\ `Y88888Y' / \\ | \\ \\
 .' / O  / `.   -   .' \\  O \\ \\\\
  / /(O)/ /| `.___.' | \\\\(O) \\
   / / / / |  |   |  |\\  \\  \\ \\
   / / // /|  |   |  |  \\  \\ \\  VK
 _.--/--/'( ) ) ( ) ) )`\\-\\-\\-._
( ( ( ) ( ) ) ( ) ) ( ) ) ) ( ) ) """,
                message="""
La porte s'ouvre, Cyrus est aux commandes de la console de pilotage.
Il te tourne le dos et n'a pas l'air d'avoir remarqué ta présence.
C'est l'occasion rêvée pour l'estourbir sans effort !
Tu t'approches discrètement du fauteuil où est assez confortablement... UN MANNEQUIN !
C'était un piège, Cyrus surgit d'une encoignure et te désarme.
Il ne te reste plus qu'une chance : envoyer un message d'urgence depuis le transmetteur
interplanétaire caché dans ta botte gauche à la seule personne en mesure de te sauver la mise.

> Comment s'appelle cette personne ?

                                """,
                answers=["james"]
            ),
            Stars(screen, screen.width)
        ]),

        # 06
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
             ________________________________________________
            /                                                \\
           |    _________________________________________     |
           |   |                                         |    |
           |   |  ? spaceshipctl open vandervecken       |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \\_________________________________________________/
                   \\___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
                """,
                message="""
Voilà déjà presque neuf nanosecondes que ton appel de détresse est parti et James n'est toujours pas là !
T'aurait-il oublié ?
Cela n'a plus d'importance : dans moins d'une nanosecondes il en sera fini de toi et de toute l'Humanité.
Alors que Cyrus s'apprête à te porter un coup fatal, un bourdonnement terrible enfle dans la cabine et tout d'un coup
ce sont tous les écrans de contrôles de la pièce qui diffusent la même image : celle de James le Cyber-Mercenaire riant aux éclats.
Il semble te faire un clin d'œil puis enfonce la touche entrée de son clavier, ouvrant ainsi le sas de décompression de la cabine.
Tes réflexes de Mercenaire de l'Espace te permettent de sauter hors de la cabine à temps pour voir Cyrus aspiré vers son dernier
voyage à travers les étoiles.

> Quelle est la commande qui t'a sauvé ?

                                """,
                answers=["spaceshipctl open vandervecken"]
            ),
            Stars(screen, screen.width)
        ]),

        # 07
        transition.fireworks(screen, duration=300),

        # 08
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
          .                                            .
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
        o                             .                   .
         .              .                .
          0     .                  Programmation: Tristan et Vincent
                 .          .      Création : Maison JOLU            ,                ,    ,
 .          \\          .          D'après un livre dont vous êtes le héros
      .      \\   ,                Le mercenaire de l'espace de Andrew Chapman
   .          o     .              (Gallimard Jeunesse - 1999)        .                   .            .
     .         \\                 ,             .                .
               #\\##\\#      .                              .        .
             #  #O##\\###                .                        .
   .        #*#  #\\##\\###                       .                     ,
        .   ##*#  #\\##\\##               .                     .
      .      ##*#  #\\##\#         .                             ,       .
          .     *#  #\\#     .                    .             .          ,
                      \\          .                         .
____^/\\___^--____/\\____O______________/\\/\\---/\\___________---______________
   /\\^   ^  ^    ^                  ^^ ^  '\\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __
                """,
                message="",
                answers=True
            ),
            Stars(screen, screen.width)
        ])
    ]
    screen.play(scenes, unhandled_input=_unhandled_input)

last_scene = None
if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(run, arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError:
            pass

