from enum import IntEnum


class Key(IntEnum):
    LOGO = 0
    CAPS = 1
    NUM = 2
    SCROLL = 3
    GAME = 4
    BACKLIGHT = 5
    MUTE = 6
    PLAY = 7
    STOP = 8
    PREV = 9
    NEXT = 10
    F1 = 11
    F2 = 12
    F3 = 13
    F4 = 14
    F5 = 15
    F6 = 16
    F7 = 17
    F8 = 18
    F9 = 19
    F10 = 20
    F11 = 21
    F12 = 22
    SHIFT_LEFT = 23
    CTRL_LEFT = 24
    WIN_LEFT = 25
    ALT_LEFT = 26
    ALT_RIGHT = 27
    WIN_RIGHT = 28
    CTRL_RIGHT = 29
    SHIFT_RIGHT = 30
    MENU = 31
    ARROW_UP = 32
    ARROW_LEFT = 33
    ARROW_DOWN = 34
    ARROW_RIGHT = 35
    NUM_1 = 36
    NUM_2 = 37
    NUM_3 = 38
    NUM_4 = 39
    NUM_5 = 40
    NUM_6 = 41
    NUM_7 = 42
    NUM_8 = 43
    NUM_9 = 44
    NUM_0 = 45
    NUM_DOT = 46
    NUM_ENTER = 47
    NUM_PLUS = 48
    NUM_MINUS = 49
    NUM_ASTERISK = 50
    NUM_SLASH = 51
    NUM_LOCK = 52
    ESC = 53
    SCROLL_LOCK = 54
    INSERT = 55
    DEL = 56
    HOME = 57
    END = 58
    PAGE_UP = 59
    PAGE_DOWN = 60
    PRINT_SCREEN = 61
    PAUSE_BREAK = 62
    N1 = 63
    N2 = 64
    N3 = 65
    N4 = 66
    N5 = 67
    N6 = 68
    N7 = 69
    N8 = 70
    N9 = 71
    N0 = 72
    TAB = 73
    CAPS_LOCK = 74
    SPACE = 75
    BACKSPACE = 76
    ENTER = 77
    A = 78
    B = 79
    C = 80
    D = 81
    E = 82
    F = 83
    G = 84
    H = 85
    I = 86
    J = 87
    K = 88
    L = 89
    M = 90
    N = 91
    O = 92
    P = 93
    Q = 94
    R = 95
    S = 96
    T = 97
    U = 98
    V = 99
    W = 100
    X = 101
    Y = 102
    Z = 103
    UNKNOWN = 104
    EGRAVE = 105
    EAIGU = 106
    SEMICOLON = 107
    AGRAVE = 108
    DOLLAR = 109
    APOSTROPHE = 110
    DEGREE = 111
    BACKSLASH = 112
    COMMA = 113
    DOT = 114
    MINUS = 115
    OPEN_BRACKET = 116
    CLOSE_BRACKET = 117
    INDICATORS = 1
    TIDLE = 118


