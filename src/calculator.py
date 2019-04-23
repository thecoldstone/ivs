#!/usr/bin/python
# -*- coding: utf-8 -*

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from src.staff.State import State
from src.staff.buttons import create_buttons
from src.staff.entry_input import create_entry
from src.staff.map_key_press import map_key_press
from src.staff.root import create_root


root = create_root()
state = State(create_entry(root))

create_buttons(root, lambda key: map_key_press(key, state))

root.mainloop()
