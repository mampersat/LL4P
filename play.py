from bearlibterminal import terminal
import time

terminal.open()
terminal.printf(1, 1, 'Hello, world!')
terminal.refresh()
terminal.set("Hello again")

while terminal.read() != terminal.TK_CLOSE:
    pass

time.sleep(4)

terminal.close()