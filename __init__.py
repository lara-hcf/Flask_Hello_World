from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route("/contact")
def maPremiereApi():
   return render_template('contact.html')

@app.route("/calculcarre/<int:val_user>")
def carre(val_user):
  resultat = val_user*val_user
  message=""
  
  if (resultat%2 == 0):
    message="<p>C'est pair</p>"
  else: 
    message="<p>C'est impair</p>"
      
  return "<h2>Le carre de votre valeur est : </h2>"+ str(val_user*val_user) + message

@app.route("/sommevaleur/<int:val_user>")
def somme_valeur(val_user): 
   return app


                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
