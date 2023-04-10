import os
from dotenv import load_dotenv
load_dotenv()
motdepasse=os.getenv("password")
hote=os.getenv("host")
utilisateur=os.getenv("user")
dialecte=os.getenv("dialect")
bd = os.getenv("bd")



SQLALCHEMY_DATABASE_URI = "{0}://{1}:{2}@{3}/{4}".format(dialecte,utilisateur,motdepasse,hote,bd)
SQLALCHEMY_TRACK_MODIFICATIONS  = False
