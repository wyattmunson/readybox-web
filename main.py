from flask import Flask, render_template, request
import subprocess
# from os import walk
import os
import json 

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template('index.html')

@app.route("/status")
def get_status():
    # result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    # print(result.stdout)
    # return result.stdout.decode()

    page_options = [
        { 'displayName': "General", 'link': "/status/general", 'description': 'System OS and machine specifications'},
        { 'displayName': "Systemctl", 'link': "/status/process", 'description': 'Manage systemctl services and view logs'},
        { 'displayName': "Versions", 'link': "/status/versions", 'description': 'Check installed packages and versions'}
    ]
    def tester():
        print("GOTTEM")

    return render_template('status.html', pages=page_options)

@app.route("/render")
def render_cmd():

    result = subprocess.run(['sudo', 'systemctl', 'status', 'apache2'], stdout=subprocess.PIPE)
    # result = subprocess.getoutput("sudo systemctl status apache2")
        
    return render_template('render-command.html', data=result)

@app.route("/status/process")
def status_process():
    return render_template('status-process-list.html')

@app.route("/library")
def library():
    result = subprocess.run(['find', '/home/watchtower/Desktop/Library'], capture_output=True)

    def create_folder_structure_json(path): 
        # Initialize the result dictionary with folder 
        # name, type, and an empty list for children 
        result = {'name': os.path.basename(path), 
                'type': 'folder', 'path': path, 'children': []} 
    
        # Check if the path is a directory 
        if not os.path.isdir(path): 
            # result['path'] = "tes"  
            return result 
    
        # Iterate over the entries in the directory 
        for entry in os.listdir(path): 
        # Create the full path for the current entry 
            entry_path = os.path.join(path, entry) 
            # result['path'] = entry_path
    
            # If the entry is a directory, recursively call the function 
            if os.path.isdir(entry_path): 
                result['children'].append(create_folder_structure_json(entry_path)) 
            # If the entry is a file, create a dictionary with name and type 
            else: 
                # result['path'] = entry_path
                full_path = path + "/" + entry
                result['children'].append({'name': entry, 'type': 'file', 'path': full_path}) 
        
        return result
                
  
    # return result 
    folder_path = "/Users/wyatt/Downloads/folder1"
  
    # Call the function to create the JSON representation 
    folder_json = create_folder_structure_json(folder_path) 
    
    # Convert the dictionary to a JSON string with indentation 
    # folder_json_str = json.dumps(folder_json, indent=4) 
    
    # Print the JSON representation of the folder structure 
    # print(folder_json_str) 
    
    output = folder_json

    # item_list = result.stdout.decode().splitlines()
    # tree = {}
    # for i in item_list:


    return render_template('library.html', data=result, tree=[output])

@app.route("/status/process/<string:cmd_>")
def status_process_cmd(cmd_):
    # return "<h1>Hello</h1>"
    # result = subprocess.run(['sudo', 'systemctl', 'status', 'apache2'], stdout=subprocess.PIPE)

    result = subprocess.run(['sudo', 'systemctl', 'status', cmd_], capture_output=True)
    return render_template('render-command.html', cmd=cmd_, data=result, title=cmd_)

@app.route("/status/general")
def get_status_general():
    data = {}
    result = subprocess.run(['uname', '-a'], stdout=subprocess.PIPE)
    data['date'] = subprocess.run(['date'], stdout=subprocess.PIPE)
    data['uptime'] = subprocess.run(['uptime'], stdout=subprocess.PIPE)
    data['kernel'] = subprocess.run(['uname', '-s'], stdout=subprocess.PIPE)
    data['arch'] = subprocess.run(['uname', '-m'], stdout=subprocess.PIPE)
    data['os'] = subprocess.run(['uname', '-os'], stdout=subprocess.PIPE)
    data['disk'] = subprocess.run(['df', '-h'], stdout=subprocess.PIPE)
    data['docker'] = subprocess.run(['docker', '-v'], stdout=subprocess.PIPE)

    return render_template('status-general.html', data=result.stdout.decode(), props=data)


@app.route("/status/versions")
def get_status_version():

    package_list = {
        'docker': { 'versionCmd': ['docker', '-v']},
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
        
    return render_template('status-versions.html', package_list=package_list)

@app.route("/api/status")
def get_api_status():
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    # print(result.stdout)
    return result.stdout.decode()

@app.route("/api/restart/<string:cmd_>")
def restart_systemctl(cmd_):
    result = subprocess.run(['sudo', 'systemctl', 'restart', cmd_], stdout=subprocess.PIPE)
    return render_template('process-complete.html', status=result.returncode)

@app.route("/api/start/<string:cmd_>")
def start_systemctl(cmd_):
    result = subprocess.run(['sudo', 'systemctl', 'start', cmd_], stdout=subprocess.PIPE)
    return render_template('process-complete.html', status=result.returncode)

@app.route("/api/stop/<string:cmd_>")
def stop_systemctl(cmd_):
    result = subprocess.run(['sudo', 'systemctl', 'stop', cmd_], stdout=subprocess.PIPE)
    return render_template('process-complete.html', status=result.returncode)

@app.route("/api/enable/<string:cmd_>")
def enable_systemctl(cmd_):
    result = subprocess.run(['sudo', 'systemctl', 'enable', cmd_], stdout=subprocess.PIPE)
    return render_template('process-complete.html', status=result.returncode)

@app.route("/api/disable/<string:cmd_>")
def disable_systemctl(cmd_):
    result = subprocess.run(['sudo', 'systemctl', 'disable', cmd_], stdout=subprocess.PIPE)
    return render_template('process-complete.html', status=result.returncode)

@app.route("/api/open")
def open_file():
    file_path = request.args.get("file_path")

    result = subprocess.run(['open', file_path])
    return render_template('process-complete.html', status=result.returncode)
