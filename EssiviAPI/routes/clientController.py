from flask import Blueprint, jsonify, request
from EssiviAPI.models.client import Client
clientController = Blueprint("clientController",__name__,url_prefix="/clients")

@clientController.route('/')
def index():
    #Récupération de la valeur du paramètre libelle
    search = request.args.get('libelle')
    findClient = Client.query
    print(search)
    if(search is not None):
         findClient = Client.query.filter(Client.libelle.like(f'%{search}%'))
    list_client = [a.afficher() for a in findClient.all()]
    return jsonify(
         {
            "success" : True,
            "count" : findClient.count(),
            "clients" : list_client
         }
    )


#Cette route permet l'enregistrement d'un agent
@clientController.route('/', methods = ['POST'])
def addClient():
    try:
        #Récuperation du json envoyé
        body=request.get_json()
        #Affectation des valeurs aux variable
        libelle = body.get("libelle",None)
        telephone = body.get("telephone",None)
        longitude = body.get("longitude",None) # si le champ longitude n'ai pas trouvé il sera affecté à la variable None
        latitude = body.get("latitude",None)
            
        #Création d'un client avec les valeurs récupérées
        client = Client(
            libelle=libelle,
            telephone=telephone,
            longitude=longitude,
            latitude=latitude
        )
            
        #Enregistrement dans la bd
        client.inserer()
            
        return jsonify(
            {
                "success" : True,
                "clientAdded" : client.afficher()
            }
        )
    except:
        return jsonify(
            {
                "success":False,
                "erreur":"Les informations envoyées sont invalides"
            }
        )


#Cette route permet d'accéder à un client donné en connaisant son id
@clientController.route('/<int:id>',  methods = ['GET'])
def getClient(id):
    client = Client.query.get(id)
    return jsonify(
         {
            "success" : True,
            "client" : client.afficher()
         }
    )


#Cette route permet la modification des information  d'un client
@clientController.route('/<int:id>', methods = ['PATCH'])
def updateClient(id):
        #Récuperation du json envoyé
        body=request.get_json()
        
        #Récupération du client à modifier
        client = Client.query.get(id)

        #Récupération du json envoyé
        client.libelle = body.get("libelle", client.libelle)
        client.telephone = body.get("telephone", client.telephone)
        client.longitude = body.get("longitude", client.longitude)
        client.latitude = body.get("latitude", client.latitude)
        
        
        
        #Modification dans la bd
        client.modifier()
        return jsonify(
            {
                "success" : True,
                "clientUpdated" : client.afficher()
            }
        )