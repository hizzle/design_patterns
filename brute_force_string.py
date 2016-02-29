#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Brute-force string generation
# Copyright (C) 2011 Radek Pazdera

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


def next(string):
    """ Get next sequence of characters.

    It treat characters as numbers (0-255). It tries to increment
    character at the first position. If it fails, new character is
    added to the back of the list.

    It's basicaly a number with base = 256.

    :param string: A list of characters (can be empty).
    :type string: list
    :return: Next list of characters in the sequence
    :rettype: list
    """
    if len(string) <= 0:
        string.append(chr(0))
    else:
        string[0] = chr((ord(string[0]) + 1) % 256)
        if ord(string[0]) is 0:
            return list(string[0]) + next(string[1:])
    return string

def main():
    sequence = list()
    while True:
        sequence = next(sequence)
        print sequence

if __name__ == "__main__":
    main()

