from flask import Blueprint, jsonify, request
from EssiviAPI.models.produit import Produit
produitController = Blueprint("produitController",__name__,url_prefix="/produits")

@produitController.route('/',  methods = ['GET'])
def index():
    list_prod = [a.afficher() for a in Produit.query.all()]
    return jsonify(
         {
            "success" : True,
            "count" : Produit.query.count(),
            "produits" : list_prod
         }
    )



#Cette route permet l'enregistrement d'un produit
@produitController.route('/', methods = ['POST'])
def addProduit():
  
    #Récuperation du json envoyé
    body=request.get_json()
    #Affectation des valeurs aux variable
    libelle = body.get("libelle")
    prixUnit = body.get("prixUnit",None) # si le champ prixUnit n'ai pas trouvé il sera affecté à la variable None
    qteStock = 0
        
    #Création d'un produit avec les valeurs récupérées
    produit = Produit(libelle=libelle, 
                    prixUnit=prixUnit,
                   qteStock=qteStock)
        
    #Enregistrement dans la bd
    produit.inserer()
        
    return jsonify(
        {
            "success" : True,
            "produitAdded" : produit.afficher()
        }
    )




#Cette route permet la modification des information  d'un produit
@produitController.route('/<int:id>', methods = ['PATCH'])
def updateProduit(id):
        #Récuperation du json envoyé
        body=request.get_json()
        
        #Récupération du prosuit à modifier
        produit = Produit.query.get(id)

        #Récupération du json envoyé
        produit.libelle = body.get("libelle", produit.libelle)
        produit.prixUnit = body.get("nom", produit.prixUnit) 
        
        #Modification dans la bd
        produit.modifier()
        return jsonify(
            {
                "success" : True,
                "produitUpdated" : produit.afficher()
            }
        )

#Cette route permet la modification des information  d'un produit
@produitController.route('/approvisionner/<int:id>', methods = ['PATCH'])
def ApprovisionnerProduit(id):
        #Récuperation du json envoyé
        body=request.get_json()
        
        #Récupération du prosuit à modifier
        produit = Produit.query.get(id)

        #Récupération du json envoyé
        qte = body.get("qteProd", produit.qteStock)
        
        if(qte <=0):
            return jsonify(
                {
                    "success" : False,
                    "erreur" : "La quantité ne peut être inférieur à 0"
                }
            )
        else:
            
            #Modification dans la bd
            produit.qteStock = qte
            produit.modifier()
            return jsonify(
                {
                    "success" : True,
                    "produitUpdated" : produit.afficher()
                }
        )


