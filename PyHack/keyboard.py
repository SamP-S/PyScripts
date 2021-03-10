import ctypes

key_state = {
    "isDown"    : 0b1000000000000000,
    "newPress"  : 0b0000000000000001
}

key_codes = {
    # MOUSE KEYS
    "VK_LBUTTON": 0x01,
    "VK_RBUTTON": 0x02,
    "VK_CANCEL": 0x03,
    "VK_MBUTTON": 0x04,
    "VK_XBUTTON1": 0x05,
    "VK_XBUTTON2": 0x06,
    # MODIFIERS & SPECIAL
    "VK_BACK": 0x08,
    "VK_TAB": 0x09,
    "VK_CLEAR": 0x0c,
    "VK_RETURN": 0x0d,
    "VK_SHIFT": 0x10,
    "VK_CONTROL": 0x11,
    "VK_MENU": 0x12,        # ALT KEY
    "VK_PAUSE": 0x13,
    "VK_CAPITAL": 0x14,
    "VK_ESCAPE": 0x1B,
    "VK_SPACE": 0x20,
    "VK_PRIOR": 0x21,       # PAGE UP
    "VK_NEXT": 0x22,        # PAGE DOWN
    "VK_END": 0x23,
    "VK_HOME": 0x24,
    # ARROW KEYS
    "VK_LEFT": 0x25,
    "VK_UP": 0x26,
    "VK_RIGHT": 0x27,
    "VK_DOWN": 0x28,
    # SPECIAL KEYS
    "VK_SELECT": 0x29,      # SELECT KEY
    "VK_PRINT": 0x2a,
    "VK_EXECUTE": 0x2b,     # EXECTUTE KEY
    "VK_SNAPSHOT": 0x2c,    # PRINT SCREEN KEY 
    "VK_INSERT": 0x2d,
    "VK_DELETE": 0x2e,
    "VK_HELP": 0x2f,
    # NUMBERS
    "VK_0": 0x30,
    "VK_1": 0x31,
    "VK_2": 0x32,
    "VK_3": 0x33,
    "VK_4": 0x34,
    "VK_5": 0x35,
    "VK_6": 0x36,
    "VK_7": 0x37,
    "VK_8": 0x38,
    "VK_9": 0x39,
    # ALPHABET
    "VK_A": 0x41,
    "VK_B": 0x42,
    "VK_C": 0x43,
    "VK_D": 0x44,
    "VK_E": 0x45,
    "VK_F": 0x46,
    "VK_G": 0x47,
    "VK_H": 0x48,
    "VK_I": 0x49,
    "VK_J": 0x4a,
    "VK_K": 0x4b,
    "VK_L": 0x4c,
    "VK_M": 0x4d,
    "VK_N": 0x4e,
    "VK_O": 0x4f,
    "VK_P": 0x50,
    "VK_Q": 0x51,
    "VK_R": 0x52,
    "VK_S": 0x53,
    "VK_T": 0x54,
    "VK_U": 0x55,
    "VK_V": 0x56,
    "VK_W": 0x57,
    "VK_X": 0x58,
    "VK_Y": 0x59,
    "VK_Z": 0x5a,
    # NATURAL KEYS
    "VK_LWIN": 0x5b,    # LEFT WINDOWS KEY (NATURAL)
    "VK_RWIN": 0x5c,    # RIGHT WINDOWS KEY (NATURAL)
    "VK_APPS": 0x5d,    # APPLICATIONS KEY (NATURAL)
    "VK_SLEEP": 0x5f,
    # NUMPAD DIGITS
    "VK_NUMBERPAD0": 0x60,
    "VK_NUMBERPAD1": 0x61,
    "VK_NUMBERPAD2": 0x62,
    "VK_NUMBERPAD3": 0x63,
    "VK_NUMBERPAD4": 0x64,
    "VK_NUMBERPAD5": 0x65,
    "VK_NUMBERPAD6": 0x66,
    "VK_NUMBERPAD7": 0x67,
    "VK_NUMBERPAD8": 0x68,
    "VK_NUMBERPAD9": 0x69,
    # NUMPAD MATHAMTICAL OPERATORS
    "VK_MULTIPLY": 0x6a,
    "VK_ADD": 0x6b,
    "VK_SEPARATOR": 0x6c,
    "VK_SUBTRACT": 0x6d,
    "VK_DECIMAL": 0x6e,
    "VK_DIVIDE": 0x6f,
    # FUNCTION KEYS
    "VK_F1": 0x70,
    "VK_F2": 0x71,
    "VK_F3": 0x72,
    "VK_F4": 0x73,
    "VK_F5": 0x74,
    "VK_F6": 0x75,
    "VK_F7": 0x76,
    "VK_F8": 0x77,
    "VK_F9": 0x78,
    "VK_F10": 0x79,
    "VK_F11": 0x7a,
    "VK_F12": 0x7b,
    "VK_F13": 0x7c,
    "VK_F14": 0x7d,
    "VK_F15": 0x7e,
    "VK_F16": 0x7f,
    "VK_F17": 0x80,
    "VK_F18": 0x81,
    "VK_F19": 0x82,
    "VK_F20": 0x83,
    "VK_F21": 0x84,
    "VK_F22": 0x85,
    "VK_F23": 0x86,
    "VK_F24": 0x87,
    # SPECIAL
    "VK_NUMLOCK": 0x90,
    "VK_SCROLL": 0x91,
    # MODIFIERS
    "VK_LSHIFT": 0xa0,
    "VK_RSHIFT": 0xa1,
    "VK_LCONTROL": 0xa2,
    "VK_RCONTROL": 0xa3,
    # MENU
    "VK_LMENU": 0xa4,
    "VK_RMENU": 0xa5,
    # BROWSER
    # VOlUME
    # MEDIA
    # PUNCTUATION
    "VK_OEM_1": 0xba,       #  ; : 
    "VK_OEM_PLUS": 0xbb,    #  = +
    "VK_OEM_COMMA": 0xbc,   #  , <
    "VK_OEM_MINUS": 0xbd,   #  - _
    "VK_OEM_PERIOD": 0xbe,  #  . >
    "VK_OEM_2": 0xbf,       #  / ?
    "VK_OEM_3": 0xc0,       #  ` ¬
    "VK_OEM_4": 0xdb,       #  [ {
    "VK_OEM_5": 0xdc,       #  \ |
    "VK_OEM_6": 0xdd,       #  ] }
    "VK_OEM_7": 0xde,       #  ' @
    "VK_OEM_8": 0xdf,       #  # ~
}

class input_keyboard:

    def __init__(self):
        self.u32 = ctypes.WinDLL('User32.dll')
        self.u32.GetKeyState.argtypes = [ctypes.wintypes.INT]
        self.u32.GetKeyState.restype = ctypes.wintypes.SHORT
        self.u32.GetAsyncKeyState.argtypes = [ctypes.wintypes.INT]
        self.u32.GetAsyncKeyState.restype = ctypes.wintypes.SHORT

    def get_key_state(self, nVirtKey):
        # reads current key state from thread
        # args: (INT) nVirtKey = ascii value of keyboard character
        # return: (SHORT) state of key
        return self.u32.GetKeyState(nVirtKey)

    def get_async_key_state(self, vKey):
        # gets key state at time of function call
        # args: (INT) vKey = virtual-key code of desired key
        # return: (SHORT) state of key
        return self.u32.GetAsyncKeyState(vKey)

def main():
    keyboard = input_keyboard()
    while True:
        alt_state = keyboard.get_async_key_state(key_codes["VK_MENU"])
        q_state = keyboard.get_async_key_state(key_codes["VK_Q"])
        if alt_state > 1 and q_state > 1:
            break

if __name__ == "__main__":
    main()
    print("done!")