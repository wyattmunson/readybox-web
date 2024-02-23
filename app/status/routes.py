from flask import render_template
from app.status import bp

@bp.route('/')
def index():
    page_options = [
        { 'displayName': "General", 'link': "/status/general", 'description': 'System OS and machine specifications'},
        { 'displayName': "Systemctl", 'link': "/status/process", 'description': 'Manage systemctl services and view logs'},
        { 'displayName': "Versions", 'link': "/status/versions", 'description': 'Check installed packages and versions'}
    ]
    def tester():
        print("GOTTEM")

    # return render_template('status.html', pages=page_options)
    return render_template('status/status.html', pages=page_options)

@bp.route('/general/')
def categories():
    return render_template('posts/categories.html')
