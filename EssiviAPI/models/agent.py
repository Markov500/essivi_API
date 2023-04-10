from EssiviAPI.extension import db

class Agent(db.Model):
    __tablename__ = "agents"
    numId = db.Column(db.String(5), primary_key=True)
    email = db.Column(db.String(20), nullable= False, unique = True)
    nom = db.Column(db.String(15), nullable = True)
    prenom = db.Column(db.String(25), nullable = True)
    password = db.Column(db.String(50), nullable= False)

    def __init__(self, numId, email, password, nom, prenom):
        self.numId = numId
        self.email = email
        self.nom = nom
        self.prenom = prenom
        self.password = password
    
    def inserer(self):
        db.session.add(self)
        db.session.commit()
   

    def supprimer(self):
        db.session.delete(self)
        db.session.commit()
     

    def modifier(self):
         db.session.commit()

    def afficher(self):
        return{
            'numId': self.numId,
            'email': self.email,
            'nom' : self.nom,
            'prenom' : self.prenom,
            "password" : self.password
        }
