class viewing_processes:
    def windows(self=''):
        import subprocess
        subprocess.run('tasklist')
    def mac_os(self=''):
        import subprocess
        subprocess.run('top')
    def linux(self=''):
        import subprocess
        subprocess.run('top')
class cpu:
    def linux(self=''):
        import subprocess
        subprocess.run('mpstart')
    def mac_os(self=''):
        import subprocess
        subprocess.run('mpstart')
    def windows(self=''):
        import subprocess
        subprocess.run('wmic cpu get *')
class system_informations:
    def windows(self=''):
        import subprocess
        subprocess.run('systeminfo')
    def linux(self=''):
        import subprocess
        subprocess.run('uname -a')
class memory:
    def windows(self=''):
        import subprocess
        subprocess.run('memorychip')
    def linux(self=''):
        import subprocess
        subprocess.run('cat /proc/meminfo')
    def mac_os(self=''):
        import subprocess
        subprocess.run('cat /proc/meminfo')
class harddisk:
    def windows(self=''):
        import subprocess
        subprocess.run('wmic diskdrive get model,name,size')
    def mac_os(self=''):
        import subprocess
        subprocess.run('lsblk')
    def linux(self=''):
        import subprocess
        subprocess.run('lsblk')
