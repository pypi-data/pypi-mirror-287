import sys
import cursor
from colorama import Cursor
from colorama import just_fix_windows_console, Fore, Back, Style


class SingleLine(object):

    clear_eol = '\033[K'

    def __init__(self, single_line=True, message_when_done=None, stream=sys.stdout):
        self.single_line = single_line
        self.message_when_done = '' if not message_when_done else message_when_done
        self.stream = stream
        just_fix_windows_console()

    def __enter__(self):
        if self.stream.isatty():
            cursor.hide()
            if self.single_line:
                # ensure subsequent print replaces our blank line
                print('')
        return self

    def __exit__(self, *args):
        if self.stream.isatty():
            if self.single_line:
                self.print(self.message_when_done)
            cursor.show()

    def print(self, message, color=None):
        if self.single_line:
            print(f'{Cursor.UP(1)}{self.clear_eol}', end='', file=self.stream)
            if not color:
                color = {'fore': Fore.RESET, 'back': Back.RESET, 'style': Style.NORMAL}
            _color = color.get('fore', Fore.RESET) + color.get('back', Back.RESET) + color.get('style', Style.NORMAL)
            _message = f'{_color}{message}{Style.RESET_ALL}'
        else:
            _message = message
        print(_message, file=self.stream, flush=True)
