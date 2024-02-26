# from flask import Flask
# app = Flask(__name__)

# import yourapplication.views

from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.status import bp as status_bp
    app.register_blueprint(status_bp, url_prefix='/status')
    
    from app.ansible import bp as ansible_bp
    app.register_blueprint(ansible_bp, name='ansible', url_prefix='/ansible')
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')



    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app