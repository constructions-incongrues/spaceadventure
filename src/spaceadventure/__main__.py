from asciimatics.event import KeyboardEvent
from asciimatics.effects import Stars, Cycle, RandomNoise, Julia
from asciimatics.exceptions import NextScene, ResizeScreenError
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.renderers import FigletText, Rainbow
from frame import SpaceAdventureFrame
import sys

def _unhandled_input(event):
    if (event is not None and isinstance(event, KeyboardEvent) and event.key_code == 10):
        raise NextScene
    else:
        return event

def julia(screen, duration=5):
    effects = [Julia(screen)]

    return Scene(effects, duration)


def noise(screen, text=None, duration=5):
    if text is None:
        effects = [RandomNoise(screen)]
    else:
        effects = [RandomNoise(screen, signal=Rainbow(screen, FigletText(text)))]

    return Scene(effects, duration)

def title(screen):
    effects = [
        Cycle(
            screen,
            FigletText("SPACE", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("ADVENTURE", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]

    return Scene(effects, -1)

def run(screen, scene):
    scenes = [
        # title
        julia(screen),
        title(screen),

        # 01
        Scene([
            SpaceAdventureFrame(
                screen,
                image="",
                message="""
Salut inconnu.e, soit le bienvenu dans le jeu Space Adventure.
Nous comptons sur ton courage, ta coopération et ta réfléxion pour avancer dans les différentes quêtes.
Je vois que tu es prêt à relever ce défi.

> Comment t'appelles-tu ?
                """,
                answers=["jimmy"]
            ),
            Stars(screen, 200)
        ]),

        noise(screen),

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
> X-Wing | NCC-1701-J | Vandervecken | Aloha-Oe | Cyrus
                """,
                answers=["vandervecken"]
            ),
            Stars(screen, 200)
        ]),

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
À son bord, le savant dément,
se prépare à soumettre votre monde à ses effroyables expériences.

> Découvre l'identité du commandant et communique son nom à ton équipage.
                """,
                answers=["cyrus"]
            ),
            Stars(screen, 200)
        ]),

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
ll n'y a plus un instant à perdre :
les autorités ont fait appel à la Guilde des Mercenaires de l'espace
pour mettre un terme aux sombres machinations de Cyrus

> Souhaites-tu intégrer la Guilde des Mercenaires ?
                """,
                answers=["oui"]
            ),
            Stars(screen, 200)
        ]),

        # 04
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
                          __.--|~|--.__                               ,,;/;
                         /~     | |    ;~\                          ,;;;/;;'
                        /|      | |    ;~\\                      ,;;;;/;;;'
                       |/|      \_/   ;;;|\                    ,;;;;/;;;;'
                       |/ \          ;;;/  )                 ,;;;;/;;;;;'
                   ___ | ______     ;_____ |___....__      ,;;;;/;;;;;'
             ___.-~ \\(| \  \.\ \__/ /./ /:|)~   ~   \   ,;;;;/;;;;;'
         /~~~    ~\    |  ~-.     |   .-~: |//  _.-~~--,;;;;/;;;;;'
        (.-~___     \.'|    | /-.__.-\|::::| //~     ,;;;;/;;;;;'
        /      ~~--._ \|   /          `\:: |/      ,;;;;/;;;;;'
     .-|             ~~|   |  /V''''V\ |:  |     ,;;;;/;;;;;' \
    /                   \  |  ~`^~~^'~ |  /    ,;;;;/;;;;;'    ;
   (        \             \|`\._____./'|/    ,;;;;/;;;;;'      '\
  / \        \                             ,;;;;/;;;;;'     /    |
 |            |                          ,;;;;/;;;;;'      |     |
|`-._          |                       ,;;;;/;;;;;'              \
|             /                      ,;;;;/;;;;;'  \              \__________
(             )                 |  ,;;;;/;;;;;'      |        _.--~
 \          \/ \              ,  ;;;;;/;;;;;'       /(     .-~_..--~~~~~~~~~~
 \__         '  `       ,     ,;;;;;/;;;;;'    .   /  \   / /~
 /___________\'  |`._______ ,;;;;;;/;;;;;;'_______ /   : \/'/'
                """,
                message="""
Félicitation ! Tu as été promu "Mercenaire de l'espace".
Tu vas devoir t'introduire dans le Vandervecken, un univers de pièges diaboliques,
pour y affronter Cyrus et les créatures qui le protègent.

> Quel équipement choisis-tu pour t'aider dans ta mission ?

                """,
                answers=True
            ),
            Stars(screen, 200)
        ]),

        # 05
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |_____;----.___|

                """,
                message="""