key_groups = {
    "logo": (
        Key.LOGO
    ),
    "indicators": (
        Key.CAPS, Key.NUM, Key.SCROLL, Key.GAME, Key.BACKLIGHT
    ),
    "multimedia": (
        Key.MUTE, Key.PLAY, Key.STOP, Key.PREV, Key.NEXT
    ),
    "fkeys": (
        Key.F1, Key.F2, Key.F3, Key.F4, Key.F5, Key.F6, Key.F7, Key.F8, Key.F9, Key.F10, Key.F11, Key.F12
    ),
    "modifiers": (
        Key.SHIFT_LEFT, Key.CTRL_LEFT, Key.WIN_LEFT, Key.ALT_LEFT, Key.ALT_RIGHT, Key.WIN_RIGHT, Key.MENU,
        Key.CTRL_RIGHT, Key.SHIFT_RIGHT
    ),
    "arrows": (
        Key.ARROW_UP, Key.ARROW_LEFT, Key.ARROW_DOWN, Key.ARROW_RIGHT
    ),
    "numeric": (
        Key.NUM_1, Key.NUM_2, Key.NUM_3, Key.NUM_4, Key.NUM_6, Key.NUM_7, Key.NUM_8, Key.NUM_9, Key.NUM_0, Key.NUM_DOT,
        Key.NUM_ENTER, Key.NUM_PLUS, Key.NUM_MINUS, Key.NUM_ASTERISK, Key.NUM_SLASH, Key.NUM_LOCK
    ),
    "functions": (
        Key.ESC, Key.SCROLL_LOCK, Key.INSERT, Key.DEL, Key.HOME, Key.END, Key.PAGE_UP, Key.PAGE_DOWN, Key.PRINT_SCREEN,
        Key.PAUSE_BREAK
    ),
    "keys": (
        Key.LOGO,
        Key.CAPS, Key.NUM, Key.SCROLL, Key.GAME, Key.BACKLIGHT,
        Key.MUTE, Key.PLAY, Key.STOP, Key.PREV, Key.NEXT,
        Key.F1, Key.F2, Key.F3, Key.F4, Key.F5, Key.F6, Key.F7, Key.F8, Key.F9, Key.F10, Key.F11, Key.F12,
        Key.SHIFT_LEFT, Key.CTRL_LEFT, Key.WIN_LEFT, Key.ALT_LEFT, Key.ALT_RIGHT, Key.WIN_RIGHT, Key.MENU,
        Key.CTRL_RIGHT, Key.SHIFT_RIGHT,
        Key.ARROW_UP, Key.ALT_LEFT, Key.ARROW_DOWN, Key.ALT_RIGHT,
        Key.NUM_1, Key.NUM_2, Key.NUM_3, Key.NUM_4, Key.NUM_6, Key.NUM_7, Key.NUM_8, Key.NUM_9, Key.NUM_0, Key.NUM_DOT,
        Key.NUM_ENTER, Key.NUM_PLUS, Key.NUM_MINUS, Key.NUM_ASTERISK, Key.NUM_SLASH, Key.NUM_LOCK,
        Key.ESC, Key.SCROLL_LOCK, Key.INSERT, Key.DEL, Key.HOME, Key.END, Key.PAGE_UP, Key.PAGE_DOWN, Key.PRINT_SCREEN,
        Key.PAUSE_BREAK,
        Key.TAB, Key.CAPS_LOCK, Key.SPACE, Key.BACKSPACE, Key.ENTER, Key.A, Key.B, Key.C, Key.D, Key.E, Key.F, Key.G,
        Key.H, Key.I, Key.J, Key.K, Key.L, Key.M, Key.N, Key.O, Key.P, Key.Q, Key.R, Key.S, Key.T, Key.U, Key.V, Key.W,
        Key.X, Key.Y, Key.Z, Key.UNKNOWN, Key.EGRAVE, Key.EAIGU, Key.SEMICOLON, Key.AGRAVE, Key.DOLLAR, Key.APOSTROPHE,
        Key.DEGREE, Key.BACKSLASH, Key.COMMA, Key.DOT, Key.MINUS, Key.OPEN_BRACKET, Key.CLOSE_BRACKET, Key.TIDLE
    ),
    "gaming": (
        Key.W, Key.A, Key.S, Key.D,
        Key.CTRL_LEFT, Key.SPACE
    )
}


class AddressGroup(IntEnum):
    LOGO = 0
    INDICATORS = 1
    MULTIMEDIA = 2
    KEYS = 3


address_group_data_size = {
    AddressGroup.LOGO: 20,
    AddressGroup.INDICATORS: 64,
    AddressGroup.MULTIMEDIA: 64,
    AddressGroup.KEYS: 64
}

