import logging

from unduckify.library import maps


class Key:
    def __init__(self) -> None:
        self.key_mod = 0
        self.key_mod_values = []
        self.key = 0
        self.key_values = []
        self.char = ""
        self.alt = False
        self.altGr = False
        self.shift = False
        self.us = ""
        self.combo = ""
        self.comboAlt = False
        self.comboAltGr = False
        self.comboShift = False

    def __repr__(self) -> str:
        return (
            f"({self.key_mod},{self.key}) "
            f"us='{self.us}', char='{self.char}', "
            f"key_mod_values={self.key_mod_values}, key_values={self.key_values}, "
            f"alt={self.alt}, altGr={self.altGr}, shift={self.shift}, combo='{self.combo}', "
            f"comboAlt={self.comboAlt}, comboAltGr={self.comboAltGr}, comboShift={self.comboShift}"
        )

    def reverse_key_mod(self) -> None:
        if "LSHIFT" in self.key_mod_values:
            self.shift = True
        if "LALT" in self.key_mod_values:
            self.alt = True
        if "RALT" in self.key_mod_values:
            self.altGr = True

    def reverse_key_mod_combo(self) -> None:
        if "LSHIFT" in self.key_mod_values:
            self.comboShift = True
        if "LALT" in self.key_mod_values:
            self.comboAlt = True
        if "RALT" in self.key_mod_values:
            self.comboAltGr = True


def reverse_combo(key_mod, key, layout):
    _k = Key()
    _k.key_mod = key_mod
    _k.key = key
    _k.key_values = [k for k, v in maps.charMap.items() if v == _k.key]
    if len(_k.key_values) == 1:
        # possible combo key
        _k.combo = _k.key_values[0]
        # check key_mod values
        _k.key_mod_values = [k for k, v in maps.modMap.items() if v == (_k.key_mod & v)]
        _k.reverse_key_mod_combo()
        # check combo
        possible_combo = list(
            filter(
                lambda x: all(
                    [
                        x["combo"] == _k.combo,
                        x["comboShift"] == _k.comboShift,
                        x["comboAlt"] == _k.comboAlt,
                        x["comboAltGr"] == _k.comboAltGr,
                    ]
                ),
                layout.get("keys", []),
            )
        )
        if len(possible_combo) > 0:
            logging.debug(f"possible combo key found!")
            return _k
        else:
            # not a combo key
            return False
    else:
        # not a combo key
        return False


def reverse_combo_key(key_mod, key, layout, previous_key: Key = None):
    if previous_key and previous_key.combo:
        # previous key is a combo key, let's try if it can be combined with the current one
        _k = previous_key
        _k.key_mod = key_mod
        _k.key = key
        _k.key_values = [k for k, v in maps.charMap.items() if v == _k.key]
        if len(_k.key_values) == 1:
            _k.us = _k.key_values[0]
            _k.key_mod_values = [k for k, v in maps.modMap.items() if v == (_k.key_mod & v)]
            _k.reverse_key_mod()
            possible_char = list(
                filter(
                    lambda x: all(
                        [
                            x["us"] == _k.us,
                            x["shift"] == _k.shift,
                            x["alt"] == _k.alt,
                            x["altGr"] == _k.altGr,
                            x["combo"] == _k.combo,
                            x["comboShift"] == _k.comboShift,
                            x["comboAlt"] == _k.comboAlt,
                            x["comboAltGr"] == _k.comboAltGr,
                        ]
                    ),
                    layout.get("keys", []),
                )
            )
            if len(possible_char) == 1:
                _k.char = possible_char[0].get("char")
                logging.debug(f"key+combo found!")
                return _k
            elif len(possible_char) > 1:
                logging.warning(f"Multiple char found for this key+combo! {possible_char}")
                logging.warning(_k)
                return False
            else:
                return False
        else:
            return False
    else:
        return False


def reverse_key(key_mod, key, layout) -> Key:
    # assume no previous combo key was found
    _k = Key()
    _k.key_mod = key_mod
    _k.key = key
    _k.key_values = [k for k, v in maps.charMap.items() if v == _k.key]
    if len(_k.key_values) == 1:
        _k.us = _k.key_values[0]
        _k.key_mod_values = [k for k, v in maps.modMap.items() if v == (_k.key_mod & v)]
        _k.reverse_key_mod()
        possible_char = list(
            filter(
                lambda x: all(
                    [
                        x["us"] == _k.us,
                        x["shift"] == _k.shift,
                        x["alt"] == _k.alt,
                        x["altGr"] == _k.altGr,
                        x["combo"] == _k.combo,
                        x["comboShift"] == _k.comboShift,
                        x["comboAlt"] == _k.comboAlt,
                        x["comboAltGr"] == _k.comboAltGr,
                    ]
                ),
                layout.get("keys", []),
            )
        )
        if len(possible_char) == 1:
            _k.char = possible_char[0].get("char")
            logging.debug(f"key found!")
            return _k
        elif len(possible_char) > 1:
            logging.warning(f"Multiple char found for this key! {possible_char}")
            logging.warning(_k)
            return False
        else:
            return False
    elif len(_k.key_values) > 1:
        # edge case: space value is duplicated in charMap
        if " " in _k.key_values and "Space" in _k.key_values:
            # ignore key_mod
            _k.char = " "
            _k.us = " "
            logging.debug(f"space found!")
            return _k
        else:
            return False
    else:
        return False
