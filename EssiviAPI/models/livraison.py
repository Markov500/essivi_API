from EssiviAPI.extension import db


class Livraison(db.Model):
    __tablename__ = "livraisons"
    id = db.Column(db.Integer, primary_key=True)
    dateLiv = db.Column(db.DateTime, nullable=False)
    qteLiv = db.Column(db.Integer, nullable=False)
    agentId = db.Column(db.String(5), db.ForeignKey('agents.numId'), nullable=False)
    agent = db.relationship(
        'Agent', backref=db.backref('livraisons', lazy=True))
    commandeId = db.Column(db.Integer, db.ForeignKey(
        'commandes.id'), nullable=False)
    commande = db.relationship(
        'Commande', backref=db.backref('livraisons', lazy=True))

    def __init__(self, dateLiv, qteLiv, agentId, commandeId):
        self.dateLiv = dateLiv
        self.qteLiv = qteLiv
        self.agentId = agentId
        self.commandeId = commandeId

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
            "dateLiv" : self.dateLiv,
            "qteLiv" : self.qteLiv,
            "agentId" : self.agentId,
            "commadeId" : self.commandeId
        }
