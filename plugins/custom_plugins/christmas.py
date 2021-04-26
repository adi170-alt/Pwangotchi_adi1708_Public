from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import datetime
import math


class Christmas(plugins.Plugin):
    __author__ = 'https://github.com/LoganMD'
    __version__ = '1.2.0'
    __license__ = 'GPL3'
    __description__ = 'Birth Day Counter for pwnagotchi'

    def on_loaded(self):
        logging.info("Christmas Plugin loaded.")

    def on_ui_setup(self, ui):
        emenable = False
        
        with open('/etc/pwnagotchi/config.toml', 'r') as f:
            config = f.read().splitlines()

        if "main.plugins.memtemp.enabled = true" in config:
            memenable = True
            logging.info(
                "Christmas Plugin: memtemp is enabled")
                
        if ui.is_waveshare_v2():
            pos = (160, 95) if memenable else (160, 95)
            ui.add_element('christmas', LabeledValue(color=BLACK, label='', value='christmas\n',
                                                     position=pos,
                                                     label_font=fonts.Small, text_font=fonts.Small))

    def on_ui_update(self, ui):
        now = datetime.datetime.now()
        christmas = datetime.datetime(now.year, 7, 3)
        if now > christmas:
            christmas = christmas.replace(year=now.year + 1)

        difference = (christmas - now)

        days = difference.days
        hours = difference.seconds // 3600
        minutes = (difference.seconds % 3600) // 60

        if now.month == 7 and now.day == 3:
            ui.set('christmas', "Happy bd!")
        elif days == 0:
            ui.set('christmas', "christmas\n%dH %dM" % (hours, minutes))
        else:
            ui.set('christmas', "(%dD)" % (days))
