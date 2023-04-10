from EssiviAPI.extension import db


class Produit(db.Model):
    __tablename__ = "produits"
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(50), nullable=False)
    qteStock = db.Column(db.Integer, nullable=False)
    prixUnit = db.Column(db.Double, nullable=False)

    def __init__(self, libelle, qteStock, prixUnit):
        self.libelle = libelle
        self.qteStock = qteStock
        self.prixUnit = prixUnit

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
            "libelle": self.libelle,
            "qteStock" : self.qteStock,
            "prixUnit" : self.prixUnit
        }
