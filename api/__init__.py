from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# configuring the database

app.config['SQLALCHEMY_DATABASE_URI'] = f"{os.getenv('engine_name')}://{os.getenv('myuser')}:{os.getenv('mypass')}@{os.getenv('ip')}:{os.getenv('port_number')}/{os.getenv('db_name')}"


#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://foebutln:eoQ3zdYQdIUjZBOq737ewLA-4Wb30XRz@hansken.db.elephantsql.com/foebutln"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'My First GraphQL project !!'