Tu arpentes la coursive et découvre deux portes. L'une est noire, comme on en voit au plus profond des galaxies. L'autre brille d'un blanc éclatant, presque aveuglant..

> De quelle couleur est la porte que tu décides d'ouvrir ?
                """,
                answers=["noire", "blanche"]
            ),
            Stars(screen, 200)
        ]),

        # 06
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
               /|
  _______________)|.. 
<'______________<(,_|) 
           .((()))| )) << YEAAYAAAAEAAAARGH!! >>
           (======)| \
          ((( "_"()|_ \
         '()))(_)/_/ ' )
         .--/_\ /(  /./
        /'._.--\ .-(_/
       / / )\___:___) 
      ( -.'.._  |  /
       \  \_\ ( | )
        '. /\)_(_)|
          '-|  XX |
           %%%%%%%%
          / %%%%%%%\
         ( /.-'%%%. \ 
        /(.'   %%\ :|
       / ,|    %  ) )
     _|___)   %  (__|_
     )___/       )___(
      |x/      mrf\ >
      |x)         / '.
      |x\       _(____''.__
    --\ -\--
     --\__|--
                """,
                message="""
La porte s'ouvre, Cyrus est aux commandes de la console de pilotage. Il te tourne le dos et n'a pas l'air d'avoir remarqué ta présence.
C'est l'occasion rêvée pour l'estourbir sans effort ! Tu t'approches discrètement du fauteuil où est assez confortablement... UN MANEQUIN !
C'était un piège, Cyrus surgit d'une encoignure et te désarme. Il ne te reste plus qu'une chance : envoyer un message d'urgence depuis le transmetteur
interplanétaire caché dans ta botte gauche à la seule personne en mesure de te sauver la mise.

> Comment s'appelle cette personne ?

                                """,
                answers=["james"]
            ),
            Stars(screen, 200)
        ]),

        # 06
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
                """,
                message="""
Voilà déjà presque neuf nanosecondes que ton appel de détresse est parti et James n'est toujours pas là !
T'aurait-il oublié ? Cela n'a plus d'importance : dans moins d'une nanosecondes il en sera fini de toi et de toute l'Humanité.
Alors que Cyrus s'apprête à te porter un coup fatal, un bourdonnement terrible enfle dans la cabine et tout d'un coup
ce sont tous les écrans de contrôles de la pièce qui diffusent la même image : celle de James le Cyber-Mercenaire riant aux éclats.
Il semble te faire un clin d'œil puis enfonce la touche entrée de son clavier, ouvrant ainsi le sas de décompression de la cabine.
Tes réflexes de Mercenaire de l'Espace te permettent de sauter hors de la cabine à temps pour voir Cyrus aspiré vers son dernier
voyage à travers les étoiles.

> Quelle est la commande qui t'a sauvé ?

                                """,
                answers=["sudo spaceshipctl open vandervecken/airlock"]
            ),
            Stars(screen, 200)
        ]),

        # 07
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
    ___________
   '._==_==_=_.'
   .-\:      /-.
  | (|:.     |) |
   '-|:.     |-'
     \::.    /
      '::. .'
        ) (
      _.' '._.
     `"""""""`
                """,
                message="""
Félicitation !
Le vaisseau Vandervecken est sous controle.
Cyrus est neutralisé.
Votre mission est désormais terminé.
Prochaine mission : Explorer Saturne

                                """,
                answers=True
            ),
            Stars(screen, 200)
        ]),

        # 07
        Scene([
            SpaceAdventureFrame(
                screen,
                image="""
          .                                            .
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
        o                             .                   .
         .              .                .
          0     .                  Programmation: Tristan
                 .          .      Création : Maison JOLU            ,                ,    ,
 .          \          .           Un livre dont vous êtes le héros
      .      \   ,                 Le mercenaire de l'espace de Andrew Chapman
   .          o     .              (Gallimard Jeunesse - 1999)        .                   .            .
     .         \                 ,             .                .
               #\##\#      .                              .        .
             #  #O##\###                .                        .
   .        #*#  #\##\###                       .                     ,
        .   ##*#  #\##\##               .                     .
      .      ##*#  #1984#         .                             ,       .
          .     *#  #\#     .                    .             .          ,
                      \          .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __
                """,
                message="",
                answers=True
            ),
            Stars(screen, 200)
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



