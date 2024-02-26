from flask import render_template
from app.api import bp
# from app.status.logic import get_status_cats
# import app.ansible.logic as ansible

@bp.route('/')
def homie():
    # page_options = ansible.get_ansible_list()
    

    # return render_template('status/status.html', pages=page_options, title_text='Ansible Scripts')
    return "not implemented"