import os

import info

import re

def runstd(args, full, fullcmd, command):
    match command:
        case 'exit' | 'exitprompt' | 'E' | 'EP': info.running = False
        case 'getcwd': print(os.getcwd())
        case 'setprompt': info.prompt = args[0]
        case 'testcmd': print(full)
        case _: os.system(fullcmd)

def run(cmd):
    fullcmd = cmd
    
    alternate = cmd.split('"')
    full = []
    for idx, i in enumerate(alternate):
        if idx % 2 != 0:
            full.append(i)
        else:
            full += i.split(' ')
    
    if full[0][0] == '#':
        type = full[0][1:]
        del full[0]
        re.sub('$[a-z]', '', fullcmd)
    else:
        type = 'std'
    
    cmd = full[0]
    args = full[1:]
    
    for idx, i in enumerate(args):
        if i == '':
            del args[idx]
            del full[idx + 1]
    
    globals['run' + type](args, full, fullcmd, cmd)