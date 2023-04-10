from EssiviAPI.extension import db

class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(80), nullable=False)
    telephone = db.Column(db.String(8), nullable = False)
    longitude = db.Column(db.Double, nullable = False)
    latitude = db.Column(db.Double, nullable = False)


    def __init__(self, libelle, telephone, longitude, latitude):
        self.libelle = libelle
        self.telephone = telephone
        self.longitude = longitude
        self.latitude = latitude

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
            "telephone":self.telephone,
            "longitude":self.longitude,
            "latitude" : self.latitude,
        }
