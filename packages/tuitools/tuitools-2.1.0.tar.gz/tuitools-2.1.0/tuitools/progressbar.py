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