from flask import Blueprint, jsonify, request, abort
from EssiviAPI.models.agent import Agent
from EssiviAPI.extension import db

agentController = Blueprint("agentController",__name__,url_prefix="/agents")

@agentController.route('/',  methods = ['GET'])
def index():
    search = request.args.get('nom')
    findAgent = Agent.query
    print(search)
    if(search is not None):
         findAgent = Agent.query.filter(Agent.nom.like(f'%{search}%'))
    list_agent = [a.afficher() for a in findAgent.all()]
    return jsonify(
         {
            "success" : True,
            "count" : findAgent.count(),
            "agents" : list_agent
         }
    )


@agentController.route('/<string:id>',  methods = ['GET'])
def getAgent(id):
    print("\n\n"+id+"\n\n")
    agent = Agent.query.get(id)
    if agent != None:
        return jsonify(
            {
                "success" : True,
                "agent" : agent.afficher()
            }
        )
    else:
         return jsonify(
            {
                "success" : False,
                "erreur" : "Aucun agent trouvé"
            }
        )
    


#Cette route permet l'enregistrement d'un agent
@agentController.route('/', methods = ['POST'])
def addAgent():
  
    #Récuperation du json envoyé
    body=request.get_json()
    #Affectation des valeurs aux variable
    numId = body.get("numId")
    email = body.get("email")
    nom = body.get("nom",None) # si le champ nom n'ai pas trouvé il sera affecté à la variable None
    prenom = body.get("prenom",None)
    password = body.get("password",None)
        
    #Création d'un agent avec les valeurs récupérées
    agent = Agent(numId=numId, 
                    email= email,
                   nom= nom,
                   prenom= prenom,
                  password=password)
        
    #Enregistrement dans la bd
    agent.inserer()
        
    return jsonify(
        {
            "success" : True,
            "agentAdded" : agent.afficher()
        }
    )




#Cette route permet la modification des information  d'un agent
@agentController.route('/<string:id>', methods = ['PATCH'])
def updateAgent(id):
        #Récuperation du json envoyé
        body=request.get_json()
        
        #Récupération de l'agent à modifier
        agent = Agent.query.get(id)

        #Récupération du json envoyé
        agent.email = body.get("email", agent.email)
        agent.nom = body.get("nom", agent.nom) # si le champ nom n'ai pas trouvé il sera affecté à la variable agent.nom
        agent.prenom = body.get("prenom", agent.prenom)
        agent.password = body.get("password", agent.password)
        
        
        #Modification dans la bd
        agent.modifier()
        return jsonify(
            {
                "success" : True,
                "agentUpdated" : agent.afficher()
            }
        )



#Cette route permet à un agent de se connecter
@agentController.route('/login', methods = ['POST'])
def login():
    #Récuperation du json envoyé
    body=request.get_json()

    #Affectation des valeurs aux variable
    numId = body.get("numId",None)
    password = body.get("password",None)
        
    #Result stock la requête de recherche
    # la requête renvoie les agent ayant un numId ou un email égale à la variable numId et un mot de passe égale à password 
    result = Agent.query.filter(
        db.and_(
                db.or_(
                    Agent.numId == numId,
                    Agent.email == numId
                ),
                Agent.password == password
            )
    )
    if(result.count()== 0):
        return jsonify(
            {
                "auth":False,
            }
        ) 
    else :
        
        return jsonify(
        {
            "auth":True,
            "agent":result.first().afficher()
        }
        ) 
