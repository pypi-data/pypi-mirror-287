modMap = {
    # Ducky Script
    "CTRL": 0x01,  # LCTRL
    "CONTROL": 0x01,  # LCTRL
    "SHIFT": 0x02,  # LSHIFT
    "ALT": 0x04,  # LALT
    "GUI": 0x08,  # LMETA
    "WINDOWS": 0x08,  # LMETA
    # BadUSB Script
    "ALTGR": 0x40,  # RALT
    # Extras
    "LCTRL": 0x01,
    "LSHIFT": 0x02,
    "LALT": 0x04,
    "LMETA": 0x08,
    "RCTRL": 0x10,
    "RSHIFT": 0x20,
    "RALT": 0x40,
    "RMETA": 0x80,
}

charMap = {
    "a": 0x04,
    "b": 0x05,
    "c": 0x06,
    "d": 0x07,
    "e": 0x08,
    "f": 0x09,
    "g": 0x0A,
    "h": 0x0B,
    "i": 0x0C,
    "j": 0x0D,
    "k": 0x0E,
    "l": 0x0F,
    "m": 0x10,
    "n": 0x11,
    "o": 0x12,
    "p": 0x13,
    "q": 0x14,
    "r": 0x15,
    "s": 0x16,
    "t": 0x17,
    "u": 0x18,
    "v": 0x19,
    "w": 0x1A,
    "x": 0x1B,
    "y": 0x1C,
    "z": 0x1D,
    "1": 0x1E,
    "2": 0x1F,
    "3": 0x20,
    "4": 0x21,
    "5": 0x22,
    "6": 0x23,
    "7": 0x24,
    "8": 0x25,
    "9": 0x26,
    "0": 0x27,
    " ": 0x2C,
    "-": 0x2D,
    "=": 0x2E,
    "[": 0x2F,
    "]": 0x30,
    "\\": 0x31,
    "#": 0x32,
    ";": 0x33,
    "'": 0x34,
    "`": 0x35,
    ",": 0x36,
    ".": 0x37,
    "/": 0x38,
    # Extras
    "\n": 0x28,  # ENTER
    "Space": 0x2C,  # SPACE
    "Intl\\": 0x64,  # Keyboard Non-US \ and |
    "IntlRo": 0x87,  # Keyboard International1
    "IntlYen": 0x89,  # Keyboard International3
}

