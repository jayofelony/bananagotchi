from pwnagotchi.ui.hw.inky import Inky
from pwnagotchi.ui.hw.papirus import Papirus
from pwnagotchi.ui.hw.oledhat import OledHat
from pwnagotchi.ui.hw.lcdhat import LcdHat
from pwnagotchi.ui.hw.dfrobot import DFRobotV1
from pwnagotchi.ui.hw.dfrobot_v2 import DFRobotV2
from pwnagotchi.ui.hw.waveshare2in13 import WaveshareV1
from pwnagotchi.ui.hw.waveshare2in13_V2 import WaveshareV2
from pwnagotchi.ui.hw.waveshare2in13_V3 import WaveshareV3
from pwnagotchi.ui.hw.waveshare2in13_V4 import WaveshareV4
from pwnagotchi.ui.hw.waveshare2in7 import Waveshare27inch
from pwnagotchi.ui.hw.waveshare2in7_V2 import Waveshare27inchV2
from pwnagotchi.ui.hw.waveshare2in9 import Waveshare29inch
from pwnagotchi.ui.hw.waveshare2in9_V2 import Waveshare29inchV2
from pwnagotchi.ui.hw.waveshare1in44lcd import Waveshare144lcd
from pwnagotchi.ui.hw.waveshare1in54b import Waveshare154inchb
from pwnagotchi.ui.hw.waveshare2in13bc import Waveshare213bc
from pwnagotchi.ui.hw.waveshare2in13d import Waveshare213d
from pwnagotchi.ui.hw.waveshare2in13g import Waveshare2in13g
from pwnagotchi.ui.hw.waveshare2in13b_V4 import Waveshare213bV4
from pwnagotchi.ui.hw.waveshare3in5lcd import Waveshare35lcd
from pwnagotchi.ui.hw.spotpear24in import Spotpear24inch
from pwnagotchi.ui.hw.displayhatmini import DisplayHatMini
from pwnagotchi.ui.hw.waveshare1in02 import Waveshare1in02
from pwnagotchi.ui.hw.waveshare1in54 import Waveshare154
from pwnagotchi.ui.hw.waveshare1in54_V2 import Waveshare154V2
from pwnagotchi.ui.hw.waveshare1in54b_V2 import Waveshare154bV2
from pwnagotchi.ui.hw.waveshare1in54c import Waveshare1in54c
from pwnagotchi.ui.hw.waveshare1in64g import Waveshare1in64g
from pwnagotchi.ui.hw.waveshare2in7b import Waveshare27b
from pwnagotchi.ui.hw.waveshare2in7b_V2 import Waveshare27bV2
from pwnagotchi.ui.hw.waveshare2in9b_V3 import Waveshare29bV3
from pwnagotchi.ui.hw.waveshare2in9b_V4 import Waveshare29bV4
from pwnagotchi.ui.hw.waveshare2in9bc import Waveshare2in9bc
from pwnagotchi.ui.hw.waveshare2in9d import Waveshare2in9d
from pwnagotchi.ui.hw.waveshare2in13b_V3 import Waveshare2in13bV3
from pwnagotchi.ui.hw.waveshare2in36g import Waveshare2in36g
from pwnagotchi.ui.hw.waveshare2in66 import Waveshare2in66
from pwnagotchi.ui.hw.waveshare2in66b import Waveshare2in66b
from pwnagotchi.ui.hw.waveshare2in66g import Waveshare2in66g
from pwnagotchi.ui.hw.waveshare3in0g import Waveshare3in0g
from pwnagotchi.ui.hw.waveshare3in7 import Waveshare3in7
from pwnagotchi.ui.hw.waveshare3in52 import Waveshare3in52
from pwnagotchi.ui.hw.waveshare4in01f import Waveshare4in01f
from pwnagotchi.ui.hw.waveshare4in2 import Waveshare4in2
from pwnagotchi.ui.hw.waveshare4in2_V2 import Waveshare4in2V2
from pwnagotchi.ui.hw.waveshare4in2b_V2 import Waveshare4in2bV2
from pwnagotchi.ui.hw.waveshare4in2bc import Waveshare4in2bc
from pwnagotchi.ui.hw.waveshare4in26 import Waveshare4in26
from pwnagotchi.ui.hw.waveshare4in37g import Waveshare4in37g
from pwnagotchi.ui.hw.waveshare5in65f import Waveshare5in65f
from pwnagotchi.ui.hw.waveshare5in83 import Waveshare5in83
from pwnagotchi.ui.hw.waveshare5in83_V2 import Waveshare5in83V2
from pwnagotchi.ui.hw.waveshare5in83b_V2 import Waveshare5in83bV2
from pwnagotchi.ui.hw.waveshare5in83bc import Waveshare5in83bc
from pwnagotchi.ui.hw.waveshare7in3f import Waveshare7in3f
from pwnagotchi.ui.hw.waveshare7in3g import Waveshare7in3g
from pwnagotchi.ui.hw.waveshare7in5 import Waveshare7in5
from pwnagotchi.ui.hw.waveshare7in5_HD import Waveshare7in5HD
from pwnagotchi.ui.hw.waveshare7in5_V2 import Waveshare7in5V2
from pwnagotchi.ui.hw.waveshare7in5b_HD import Waveshare7in5bHD
from pwnagotchi.ui.hw.waveshare7in5b_V2 import Waveshare7in5bV2
from pwnagotchi.ui.hw.waveshare7in5bc import Waveshare7in5bc
from pwnagotchi.ui.hw.waveshare13in3k import Waveshare13in3k


