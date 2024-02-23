from flask import render_template
from app.status import bp
# from app.status.logic import get_status_cats
import app.status.logic as tester

@bp.route('/')
def index():
    page_options = tester.get_status_cats()

    return render_template('status/status.html', pages=page_options)

@bp.route('/general/')
def categories():
    data = tester.get_status_general()
    return render_template('status/general.html', props=data)

@bp.route('/processes/')
def all_processes():
    # data = tester.get_status_general()
    return render_template('status/process-list.html')

@bp.route("/process/<string:cmd_>")
def status_process_cmd(cmd_):
    result = tester.get_process_status(cmd_)

    # result = subprocess.run(['sudo', 'systemctl', 'status', cmd_], capture_output=True)
    return render_template('status/process-systemctl.html', cmd=cmd_, data=result, title=cmd_)

@bp.route("/versions")
def status_versions():
    result = tester.get_status_version()
    
    return render_template('status/versions.html', package_list=result)

@bp.route("/system/usb")
def system_usb():
    result = tester.run_command_array(['df', '-h'])
    
    return render_template('status/command.html', title="USB Devices", data=result)

@bp.route("/system/storage")
def system_storage():
    result = tester.run_command_array(['df', '-h'])
    
    return render_template('status/command.html', title="Storage  Devices", data=result)