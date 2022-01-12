from flask import Flask
app = Flask(__name__)

@app.route("/") #Ruta raiz
def server_info():
    return "Hola mundo con Flask"

if __name__ == "__main__":
    app.run()