# adopted from TerminalView

_KEY_MAP = {
    "enter": "\r",
    "backspace": "\x7f",
    "tab": "\t",
    "space": " ",
    "escape": "\x1b",
    "down": "\x1b[B",
    "up": "\x1b[A",
    "right": "\x1b[C",
    "left": "\x1b[D",
    "home": "\x1b[1~",
    "end": "\x1b[4~",
    "pageup": "\x1b[5~",
    "pagedown": "\x1b[6~",
    "delete": "\x1b[3~",
    "insert": "\x1b[2~",
    "f1": "\x1bOP",
    "f2": "\x1bOQ",
    "f3": "\x1bOR",
    "f4": "\x1bOS",
    "f5": "\x1b[15~",
    "f6": "\x1b[17~",
    "f7": "\x1b[18~",
    "f8": "\x1b[19~",
    "f9": "\x1b[20~",
    "f10": "\x1b[21~",
    "f12": "\x1b[24~",
    "bracketed_paste_mode_start": "\x1b[200~",
    "bracketed_paste_mode_end": "\x1b[201~",
}

# _APP_KEY_MAP = {
#     "down": "\x1bOB",
#     "up": "\x1bOA",
#     "right": "\x1bOC",
#     "left": "\x1bOD",
# }

_CTRL_KEY_MAP = {
    "up": "\x1b[1;5A",
    "down": "\x1b[1;5B",
    "right": "\x1b[1;5C",
    "left": "\x1b[1;5D",
    "@": "\x00",
    "`": "\x00",
    "[": "\x1b",
    "{": "\x1b",
    "\\": "\x1c",
    "|": "\x1c",
    "]": "\x1d",
    "}": "\x1d",
    "^": "\x1e",
    "~": "\x1e",
    "_": "\x1f",
    "?": "\x7f",
}

_ALT_KEY_MAP = {
    "up": "\x1b[1;3A",
    "down": "\x1b[1;3B",
    "right": "\x1b[1;3C",
    "left": "\x1b[1;3D",
}


def _get_ctrl_combination_key_code(key):
    key = key.lower()
    if key in _CTRL_KEY_MAP:
        return _CTRL_KEY_MAP[key]
    elif len(key) == 1:
        c = ord(key)
        if (c >= 97) and (c <= 122):
            c = c - ord('a') + 1
            return chr(c)
        return _get_key_code(key)

    return _get_key_code(key)


def _get_alt_combination_key_code(key):
    key = key.lower()
    if key in _ALT_KEY_MAP:
        return _ALT_KEY_MAP[key]

    code = _get_key_code(key)
    return "\x1b" + code


# def _get_app_key_code(key):
#     if key in _APP_KEY_MAP:
#         return _APP_KEY_MAP[key]
#     return _get_key_code(key)


def _get_key_code(key):
    if key in _KEY_MAP:
        return _KEY_MAP[key]
    return key


def get_key_code(key, ctrl=False, alt=False, shift=False):
    """
    Send keypress to the shell
    """
    if ctrl:
        keycode = _get_ctrl_combination_key_code(key)
    elif alt:
        keycode = _get_alt_combination_key_code(key)
    else:
        keycode = _get_key_code(key)

    return keycode
