from asciimatics.event import KeyboardEvent
from asciimatics.widgets import Frame
from asciimatics.exceptions import NextScene
from asciimatics.widgets import Frame, Layout, Label, Text
import textwrap

class SpaceAdventureFrame(Frame):
    def __init__(self, screen, image="IMAGE", message="MESSAGE", theme="monochrome", answers=[]):
        super(SpaceAdventureFrame, self).__init__(screen,
                                        int(screen.height * 2 // 3),
                                        int(screen.width * 2 // 3),
                                        can_scroll = False,
                                        has_border = False,
                                        reduce_cpu = True)

        # init
        self.image = image
        self.message = message
        self.answers = answers
        self.set_theme(theme)

        # layout
        layout = Layout([120], fill_frame = False)
        self.add_layout(layout)
        label_height = len(self.image.split("\n")) + len(self.message.split("\n"))
        layout.add_widget(Label(label="%s\n%s" % (self.image, self.message), height=label_height), 0)
        layout.add_widget(Text(name="answer", label="? "), 0)

        self.fix()

    def process_event(self, event):
        if (event is not None and isinstance(event, KeyboardEvent) and event.key_code == 10):
            self.save()

            if (self.answers is True or self.data["answer"].lower() in self.answers):
                raise NextScene

            return None
        else:
            return super(SpaceAdventureFrame, self).process_event(event)
