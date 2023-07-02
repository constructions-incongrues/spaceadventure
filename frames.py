#!/usr/bin/env python3

from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, DropdownList, PopupMenu
from asciimatics.effects import Background
from asciimatics.renderers import FigletText
from asciimatics.event import KeyboardEvent
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import NextScene
from asciimatics.parsers import AsciimaticsParser
import sys
import re
import datetime
import logging


class Question1Frame(Frame):
    def __init__(self, screen):
        super(Question1Frame, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        data = {},
                                        can_scroll = False,
                                        has_border = False,
                                        reduce_cpu = True)

        self.set_theme("monochrome")
        layout = Layout([1, 18, 1])
        self.add_layout(layout)
        label = """
Salut inconnu.e, soit le bienvenu dans le jeu Space Adventure.
Nous comptons sur ton courage, ta coopération et ta réfléxion pour avancer dans les différentes quêtes.
Si tu es prêt à jouer, communique moi ton prénom.

"""
        layout.add_widget(Label(label=label, height=6), 1)

        self.add_layout(layout)
        layout.add_widget(Text(name="prenom", label="? "), 1)

        self.fix()

    # def _on_click(self):
    #     self.save()
    #     if (self.data["prenom"].lower() == "jimmy"):
    #         raise NextScene

    def process_event(self, event):
        if (event is not None and isinstance(event, KeyboardEvent) and event.key_code == 10):
            self.save()

            if (self.data["prenom"].lower() == "jimmy"):
                raise NextScene

            return None
        else:
            return super(Question1Frame, self).process_event(event)


#### Q2

class Question2Frame(Frame):
    def __init__(self, screen):
        super(Question2Frame, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        data = {},
                                        can_scroll = False,
                                        has_border = False,
                                        reduce_cpu = True)

        self.set_theme("monochrome")

        image = """
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

Au-dessus de votre planète se dessine l'ombre inquiétante d'un vaisseau spatial.
Identifier son matricule ?

> X-Wing | NCC-1701-J | Vandervecken | Aloha-Oe | Cyrus
"""

        layout = Layout([1, 1], fill_frame = True)
        self.add_layout(layout)
        layout.add_widget(Label(label=image, height=80), 0)
        layout.add_widget(Text(name="matricule", label="? "), 1)

        self.fix()

    def process_event(self, event):
        if (event is not None and isinstance(event, KeyboardEvent) and event.key_code == 10):
            self.save()

            if (self.data["matricule"].lower() == "vandervecken"):
                raise NextScene

            return None
        else:
            return super(Question2Frame, self).process_event(event)


#### Q3

class Question3Frame(Frame):
    def __init__(self, screen):
        super(Question3Frame, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        data = {},
                                        can_scroll = False,
                                        has_border = False,
                                        reduce_cpu = True)

        self.set_theme("monochrome")

        image = """
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


À son bord, le savant dément,
se prépare à soumettre votre monde à ses effroyables expériences.
Découvre l'identité du commandant et communique son nom à ton équipage.
"""

        layout = Layout([1, 1], fill_frame = True)
        self.add_layout(layout)
        layout.add_widget(Label(label=image, height=80), 0)
        layout.add_widget(Text(name="answer", label="? "), 1)

        self.fix()

    def process_event(self, event):
        if (event is not None and isinstance(event, KeyboardEvent) and event.key_code == 10):
            self.save()

            if (self.data["answer"].lower() == "cyrus"):
                raise NextScene

            return None
        else:
            return super(Question3Frame, self).process_event(event)


#### Q4


class Question4Frame(Frame):
    def __init__(self, screen):
        super(Question4Frame, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        data = {},
                                        can_scroll = False,
                                        has_border = False,
                                        reduce_cpu = True)

        self.set_theme("monochrome")

        image = """
              .+.
          _.-//_\\-._
        .'.-' XII '-.'.
      /`.'*         *'.`\
     / /*        /    *\ \
    | ;        _/       ; |
    | |IX     (_)    III| |
    | ;         \       ; |
     \ \*        \    */ /
      \ '.*       \ *.'./
       '._'-.__VI_.-'_.'
          '-.,___,.-'

ll n'y a plus un instant à perdre :
les autorités ont fait appel à la Guilde des Mercenaires de l'espace
pour mettre un terme aux sombres machinations de Cyrus
Souhaites-tu intégrer la Guilde des Mercenaires ?
"""

        layout = Layout([40, 40], fill_frame = True)
        self.add_layout(layout)
        layout.add_widget(Label(label=image, height=80), 0)
        layout.add_widget(Text(name="answer", label="? "), 1)

        self.fix()

    def process_event(self, event):
        if (event is not None and isinstance(event, KeyboardEvent) and event.key_code == 10):
            self.save()

            if (self.data["answer"].lower() == "oui"):
                raise NextScene

            return None
        else:
            return super(Question4Frame, self).process_event(event)

class Question5Frame(Frame):
    def __init__(self, screen):
        super(Question5Frame, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        data = {},
                                        can_scroll = False,
                                        has_border = False,
                                        reduce_cpu = True)

        self.set_theme("monochrome")

        image = """
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
     .-|             ~~|   |  /V''''V\ |:  |     ,;;;;/;;;;;' \\
    /                   \  |  ~`^~~^'~ |  /    ,;;;;/;;;;;'    ;
   (        \             \|`\._____./'|/    ,;;;;/;;;;;'      '\\
  / \        \                             ,;;;;/;;;;;'     /    |
 |            |                          ,;;;;/;;;;;'      |     |
|`-._          |                       ,;;;;/;;;;;'              \
|             /                      ,;;;;/;;;;;'  \              \__________
(             )                 |  ,;;;;/;;;;;'      |        _.--~
 \          \/ \              ,  ;;;;;/;;;;;'       /(     .-~_..--~~~~~~~~~~
 \__         '  `       ,     ,;;;;;/;;;;;'    .   /  \   / /~
 /___________\'  |`._______ ,;;;;;;/;;;;;;'_______ /   : \/'/'

 Félicitation ! Tu as été promu "Mercenaire de l'espace".
 Tu vas devoir t'introduire dans le Vandervecken, un univers de pièges diaboliques, pour y affronter Cyrus et les créatures qui le protègent.
 Acceptes-tu la mission ?
"""

        layout = Layout([40, 40], fill_frame = True)
        self.add_layout(layout)
        layout.add_widget(Label(label=image, height=80), 0)
        layout.add_widget(Text(name="answer", label="? "), 1)

        self.fix()

    def process_event(self, event):
        if (event is not None and isinstance(event, KeyboardEvent) and event.key_code == 10):
            raise NextScene
        else:
            return super(Question5Frame, self).process_event(event)

