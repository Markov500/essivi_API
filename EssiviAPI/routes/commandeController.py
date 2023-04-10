from flask import Blueprint, jsonify, request
from EssiviAPI.models.commande import Commande
from EssiviAPI.models.produit import Produit
from EssiviAPI.models.client import Client
from EssiviAPI.extension import db
commandeController = Blueprint("commandeController",__name__,url_prefix="/commandes")



@commandeController.route('/', methods= ['GET'])
def allCommandes():
    search = request.args.get('search')
    findCommande = Commande.query
    print(search)
    if(search is not None):
         findCommande = Commande.query.filter(
             db.or_(
                Commande.client.libelle.like(f'%{search}%'),
                Commande.produit.libelle.like(f'%{search}%')
                ) )
    list_commande = [a.afficher() for a in findCommande.all()]
    return jsonify(
         {
            "success" : True,
            "count" : findCommande.count(),
            "commandes" : list_commande
         }
    )


@commandeController.route('/<int:id>', methods= ['GET'])
def oneCommande(id):
    #Création d'une liste de commande en format json suivant la méthode afficher de chaque commande
    commande = Commande.query.get(id)
    if(commande != None):
        return jsonify(
            {
                "success" : True,
                "commande" : commande.afficher()
            }
        )
    else:
        return jsonify(
            {
                "success" : False,
                "erreur" : "Aucune commande trouvée"
            }
        )
    

#Affichage de la liste de toutes les commandes d'un client
@commandeController.route('/clients/<int:id>', methods= ['GET'])
def clientCommandes(id):
    #Création d'une liste de commande en format json suivant la méthode afficher de chaque commande
    
    if(id != None):
        listF = Commande.query.filter(Commande.clientId == id)
    else:
        listF = Commande.query
        
    list_commmande = [com.afficher() for com in listF.all()]
    return jsonify(
        {
            "success" : True,
            "count"  : listF.count(),
            "commandes" : list_commmande
        }
    )

#Enregistrement d'une commande
@commandeController.route('/', methods = ['POST'])
def addCommande():
    #Récuperation du json envoyé
    body=request.get_json()
    #affectation des valeurs aux variables
    produitId = body.get("produitId")
    clientId = body.get("clientId")
    qteProd = body.get("qteProd")
    
    
    #Vérification de l'existance d'un produit ayant l'id spécifié
    prod = Produit.query.get(produitId)
    if(prod == None):
        return jsonify(
            {
                "success" : False,
                "erreur" : "Aucun produit trouvé"
            }
            
        )
    #Vérifier si la quantité commandé n'est pas supérieur à celle en stock
    elif ( prod.qteStock < qteProd):
        return jsonify(
            {
                "success" : False,
                "erreur" : "Quantité de produit insuffisant",
                "produit": prod.afficher()
            }
            
        )
    
    print(f"\n\n{clientId}\n\n\n")
    #Faire les actions si le client existe
    if(Client.query.get(clientId) != None):
        prod.qteStock -= qteProd
        commande = Commande(clientId=clientId,
                            produitId=produitId,
                            qteProd=qteProd)
        print("\n\n\n55555\n\n\n")
        commande.inserer()
        prod.modifier()
        
        return jsonify(
            {
                "success" : True,
                "commandeAdded" : commande.afficher()
            }
        )
    return jsonify(
            {
                "success" : False,
                "erreur" : "Impossible d'ajouter une commande"
            }
        )
        
        
        