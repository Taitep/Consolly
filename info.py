from click import prompt


def init():
    global running, prompt
    running = True
    prompt = ' > '