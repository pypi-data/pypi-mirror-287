def cmd_run(output='True',tips='True',):
    import subprocess
    result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
    if output=='True':
        if tips=='True':
            if result.returncode == 0:
                print("Commend ran sucsessful.")
                print("output:")
                print(result.stdout)
            else:
                print("Commend ran unsucsessful")
                print("Error output:")
                print(result.stderr)
        if tips=='False':
            if result.returncode == 0:
                print(result.stdout)
            else:
                print(result.stderr)
        else:
            if result.returncode == 0:
                print(tips)
                print(result.stdout)
            else:
                print("Commend ran unsucsessful")
                print("Error output:")
                print(result.stderr)
    elif output=='False':
        pass
    else:
        print(
            '\033[91mTraceback (most recent call last):\n     \nTypeError:The parameter is wrong.')