from dataclasses import dataclass, fields

from pgtui.config import load_settings


@dataclass
class Bindings:
    show_help = "f1"
    open_file = "alt+o"
    exit = "alt+q"
    save = "alt+s"
    select_database = "alt+d"
    switch_layout = "alt+e"

    # Editor
    execute_query = "ctrl+enter,ctrl+full_stop"
    open_autocomplete = "ctrl+space"
    close_autocomplete = "esc"
    format_query = "alt+f"
    format_all = "alt+shift+f"
    select_query = "alt+shift+s"
    copy_selection= "alt+c"

    # Tabs
    new_tab = "alt+n"
    close_tab = "alt+w"
    next_tab = "alt+tab,alt+pagedown"
    prev_tab = "alt+shift+tab, alt+pageup"
    show_tab_1 = "alt+1"
    show_tab_2 = "alt+2"
    show_tab_3 = "alt+3"
    show_tab_4 = "alt+4"
    show_tab_5 = "alt+5"
    show_tab_6 = "alt+6"
    show_tab_7 = "alt+7"
    show_tab_8 = "alt+8"
    show_tab_9 = "alt+9"
    show_tab_10 = "alt+0"


def load_bindings() -> Bindings:
    user_bindings = load_settings().get("bindings", {})

    bindings = Bindings()
    for f in fields(bindings):
        user_value = user_bindings.get(f.name)
        if user_value and isinstance(user_value, str):
            setattr(bindings, f.name, user_value)

    return bindings


bindings = load_bindings()
