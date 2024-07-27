class progressbar:
    def basic(sleeptime):
        import sys
        import time
        total_length = 50
        progress_bar = [' '] * total_length
        progress_bar[0] = '█'
        sys.stdout.write('[' + ''.join(progress_bar) + ']')
        sys.stdout.flush()
        for i in range(1, total_length):
            time.sleep(sleeptime)
            progress_bar[i] = '█'
            sys.stdout.write('\r[' + ''.join(progress_bar) + ']')
            sys.stdout.flush()
        print()

    def settable(sleeptime, character):
        import sys
        import time
        total_length = 50
        progress_bar = [' '] * total_length
        progress_bar[0] = character
        sys.stdout.write('[' + ''.join(progress_bar) + ']')
        sys.stdout.flush()
        for i in range(1, total_length):
            time.sleep(sleeptime)
            progress_bar[i] = character
            sys.stdout.write('\r[' + ''.join(progress_bar) + ']')
            sys.stdout.flush()
        print()
    def normal(sleeptime):
        import time
        t = 60
        start = time.perf_counter()
        for i in range(t + 1):
            finsh = "▓" * i
            need_do = "-" * (t - i)
            progress = (i / t) * 100
            dur = time.perf_counter() - start
            print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="")
            time.sleep(sleeptime)
class loading_animation:
    def slash(sleeptime):
        import sys
        import time
        spinner_chars =['/','|','\\','-']
        spinner_position = 0
        sys.stdout.write('\r' + ' ' * 50)
        sys.stdout.flush()
    def dots(sleeptime):
        import sys
        import time
        spinner_chars = ['', '.', '..', '...']
        spinner_position = 0
        sys.stdout.write('\r' + ' ' * 50)
        sys.stdout.flush()
        sys.stdout.write('\r\t\t\t\t\t\t\t' + spinner_chars[spinner_position])
        sys.stdout.flush()
        time.sleep(sleeptime)
    def settable(sleeptime,character,word):
        import sys
        import time
        spinner_chars = character
        spinner_position = 0
        sys.stdout.write('\r' + ' ' * 50)
        sys.stdout.flush()
        if character == 'None':
            sys.stdout.write('\r\t\t\t\t\t\t\t' + spinner_chars[spinner_position])
            sys.stdout.flush()
            spinner_position = (spinner_position + 1) % len(spinner_chars)
            time.sleep(sleeptime)
        else:
            sys.stdout.write('\r\t\t\t\t\t\t\t' + word + spinner_chars[spinner_position])
            sys.stdout.flush()
            spinner_position = (spinner_position + 1) % len(spinner_chars)
            time.sleep(sleeptime)
class wordcolor:
    def red(word):
        print('\033[91m',word)
    def yellow(word):
        print('\033[92m',word)
    def white(word):
        print('\033[96m',word)
    def normal(word):
        print('\033[98m',word)
    def green(word):
        print('\033[32m',word)
    def purple(word):
        print('\033[35m',word)
    def grey(word):
        print('\033[90m',word)
    def black(word):
        print('\033[30m',word)
class wordcolor_backgroundcolor:
    def normal_red(word):
        print('\033[41m',word)
    def normal_black(word):
        print('\033[40m',word)
    def normal_green(word):
        print('\033[42m',word)
    def normal_blue(word):
        print('\033[44m',word)
    def black_white(word):
        print('\033[7m',word)
    def normal_yellow(word):
        print('\033[102m',word)
    def normal_white(word):
        print('\033[107m',word)
class wordstyle:
    def bold(word):
        print('\033[1m',word)
    def italic(word):
        print('\033[3m',word)
    def underline(word):
        print('\033[4m',word)
    def crossed_out(word):
        print('\033[9m',word)
    def bold_underline(word):
        print('\033[21m',word)














