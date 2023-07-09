from asciimatics.effects import RandomNoise, Julia
from asciimatics.renderers import FigletText, Rainbow, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.effects import Stars, Print
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, PalmFirework
from random import randint, choice

def julia(screen, duration=5):
    effects = [Julia(screen)]

    return Scene(effects, duration)

def noise(screen, text=None, duration=5):
    if text is None:
        effects = [RandomNoise(screen)]
    else:
        effects = [RandomNoise(screen, signal=Rainbow(screen, FigletText(text)))]

    return Scene(effects, duration)

def fireworks(screen, duration=10):
    scenes = []
    effects = [
        Stars(screen, screen.width),
        Print(screen,
              SpeechBubble("Press space to see it again"),
              y=screen.height - 3,
              start_frame=300)
    ]
    for _ in range(20):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (RingFirework, 20, 30),
            (SerpentFirework, 30, 35),
        ]
        firework, start, stop = choice(fireworks)
        effects.insert(
            1,
            firework(screen,
                     randint(0, screen.width),
                     randint(screen.height // 8, screen.height * 3 // 4),
                     randint(start, stop),
                     start_frame=randint(0, 250)))

    effects.append(Print(screen,
                         Rainbow(screen, FigletText("BRAVO")),
                         screen.height // 2 - 6,
                         speed=1,
                         start_frame=100))
    effects.append(Print(screen,
                         Rainbow(screen, FigletText("JIMMY !")),
                         screen.height // 2 + 1,
                         speed=1,
                         start_frame=100))
    scenes.append(Scene(effects, -1))

    return Scene(effects, duration)