keyMap = {
    "A": 0x04,  # Keyboard a and A
    "B": 0x05,  # Keyboard b and B
    "C": 0x06,  # Keyboard c and C
    "D": 0x07,  # Keyboard d and D
    "E": 0x08,  # Keyboard e and E
    "F": 0x09,  # Keyboard f and F
    "G": 0x0A,  # Keyboard g and G
    "H": 0x0B,  # Keyboard h and H
    "I": 0x0C,  # Keyboard i and I
    "J": 0x0D,  # Keyboard j and J
    "K": 0x0E,  # Keyboard k and K
    "L": 0x0F,  # Keyboard l and L
    "M": 0x10,  # Keyboard m and M
    "N": 0x11,  # Keyboard n and N
    "O": 0x12,  # Keyboard o and O
    "P": 0x13,  # Keyboard p and P
    "Q": 0x14,  # Keyboard q and Q
    "R": 0x15,  # Keyboard r and R
    "S": 0x16,  # Keyboard s and S
    "T": 0x17,  # Keyboard t and T
    "U": 0x18,  # Keyboard u and U
    "V": 0x19,  # Keyboard v and V
    "W": 0x1A,  # Keyboard w and W
    "X": 0x1B,  # Keyboard x and X
    "Y": 0x1C,  # Keyboard y and Y
    "Z": 0x1D,  # Keyboard z and Z
    "F1": 0x3A,  # Keyboard F1
    "F2": 0x3B,  # Keyboard F2
    "F3": 0x3C,  # Keyboard F3
    "F4": 0x3D,  # Keyboard F4
    "F5": 0x3E,  # Keyboard F5
    "F6": 0x3F,  # Keyboard F6
    "F7": 0x40,  # Keyboard F7
    "F8": 0x41,  # Keyboard F8
    "F9": 0x42,  # Keyboard F9
    "F10": 0x43,  # Keyboard F10
    "F11": 0x44,  # Keyboard F11
    "F12": 0x45,  # Keyboard F12
    # Ducky Script
    "ENTER": 0x28,  # Keyboard Return (ENTER)
    "MENU": 0x76,  # PROPS
    "APP": 0x76,  # PROPS
    "DELETE": 0x4C,  # Keyboard Delete Forward
    "HOME": 0x4A,  # Keyboard Home
    "INSERT": 0x49,  # Keyboard Insert
    "PAGEUP": 0x4B,  # Keyboard Page Up
    "PAGEDOWN": 0x4E,  # Keyboard Page Down
    "UP": 0x52,  # Keyboard Up Arrow
    "UPARROW": 0x52,  # UP
    "DOWN": 0x51,  # Keyboard Down Arrow
    "DOWNARROW": 0x51,  # DOWN
    "LEFT": 0x50,  # Keyboard Left Arrow
    "LEFTARROW": 0x50,  # LEFT
    "RIGHT": 0x4F,  # Keyboard Right Arrow
    "RIGHTARROW": 0x4F,  # RIGHT
    "TAB": 0x2B,  # Keyboard Tab
    "END": 0x4D,  # Keyboard End
    "ESC": 0x29,  # Keyboard ESCAPE
    "ESCAPE": 0x29,  # ESC
    "SPACE": 0x2C,  # Keyboard Spacebar
    "PAUSE": 0x48,  # Keyboard Pause
    "BREAK": 0x48,  # PAUSE
    "CAPSLOCK": 0x39,  # Keyboard Caps Lock
    "NUMLOCK": 0x53,  # Keyboard Num Lock and Clear
    "PRINTSCREEN": 0x46,  # PRINT
    "SCROLLLOCK": 0x47,  # Keyboard Scroll Lock
    # BadUSB Script
    "BACKSPACE": 0x2A,  # Keyboard DELETE (Backspace)
    # Numpad
    "NUM_ASTERIX": 0x55,
    "NUM_MINUS": 0x56,
    "NUM_PLUS": 0x57,
    "NUM_ENTER": 0x58,
    "NUM_1": 0x59,
    "NUM_2": 0x5A,
    "NUM_3": 0x5B,
    "NUM_4": 0x5C,
    "NUM_5": 0x5D,
    "NUM_6": 0x5E,
    "NUM_7": 0x5F,
    "NUM_8": 0x60,
    "NUM_9": 0x61,
    "NUM_0": 0x62,
    "NUM_DOT": 0x63,
    # Extras
    "NONE": 0x00,  # No key pressed
    "ERR_OVF": 0x01,  # Keyboard Error Roll Over - used for all slots if too many keys are pressed ("Phantom key")
    "MINUS": 0x2D,  # Keyboard - and _
    "EQUAL": 0x2E,  # Keyboard = and +
    "LEFTBRACE": 0x2F,  # Keyboard [ and {
    "RIGHTBRACE": 0x30,  # Keyboard ] and }
    "BACKSLASH": 0x31,  # Keyboard \ and |
    "HASHTILDE": 0x32,  # Keyboard Non-US # and ~
    "SEMICOLON": 0x33,  # Keyboard ; and :
    "APOSTROPHE": 0x34,  # Keyboard ' and "
    "GRAVE": 0x35,  # Keyboard ` and ~
    "COMMA": 0x36,  # Keyboard , and <
    "DOT": 0x37,  # Keyboard . and >
    "SLASH": 0x38,  # Keyboard / and ?
    "SYSRQ": 0x46,  # Keyboard Print Screen
    "KPSLASH": 0x54,  # Keypad /
    "KPASTERISK": 0x55,  # Keypad *
    "KPMINUS": 0x56,  # Keypad -
    "KPPLUS": 0x57,  # Keypad +
    "KPENTER": 0x58,  # Keypad ENTER
    "KP1": 0x59,  # Keypad 1 and End
    "KP2": 0x5A,  # Keypad 2 and Down Arrow
    "KP3": 0x5B,  # Keypad 3 and PageDn
    "KP4": 0x5C,  # Keypad 4 and Left Arrow
    "KP5": 0x5D,  # Keypad 5
    "KP6": 0x5E,  # Keypad 6 and Right Arrow
    "KP7": 0x5F,  # Keypad 7 and Home
    "KP8": 0x60,  # Keypad 8 and Up Arrow
    "KP9": 0x61,  # Keypad 9 and Page Up
    "KP0": 0x62,  # Keypad 0 and Insert
    "KPDOT": 0x63,  # Keypad . and Delete
    "102ND": 0x64,  # Keyboard Non-US \ and |
    "COMPOSE": 0x65,  # Keyboard Application
    "POWER": 0x66,  # Keyboard Power
    "KPEQUAL": 0x67,  # Keypad =
    "F13": 0x68,  # Keyboard F13
    "F14": 0x69,  # Keyboard F14
    "F15": 0x6A,  # Keyboard F15
    "F16": 0x6B,  # Keyboard F16
    "F17": 0x6C,  # Keyboard F17
    "F18": 0x6D,  # Keyboard F18
    "F19": 0x6E,  # Keyboard F19
    "F20": 0x6F,  # Keyboard F20
    "F21": 0x70,  # Keyboard F21
    "F22": 0x71,  # Keyboard F22
    "F23": 0x72,  # Keyboard F23
    "F24": 0x73,  # Keyboard F24
    "OPEN": 0x74,  # Keyboard Execute
    "HELP": 0x75,  # Keyboard Help
    "PROPS": 0x76,  # Keyboard Menu
    "FRONT": 0x77,  # Keyboard Select
    "STOP": 0x78,  # Keyboard Stop
    "AGAIN": 0x79,  # Keyboard Again
    "UNDO": 0x7A,  # Keyboard Undo
    "CUT": 0x7B,  # Keyboard Cut
    "COPY": 0x7C,  # Keyboard Copy
    "PASTE": 0x7D,  # Keyboard Paste
    "FIND": 0x7E,  # Keyboard Find
    "MUTE": 0x7F,  # Keyboard Mute
    "VOLUMEUP": 0x80,  # Keyboard Volume Up
    "VOLUMEDOWN": 0x81,  # Keyboard Volume Down
    "KPCOMMA": 0x85,  # Keypad Comma
    "RO": 0x87,  # Keyboard International1
    "KATAKANAHIRAGANA": 0x88,  # Keyboard International2
    "YEN": 0x89,  # Keyboard International3
    "HENKAN": 0x8A,  # Keyboard International4
    "MUHENKAN": 0x8B,  # Keyboard International5
    "KPJPCOMMA": 0x8C,  # Keyboard International6
    "HANGEUL": 0x90,  # Keyboard LANG1
    "HANJA": 0x91,  # Keyboard LANG2
    "KATAKANA": 0x92,  # Keyboard LANG3
    "HIRAGANA": 0x93,  # Keyboard LANG4
    "ZENKAKUHANKAKU": 0x94,  # Keyboard LANG5
    "KPLEFTPAREN": 0xB6,  # Keypad (
    "KPRIGHTPAREN": 0xB7,  # Keypad )
    "LEFTCTRL": 0xE0,  # Keyboard Left Control
    "LEFTSHIFT": 0xE1,  # Keyboard Left Shift
    "LEFTALT": 0xE2,  # Keyboard Left Alt
    "LEFTMETA": 0xE3,  # Keyboard Left GUI
    "RIGHTCTRL": 0xE4,  # Keyboard Right Control
    "RIGHTSHIFT": 0xE5,  # Keyboard Right Shift
    "RIGHTALT": 0xE6,  # Keyboard Right Alt
    "RIGHTMETA": 0xE7,  # Keyboard Right GUI
    "MEDIA_PLAYPAUSE": 0xE8,
    "MEDIA_STOPCD": 0xE9,
    "MEDIA_PREVIOUSSONG": 0xEA,
    "MEDIA_NEXTSONG": 0xEB,
    "MEDIA_EJECTCD": 0xEC,
    "MEDIA_VOLUMEUP": 0xED,
    "MEDIA_VOLUMEDOWN": 0xEE,
    "MEDIA_MUTE": 0xEF,
    "MEDIA_WWW": 0xF0,
    "MEDIA_BACK": 0xF1,
    "MEDIA_FORWARD": 0xF2,
    "MEDIA_STOP": 0xF3,
    "MEDIA_FIND": 0xF4,
    "MEDIA_SCROLLUP": 0xF5,
    "MEDIA_SCROLLDOWN": 0xF6,
    "MEDIA_EDIT": 0xF7,
    "MEDIA_SLEEP": 0xF8,
    "MEDIA_COFFEE": 0xF9,
    "MEDIA_REFRESH": 0xFA,
    "MEDIA_CALC": 0xFB,
}
