from flask import Blueprint, jsonify, request
from EssiviAPI.models.livraison import Livraison
livraisonController = Blueprint("livraisonController",__name__,url_prefix="/livraisons")