from runcmd import run
import os

import info
info.init()

while info.running:
    text = input(info.prompt.format(path=os.getcwd()))
    if text in ['exitprompt', 'exit']: break
    run(text)
    if not info.running: break