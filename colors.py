# Colors
## Basic colors
gray = '\033[30m'
red = '\033[1;31m'
lime = '\033[1;32m'
orange = '\033[1;33m'
blue = '\033[1;34m'
purple = '\033[1;35m'
light_blue = '\033[1;36m'
ghostwhite = '\033[1;37m'

## Light colors
cyan = '\033[36m'
white = '\033[37m'
light_gray = '\033[90m'
light_red = '\033[91m'
light_lime = '\033[92m'
light_yellow = '\033[93m'
light_blue2 = '\033[94m'
light_purple = '\033[95m'

## Dark colors
darkblack = '\033[030m'
darkred = '\033[031m'
darkgreen = '\033[032m'
darkyellow = '\033[033m'
darkblue = '\033[034m'
darkmagenta = '\033[035m'
darkcyan = '\033[036m'
darkwhite = '\033[037m'

## Text formating
reset = '\033[0m'
bold = '\033[1m'
dark = '\033[2m'
italic = '\033[3m'
underscore = '\033[4m'
normal = '\033[22m'

## The colors for the rest of the tool

try:
    from colored import fg, attr
except ModuleNotFoundError:
    print()
    criticalmsg = blue+"["+red+"CRITICAL"+blue+"]"+ghostwhite+"   A current(s) module(s) was not installed, run the 'setup.py' for install it. (sudo setup.py install)\n"
    exit(criticalmsg)
except NameError:
    print()
    criticalmsg = blue+"["+red+"CRITICAL"+blue+"]"+ghostwhite+"   A current(s) module(s) was not installed, run the 'setup.py' for install it. (sudo setup.py install)\n"
    exit(criticalmsg)
### The blues
bC = fg('#1d89f3')      # blue
bC2 = fg('#0B4D8F')     # dark blue

### The reds
rC = fg('#F44336')      # red
rC3 = fg('#ffa000')     # light orange
rC2 = fg('#ec5a0d')     # orange

### The greens
gC = fg('#39CC3F')      # green

### The yellows
yC = fg('#EDFF00')

### Reset
r = attr('reset')       # to finish the color formatting
# End of colors section