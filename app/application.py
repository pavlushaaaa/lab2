from app import create_app
from flask_restful import Api

application = create_app()


if __name__ == '__main__':
    application.run()
