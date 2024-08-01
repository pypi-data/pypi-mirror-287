import importlib.resources as pkg_resources
import json
import logging


def get_possible_layouts():
    # get list of possible keyboard layouts
    possible_layouts = set()
    with pkg_resources.path("unduckify.library", "mac") as mac_path:
        for file_name in mac_path.glob("*.json"):
            possible_layouts.add(file_name.stem)
    with pkg_resources.path("unduckify.library", "win") as win_path:
        for file_name in win_path.glob("*.json"):
            possible_layouts.add(file_name.stem)
    return list(possible_layouts)


def load_layout(system, layout):
    try:
        with pkg_resources.open_text(f"unduckify.library.{system}", f"{layout}.json") as f:
            return json.load(f)
    except Exception:
        logging.exception("Error loading layout")
        exit()