address_group_prefix = {
    AddressGroup.LOGO: [
        0x11,
        0xff,
        0x0c,
        0x3a,
        0x00,
        0x10,
        0x00,
        0x01
    ],
    AddressGroup.INDICATORS: [
        0x12,
        0xff,
        0x0c,
        0x3a,
        0x00,
        0x40,
        0x00,
        0x05
    ],
    AddressGroup.MULTIMEDIA: [
        0x12,
        0xff,
        0x0c,
        0x3a,
        0x00,
        0x02,
        0x00,
        0x05
    ],
    AddressGroup.KEYS: [
        0x12,
        0xff,
        0x0c,
        0x3a,
        0x00,
        0x01,
        0x00,
        0x0e
    ]
}

key_values = {
    # logo
    Key.LOGO: {"address": 0x01, "address_group": AddressGroup.LOGO},
    # indicators
    Key.BACKLIGHT: {"address": 0x01, "address_group": AddressGroup.INDICATORS},
    Key.GAME: {"address": 0x02, "address_group": AddressGroup.INDICATORS},
    Key.CAPS: {"address": 0x03, "address_group": AddressGroup.INDICATORS},
    Key.SCROLL: {"address": 0x04, "address_group": AddressGroup.INDICATORS},
    Key.NUM: {"address": 0x05, "address_group": AddressGroup.INDICATORS},
    # multimedia
    Key.NEXT: {"address": 0xb5, "address_group": AddressGroup.MULTIMEDIA},
    Key.PREV: {"address": 0xb6, "address_group": AddressGroup.MULTIMEDIA},
    Key.STOP: {"address": 0xb7, "address_group": AddressGroup.MULTIMEDIA},
    Key.PLAY: {"address": 0xcd, "address_group": AddressGroup.MULTIMEDIA},
    Key.MUTE: {"address": 0xe2, "address_group": AddressGroup.MULTIMEDIA},
    # keys
    Key.A: {"address": 0x04, "address_group": AddressGroup.KEYS},
    Key.B: {"address": 0x05, "address_group": AddressGroup.KEYS},
    Key.C: {"address": 0x06, "address_group": AddressGroup.KEYS},
    Key.D: {"address": 0x07, "address_group": AddressGroup.KEYS},
    Key.E: {"address": 0x08, "address_group": AddressGroup.KEYS},
    Key.F: {"address": 0x09, "address_group": AddressGroup.KEYS},
    Key.G: {"address": 0x0a, "address_group": AddressGroup.KEYS},
    Key.H: {"address": 0x0b, "address_group": AddressGroup.KEYS},
    Key.I: {"address": 0x0c, "address_group": AddressGroup.KEYS},
    Key.J: {"address": 0x0d, "address_group": AddressGroup.KEYS},
    Key.K: {"address": 0x0e, "address_group": AddressGroup.KEYS},
    Key.L: {"address": 0x0f, "address_group": AddressGroup.KEYS},
    Key.M: {"address": 0x10, "address_group": AddressGroup.KEYS},
    Key.N: {"address": 0x11, "address_group": AddressGroup.KEYS},
    Key.O: {"address": 0x12, "address_group": AddressGroup.KEYS},
    Key.P: {"address": 0x13, "address_group": AddressGroup.KEYS},
    Key.Q: {"address": 0x14, "address_group": AddressGroup.KEYS},
    Key.R: {"address": 0x15, "address_group": AddressGroup.KEYS},
    Key.S: {"address": 0x16, "address_group": AddressGroup.KEYS},
    Key.T: {"address": 0x17, "address_group": AddressGroup.KEYS},
    Key.U: {"address": 0x18, "address_group": AddressGroup.KEYS},
    Key.V: {"address": 0x19, "address_group": AddressGroup.KEYS},
    Key.W: {"address": 0x1a, "address_group": AddressGroup.KEYS},
    Key.X: {"address": 0x1b, "address_group": AddressGroup.KEYS},
    Key.Z: {"address": 0x1c, "address_group": AddressGroup.KEYS},
    Key.Y: {"address": 0x1d, "address_group": AddressGroup.KEYS},
    Key.N1: {"address": 0x1e, "address_group": AddressGroup.KEYS},
    Key.N2: {"address": 0x1f, "address_group": AddressGroup.KEYS},
    Key.N3: {"address": 0x20, "address_group": AddressGroup.KEYS},
    Key.N4: {"address": 0x21, "address_group": AddressGroup.KEYS},
    Key.N5: {"address": 0x22, "address_group": AddressGroup.KEYS},
    Key.N6: {"address": 0x23, "address_group": AddressGroup.KEYS},
    Key.N7: {"address": 0x24, "address_group": AddressGroup.KEYS},
    Key.N8: {"address": 0x25, "address_group": AddressGroup.KEYS},
    Key.N9: {"address": 0x26, "address_group": AddressGroup.KEYS},
    Key.N0: {"address": 0x27, "address_group": AddressGroup.KEYS},
    Key.ENTER: {"address": 0x28, "address_group": AddressGroup.KEYS},
    Key.ESC: {"address": 0x29, "address_group": AddressGroup.KEYS},
    Key.BACKSPACE: {"address": 0x2a, "address_group": AddressGroup.KEYS},
    Key.TAB: {"address": 0x2b, "address_group": AddressGroup.KEYS},
    Key.SPACE: {"address": 0x2c, "address_group": AddressGroup.KEYS},
    Key.APOSTROPHE: {"address": 0x2d, "address_group": AddressGroup.KEYS},
    Key.TIDLE: {"address": 0x2e, "address_group": AddressGroup.KEYS},
    Key.OPEN_BRACKET: {"address": 0x2f, "address_group": AddressGroup.KEYS},
    Key.CLOSE_BRACKET: {"address": 0x30, "address_group": AddressGroup.KEYS},
    Key.UNKNOWN: {"address": 0x31, "address_group": AddressGroup.KEYS},
    Key.DOLLAR: {"address": 0x32, "address_group": AddressGroup.KEYS},
    Key.EAIGU: {"address": 0x33, "address_group": AddressGroup.KEYS},
    Key.SEMICOLON: {"address": 0x33, "address_group": AddressGroup.KEYS},
    Key.AGRAVE: {"address": 0x34, "address_group": AddressGroup.KEYS},
    Key.DEGREE: {"address": 0x35, "address_group": AddressGroup.KEYS},
    Key.COMMA: {"address": 0x36, "address_group": AddressGroup.KEYS},
    Key.DOT: {"address": 0x37, "address_group": AddressGroup.KEYS},
    Key.MINUS: {"address": 0x38, "address_group": AddressGroup.KEYS},
    Key.CAPS_LOCK: {"address": 0x39, "address_group": AddressGroup.KEYS},
    Key.F1: {"address": 0x3a, "address_group": AddressGroup.KEYS},
    Key.F2: {"address": 0x3b, "address_group": AddressGroup.KEYS},
    Key.F3: {"address": 0x3c, "address_group": AddressGroup.KEYS},
    Key.F4: {"address": 0x3d, "address_group": AddressGroup.KEYS},
    Key.F5: {"address": 0x3e, "address_group": AddressGroup.KEYS},
    Key.F6: {"address": 0x3f, "address_group": AddressGroup.KEYS},
    Key.F7: {"address": 0x40, "address_group": AddressGroup.KEYS},
    Key.F8: {"address": 0x41, "address_group": AddressGroup.KEYS},
    Key.F9: {"address": 0x42, "address_group": AddressGroup.KEYS},
    Key.F10: {"address": 0x43, "address_group": AddressGroup.KEYS},
    Key.F11: {"address": 0x44, "address_group": AddressGroup.KEYS},
    Key.F12: {"address": 0x45, "address_group": AddressGroup.KEYS},
    Key.PRINT_SCREEN: {"address": 0x46, "address_group": AddressGroup.KEYS},
    Key.SCROLL_LOCK: {"address": 0x47, "address_group": AddressGroup.KEYS},
    Key.PAUSE_BREAK: {"address": 0x48, "address_group": AddressGroup.KEYS},
    Key.INSERT: {"address": 0x49, "address_group": AddressGroup.KEYS},
    Key.HOME: {"address": 0x4a, "address_group": AddressGroup.KEYS},
    Key.PAGE_UP: {"address": 0x4b, "address_group": AddressGroup.KEYS},
    Key.DEL: {"address": 0x4c, "address_group": AddressGroup.KEYS},
    Key.END: {"address": 0x4d, "address_group": AddressGroup.KEYS},
    Key.PAGE_DOWN: {"address": 0x4e, "address_group": AddressGroup.KEYS},
    Key.ARROW_RIGHT: {"address": 0x4f, "address_group": AddressGroup.KEYS},
    Key.ARROW_LEFT: {"address": 0x50, "address_group": AddressGroup.KEYS},
    Key.ARROW_DOWN: {"address": 0x51, "address_group": AddressGroup.KEYS},
    Key.ARROW_UP: {"address": 0x52, "address_group": AddressGroup.KEYS},
    Key.NUM_LOCK: {"address": 0x53, "address_group": AddressGroup.KEYS},
    Key.NUM_SLASH: {"address": 0x54, "address_group": AddressGroup.KEYS},
    Key.NUM_ASTERISK: {"address": 0x55, "address_group": AddressGroup.KEYS},
    Key.NUM_MINUS: {"address": 0x56, "address_group": AddressGroup.KEYS},
    Key.NUM_PLUS: {"address": 0x57, "address_group": AddressGroup.KEYS},
    Key.NUM_ENTER: {"address": 0x58, "address_group": AddressGroup.KEYS},
    Key.NUM_1: {"address": 0x59, "address_group": AddressGroup.KEYS},
    Key.NUM_2: {"address": 0x5a, "address_group": AddressGroup.KEYS},
    Key.NUM_3: {"address": 0x5b, "address_group": AddressGroup.KEYS},
    Key.NUM_4: {"address": 0x5c, "address_group": AddressGroup.KEYS},
    Key.NUM_5: {"address": 0x5d, "address_group": AddressGroup.KEYS},
    Key.NUM_6: {"address": 0x5e, "address_group": AddressGroup.KEYS},
    Key.NUM_7: {"address": 0x5f, "address_group": AddressGroup.KEYS},
    Key.NUM_8: {"address": 0x60, "address_group": AddressGroup.KEYS},
    Key.NUM_9: {"address": 0x61, "address_group": AddressGroup.KEYS},
    Key.NUM_0: {"address": 0x62, "address_group": AddressGroup.KEYS},
    Key.NUM_DOT: {"address": 0x63, "address_group": AddressGroup.KEYS},
    Key.BACKSLASH: {"address": 0x64, "address_group": AddressGroup.KEYS},
    Key.MENU: {"address": 0x65, "address_group": AddressGroup.KEYS},
    Key.CTRL_LEFT: {"address": 0xe0, "address_group": AddressGroup.KEYS},
    Key.SHIFT_LEFT: {"address": 0xe1, "address_group": AddressGroup.KEYS},
    Key.ALT_LEFT: {"address": 0xe2, "address_group": AddressGroup.KEYS},
    Key.WIN_LEFT: {"address": 0xe3, "address_group": AddressGroup.KEYS},
    Key.CTRL_RIGHT: {"address": 0xe4, "address_group": AddressGroup.KEYS},
    Key.SHIFT_RIGHT: {"address": 0xe5, "address_group": AddressGroup.KEYS},
    Key.ALT_RIGHT: {"address": 0xe6, "address_group": AddressGroup.KEYS},
    Key.WIN_RIGHT: {"address": 0xe7, "address_group": AddressGroup.KEYS},
    # unknown
    Key.EGRAVE: {"address": 0x00, "address_group": AddressGroup.KEYS}
}
