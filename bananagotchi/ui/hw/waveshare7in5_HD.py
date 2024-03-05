import logging

import bananagotchi.ui.fonts as fonts
from bananagotchi.ui.hw.base import DisplayImpl


class Waveshare7in5HD(DisplayImpl):
    def __init__(self, config):
        super(Waveshare7in5HD, self).__init__(config, 'waveshare7in5_HD')

    def layout(self):
        fonts.setup(10, 8, 10, 18, 25, 9)
        self._layout['width'] = 880
        self._layout['height'] = 528
        self._layout['face'] = (0, 43)
        self._layout['name'] = (0, 14)
        self._layout['channel'] = (0, 0)
        self._layout['aps'] = (0, 71)
        self._layout['uptime'] = (0, 25)
        self._layout['line1'] = [0, 12, 880, 12]
        self._layout['line2'] = [0, 116, 880, 116]
        self._layout['friend_face'] = (12, 88)
        self._layout['friend_name'] = (1, 103)
        self._layout['shakes'] = (26, 117)
        self._layout['mode'] = (0, 117)
        self._layout['status'] = {
            'pos': (65, 26),
            'font': fonts.status_font(fonts.Small),
            'max': 12
        }
        return self._layout

    def initialize(self):
        logging.info("initializing waveshare 7.5HD inch lcd display")
        from bananagotchi.ui.hw.libs.waveshare.v7in5_HD.epd7in5_HD import EPD
        self._display = EPD()
        self._display.init()
        self._display.Clear()

    def render(self, canvas):
        buf = self._display.getbuffer(canvas)
        self._display.display(buf)

    def clear(self):
        self._display.Clear()
