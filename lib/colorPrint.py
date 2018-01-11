from colorama import  init, Fore, Back, Style

class ColorPrint():
    '''
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    '''

    def __init__(self):
        # TODO IDEA 开启后终端无颜色 ，原因不明
        # init(autoreset=True)
        self.idea=True

    def print_BLACK(self,s):
        print(Fore.BLACK+s+Fore.RESET)

    def print_RED(self,s):
        print(Fore.RED+s+Fore.RESET)

    def print_GREEN(self,s):
        print(Fore.GREEN+s+Fore.RESET)

    def print_YELLOW(self,s):
        print(Fore.YELLOW+s+Fore.RESET)

    def print_BLUE(self,s):
        print(Fore.BLUE+s+Fore.RESET)

    def print_MAGENTA(self,s):
        print(Fore.MAGENTA+s+Fore.RESET)

    def print_CYAN(self,s):
        print(Fore.CYAN+s+Fore.RESET)

    def print_WHITE(self,s):
        print(Fore.WHITE+s+Fore.RESET)

    def print_RESET(self,s):
        print(s)
if __name__ == '__main__':
    cp=ColorPrint()
    cp.print_RED("Asd")
    cp.print_GREEN("qweqwe")
    print("asd")

