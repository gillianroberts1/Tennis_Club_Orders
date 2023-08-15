from flask import Flask
from controllers.controller import items_blueprint


app = Flask(__name__)
app.register_blueprint(items_blueprint)


#if we had other comtrollers we woudl regieste them here too
#for example customer_blueprint

