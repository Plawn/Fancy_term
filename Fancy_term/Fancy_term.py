# -*- coding: utf-8 -*-

# <-------------- colors --------------> #

class colors:
    _beginning = "\033["
    red = "31;10m"
    white = "31;97m"
    green = "32;400m"
    yellow = "33;40m"
    purple = "34;40m"
    rose = "35;40m"
    blue = "36;36m"
    reset = "\033[31;97m"
    end = "\033[m"


class substyles:
    bold = 'bold'
    faded = 'faded'
    less_faded = 'less_faded'
    underligned = 'underligned'
    blinking = 'blinking'
    background = 'background'
    normal = 'normal'

_UP = '\x1b[1A'

Colors_available = ["red", "white", "green",
                    "yellow", "purple", "rose", "blue", "reset"]


Substyles_available = ["bold", "faded", "less_faded",
                       "underligned", "blinking", "background", "normal"]
# <-------------- colors --------------> #


def printc(style, *strings, sep=''):
    print(style.str(), sep.join(strings), colors.end, sep="")


def colored_string(style, *strings, sep=''):
    return style.begin() + sep.join(strings) + colors.end


class Smart_print:
    """
            Can be used to set a style or directly used as a print function
    """

    def __init__(self, style, *args, **kwargs):
        self.default_style = Style(color=colors.white)
        self.actual_style = style
        self.prefix = kwargs.get('prefix', '')
        self.suffix = kwargs.get('suffix', '')

    def set(self, style=None):
        """
                Sets a Style for future use : Should work with any printable stuff
        """
        if style != None:
            print(_UP, style.begin(), sep="")
            self.actual_style = style
        else:
            if self.actual_style != None:
                print(colors.end, self.actual_style.begin(), _UP, sep='')
            else:
                raise Exception("no style defined")

    def use(self, style):
        self.actual_style = style

    def reset(self):
        print(_UP, colors.reset, sep="")
        self.actual_style = None

    def __call__(self, *strings):
        print(self.prefix, colors.end, self.actual_style.begin(),
              ''.join(strings), colors.end, self.suffix, sep="")


class Style:
    """
Colors available by typing print(Colors_available)
Substyles available by typing print(Substyles_available)
    """

    _sub_styles = {"bold": 1, "faded": 2, "less_faded": 3,
                   "underligned": 4, "blinking": 5, "background": 7, "normal": 0}
    default = 'normal'

    def __init__(self, *args, **kwargs):

        self.is_bold = kwargs.get(self.default, True)
        self._color = kwargs.get('color', colors.white)
        self._sub_style = ''
        self._gen_substyle(kwargs.get('substyle', [self.default]))

    def begin(self):
        return colors.end + colors._beginning + self._sub_style + self._color

    def _gen_substyle(self, sub_styles):
        L_styles = []
        for substyle in sub_styles:
            try:
                L_styles.append(str(self._sub_styles[substyle]))
            except:
                raise Exception('"{}" is not a valid format'.format(substyle))
        L_styles.sort()
        self._sub_style = ''
        for i in L_styles:
            self._sub_style += str(i) + ";"

# <-------------- test unit --------------> #
if __name__ == '__main__':
    suc = Style(color=colors.green, substyle=[substyles.bold])
    a = colored_string(suc, 'success', sep=" ")
    success_printer = Smart_print(prefix='['+a+'] ', style=Style())
    success_printer('test')
# <-------------- test unit --------------> #
