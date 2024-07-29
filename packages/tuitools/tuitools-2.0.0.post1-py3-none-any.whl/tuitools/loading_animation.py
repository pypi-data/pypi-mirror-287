def slash(sleeptime,number_of_time):
    import sys
    import time
    spinner_chars=['/','|','\\','-']
    spinner_position = 0
    for i in range(25):
            print('')
    for i in range(number_of_time):
        sys.stdout.write('\r' + ' ' * 50)
        sys.stdout.flush()
        sys.stdout.write('\r\t\t\t\t\t\t\t  ' + spinner_chars[spinner_position])
        sys.stdout.flush()
        spinner_position = (spinner_position + 1) % len(spinner_chars)
        time.sleep(sleeptime)

def dots(sleeptime,number_of_time):
    import sys
    import time
    spinner_chars=['','.','..','...']
    spinner_position = 0
    for i in range(25):
       print('')
    for i in range(sleeptime,number_of_time):
        sys.stdout.write('\r' + ' ' * 50)
        sys.stdout.flush()
        sys.stdout.write('\r\t\t\t\t\t\t\t  ' + spinner_chars[spinner_position])
        sys.stdout.flush()
        spinner_position = (spinner_position + 1) % len(spinner_chars)
        time.sleep(sleeptime)
def settable(sleeptime,number_of_time,character):
    import sys
    import time
    spinner_chars=character
    spinner_position = 0
    for i in range(25):
       print('')
    for i in range(number_of_time):
        sys.stdout.write('\r' + ' ' * 50)
        sys.stdout.flush()
        sys.stdout.write('\r\t\t\t\t\t\t\t  ' + spinner_chars[spinner_position])
        sys.stdout.flush()
        spinner_position = (spinner_position + 1) % len(spinner_chars)
        time.sleep(sleeptime)
