from apps import create_app
from src.config import application as application_config

application = create_app(application_config)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port='8080', debug=True)
