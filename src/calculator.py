#!/usr/bin/python
# -*- coding: utf-8 -*

from src.staff.State import State
from src.staff.buttons import create_buttons
from src.staff.entry_input import create_entry
from src.staff.map_key_press import map_key_press
from src.staff.root import create_root


root = create_root()
state = State(create_entry(root))

create_buttons(root, lambda key: map_key_press(key, state))

root.mainloop()