def display_for(config):
    # config has been normalized already in utils.load_config
    if config['ui']['display']['type'] == 'inky':
        return Inky(config)

    elif config['ui']['display']['type'] == 'papirus':
        return Papirus(config)

    elif config['ui']['display']['type'] == 'oledhat':
        return OledHat(config)

    elif config['ui']['display']['type'] == 'lcdhat':
        return LcdHat(config)

    elif config['ui']['display']['type'] == 'dfrobot_1':
        return DFRobotV1(config)

    elif config['ui']['display']['type'] == 'dfrobot_2':
        return DFRobotV2(config)

    elif config['ui']['display']['type'] == 'waveshare144lcd':
        return Waveshare144lcd(config)

    elif config['ui']['display']['type'] == 'waveshare35lcd':
        return Waveshare35lcd(config)

    elif config['ui']['display']['type'] == 'spotpear24inch':
        return Spotpear24inch(config)

    elif config['ui']['display']['type'] == 'displayhatmini':
        return DisplayHatMini(config)

    elif config['ui']['display']['type'] == 'waveshare1in02':
        return Waveshare1in02(config)

    elif config['ui']['display']['type'] == 'waveshare1in54':
        return Waveshare154(config)

    elif config['ui']['display']['type'] == 'waveshare1in54_v2':
        return Waveshare154V2(config)

    elif config['ui']['display']['type'] == 'waveshare1in54b':
        return Waveshare154inchb(config)

    elif config['ui']['display']['type'] == 'waveshare1in54b_v2':
        return Waveshare154bV2(config)

    elif config['ui']['display']['type'] == 'waveshare1in54c':
        return Waveshare1in54c(config)

    elif config['ui']['display']['type'] == 'waveshare1in64g':
        return Waveshare1in64g(config)

    elif config['ui']['display']['type'] == 'waveshare2in7':
        return Waveshare27inch(config)

    elif config['ui']['display']['type'] == 'waveshare2in7_v2':
        return Waveshare27inchV2(config)

    elif config['ui']['display']['type'] == 'waveshare2in7b':
        return Waveshare27b(config)

    elif config['ui']['display']['type'] == 'waveshare2in7b_v2':
        return Waveshare27bV2(config)

    elif config['ui']['display']['type'] == 'waveshare2in9':
        return Waveshare29inch(config)

    elif config['ui']['display']['type'] == 'waveshare2in9bc':
        return Waveshare2in9bc(config)

    elif config['ui']['display']['type'] == 'waveshare2in9d':
        return Waveshare2in9d(config)

    elif config['ui']['display']['type'] == 'waveshare2in9_v2':
        return Waveshare29inchV2(config)

    elif config['ui']['display']['type'] == 'waveshare2in9b_v3':
        return Waveshare29bV3(config)

    elif config['ui']['display']['type'] == 'waveshare2in9b_v4':
        return Waveshare29bV4(config)

    elif config['ui']['display']['type'] == 'waveshare_1':
        return WaveshareV1(config)

    elif config['ui']['display']['type'] == 'waveshare_2':
        return WaveshareV2(config)

    elif config['ui']['display']['type'] == 'waveshare_3':
        return WaveshareV3(config)

    elif config['ui']['display']['type'] == 'waveshare_4':
        return WaveshareV4(config)

    elif config['ui']['display']['type'] == 'waveshare2in13bc':
        return Waveshare213bc(config)

    elif config['ui']['display']['type'] == 'waveshare2in13d':
        return Waveshare213d(config)

    elif config['ui']['display']['type'] == 'waveshare2in13b_v3':
        return Waveshare2in13bV3(config)

    elif config['ui']['display']['type'] == 'waveshare2in13b_v4':
        return Waveshare213bV4(config)

    elif config['ui']['display']['type'] == 'waveshare2in13g':
        return Waveshare2in13g(config)

    elif config['ui']['display']['type'] == 'waveshare2in36g':
        return Waveshare2in36g(config)

    elif config['ui']['display']['type'] == 'waveshare2in66':
        return Waveshare2in66(config)

    elif config['ui']['display']['type'] == 'waveshare2in66b':
        return Waveshare2in66b(config)

    elif config['ui']['display']['type'] == 'waveshare2in66g':
        return Waveshare2in66g(config)

    elif config['ui']['display']['type'] == 'waveshare3in0g':
        return Waveshare3in0g(config)

    elif config['ui']['display']['type'] == 'waveshare3in7':
        return Waveshare3in7(config)

    elif config['ui']['display']['type'] == 'waveshare3in52':
        return Waveshare3in52(config)

    elif config['ui']['display']['type'] == 'waveshare4in01f':
        return Waveshare4in01f(config)

    elif config['ui']['display']['type'] == 'waveshare4in2':
        return Waveshare4in2(config)

    elif config['ui']['display']['type'] == 'waveshare4in2_v2':
        return Waveshare4in2V2(config)

    elif config['ui']['display']['type'] == 'waveshare4in2b_v2':
        return Waveshare4in2bV2(config)

    elif config['ui']['display']['type'] == 'waveshare4in2bc':
        return Waveshare4in2bc(config)

    elif config['ui']['display']['type'] == 'waveshare4in26':
        return Waveshare4in26(config)

    elif config['ui']['display']['type'] == 'waveshare4in37g':
        return Waveshare4in37g(config)

    elif config['ui']['display']['type'] == 'waveshare5in65f':
        return Waveshare5in65f(config)

    elif config['ui']['display']['type'] == 'waveshare5in83':
        return Waveshare5in83(config)

    elif config['ui']['display']['type'] == 'waveshare5in83_v2':
        return Waveshare5in83V2(config)

    elif config['ui']['display']['type'] == 'waveshare5in83b_v2':
        return Waveshare5in83bV2(config)

    elif config['ui']['display']['type'] == 'waveshare5in83bc':
        return Waveshare5in83bc(config)

    elif config['ui']['display']['type'] == 'waveshare7in3f':
        return Waveshare7in3f(config)

    elif config['ui']['display']['type'] == 'waveshare7in3g':
        return Waveshare7in3g(config)

    elif config['ui']['display']['type'] == 'waveshare7in5':
        return Waveshare7in5(config)

    elif config['ui']['display']['type'] == 'waveshare7in5_HD':
        return Waveshare7in5HD(config)

    elif config['ui']['display']['type'] == 'waveshare7in5_v2':
        return Waveshare7in5V2(config)

    elif config['ui']['display']['type'] == 'waveshare7in5b_HD':
        return Waveshare7in5bHD(config)

    elif config['ui']['display']['type'] == 'waveshare7in5b_v2':
        return Waveshare7in5bV2(config)

    elif config['ui']['display']['type'] == 'waveshare7in5bc':
        return Waveshare7in5bc(config)

    elif config['ui']['display']['type'] == 'waveshare13in3k':
        return Waveshare13in3k(config)
