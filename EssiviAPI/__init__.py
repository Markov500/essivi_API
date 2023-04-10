from flask import Flask
from EssiviAPI.extension import db,cors,migrate
from EssiviAPI.models import *
from EssiviAPI.routes.agentController import agentController
from EssiviAPI.routes.clientController import clientController
from EssiviAPI.routes.commandeController import commandeController
from EssiviAPI.routes.produitController import produitController

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    cors.init_app(app)
    migrate.init_app(app,db)
    db.init_app(app)
    

    app.register_blueprint(produitController)
    app.register_blueprint(commandeController)
    app.register_blueprint(agentController)
    app.register_blueprint(clientController)
    return app




