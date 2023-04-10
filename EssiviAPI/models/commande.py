from EssiviAPI.extension import db
from EssiviAPI.models.client import Client
from EssiviAPI.models.produit import Produit
from datetime import datetime

class Commande(db.Model):
    __tablename__ = "commandes"
    id = db.Column(db.Integer, primary_key=True)
    dateCom = db.Column(db.DateTime, nullable=False)
    qteProd = db.Column(db.Integer, nullable=False)
    produitId = db.Column(db.Integer, db.ForeignKey(
        'produits.id'), nullable=False)
    produit = db.relationship(
        'Produit', backref=db.backref('commandes', lazy=True))
    clientId = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    client = db.relationship('Client', backref=db.backref('clients', lazy=True))

    def __init__(self, produitId, clientId, qteProd):
        self.dateCom = datetime.now()
        self.produitId = produitId
        self.clientId = clientId
        self.qteProd = qteProd

    def inserer(self):
        db.session.add(self)
        db.session.commit()

    def modifier(self):
        db.session.commit()

    def supprimer(self):
        db.session.delete(self)
        db.session.commit()

    def afficher(self):
        return {
            "id": self.id,
            "dateCommande": self.dateCom,
            "qteProduit" : self.qteProd,
            "client": Client.query.get(self.clientId).afficher(),
            "produit": Produit.query.get(self.produitId).afficher(),
            
        }
