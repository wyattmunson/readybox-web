import subprocess

def get_status_cats():
    page_options = [
        { 'displayName': "General", 'link': "/status/general", 'description': 'System OS and machine specifications'},
        { 'displayName': "Systemctl", 'link': "/status/processes", 'description': 'Manage systemctl services and view logs'},
        { 'displayName': "Versions", 'link': "/status/versions", 'description': 'Check installed packages and versions'},
        { 'displayName': "USB", 'link': "/status/system/usb", 'description': 'Check installed packages and versions'},
        { 'displayName': "HEYYA", 'link': "/status/versions", 'description': 'Check installed packages and versions'}
    ]
    def tester():
        print("GOTTEM")
        
    return page_options


def get_status_general():
    data = {}
    result = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE)
    data['uname'] = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE)
    data['date'] = subprocess.run(['date'], stdout=subprocess.PIPE)
    data['uptime'] = subprocess.run(['uptime'], stdout=subprocess.PIPE)
    data['kernel'] = subprocess.run(['uname', '-s'], stdout=subprocess.PIPE)
    data['arch'] = subprocess.run(['uname', '-m'], stdout=subprocess.PIPE)
    data['os'] = subprocess.run(['uname', '-os'], stdout=subprocess.PIPE)
    data['disk'] = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
    data['docker'] = subprocess.run(['docker', '-v'], stdout=subprocess.PIPE)
    data['iostat'] = subprocess.run(['iostat'], stdout=subprocess.PIPE)
    data['vmstat'] = subprocess.run(['vmstat', '-s'], stdout=subprocess.PIPE, shell=True)
    data['free'] = subprocess.run(['free', '-h'], stdout=subprocess.PIPE, shell=True)
    data['pci'] = subprocess.run(['lspci'], stdout=subprocess.PIPE, shell=True)
    data['usb'] = subprocess.run(['lsusb'], stdout=subprocess.PIPE, shell=True)
    
    return data

def get_process_status(cmd):
    result = subprocess.run(['sudo', 'systemctl', 'status', cmd], capture_output=True)
    return result


def get_status_version():
    package_list = {
        'docker': { 'versionCmd': ['docker', '-v']},
        'lscpu': { 'versionCmd': ['lscpu', '-v']},
        'lsusb': { 'versionCmd': ['usbutils', '-v']},
        'lspci': { 'versionCmd': ['pciutils', '-v']},
        'faker': { 'versionCmd': ['notcommand', '-v']},
        'git': { 'versionCmd': ['git', '-v']},
        'node': { 'versionCmd': ['node', '-v']},
        'curl': { 'versionCmd': ['curl', '--version']},
        'wget': { 'versionCmd': ['wget', '--version', '|', 'head', '-n', '1']},
        'dig': { 'versionCmd': ['dig', '-v']},
        'make': { 'versionCmd': ['make', '-v']},
        'clang': { 'versionCmd': ['clang', '--version']},
        'npm': { 'versionCmd': ['npm', '-v']},
        'docker-compose': { 'versionCmd': ['docker-compose', '-v']},
        'aws': { 'versionCmd': ['aws', '--version']},
        'openssl': { 'versionCmd': ['openssl', 'version']},
        'nslookup': { 'versionCmd': ['nslookup', '-version']},
        'vim': { 'versionCmd': ['vim', '--version']},
        'awk': { 'versionCmd': ['awk', '--version']},
        'cut': { 'versionCmd': ['cut', '-v']},
        # 'ssh-keygen': { 'versionCmd': ['ssh-keygen', '-v']},
        'xxd': { 'versionCmd': ['xxd', '-v']},
        'cksum': { 'versionCmd': ['cksum', '-v']},
        'nano': { 'versionCmd': ['nano', '-version']},
        'jq': { 'versionCmd': ['jq', '-v']},
        'rake': { 'versionCmd': ['rake', '--version']},
        # 'rails': { 'versionCmd': ['rails', '-v']},
        'tar': { 'versionCmd': ['tar', '--version']},
        
        'python': { 'versionCmd': ['python', '--version']},
        # 'faker': { 'versionCmd': ['faker', '-v']},
        # 'faker': { 'versionCmd': ['faker', '-v']},
        # 'faker': { 'versionCmd': ['faker', '-v']},
    }
    

    for i in package_list:
        sub = package_list[i]["versionCmd"]
        try: 
            res = subprocess.run(sub, capture_output=True)
            package_list[i]['result'] = res
            # data['faker'] = subprocess.run(['notcommand', '-v'], capture_output=True, shell=True)
            print("RES", res)
        except:
            package_list[i]['result'] = "Not installed"
            # data['faker'] = "Not installed"
            
    return package_list


def run_command_array(cmd):
    result = subprocess.run(cmd, capture_output=True)
    return result