from asciimatics.effects import RandomNoise, Julia
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.scene import Scene

class SpaceAdventureTransition:
    def __init__(self, screen, duration=5):
        self.screen = screen
        pass

def julia(screen, duration=5):
    effects = [Julia(screen)]

    return Scene(effects, duration)

def noise(screen, text=None, duration=5):
    if text is None:
        effects = [RandomNoise(screen)]
    else:
        effects = [RandomNoise(screen, signal=Rainbow(screen, FigletText(text)))]

    return Scene(effects, duration)