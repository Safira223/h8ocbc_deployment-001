import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cgbqctzsynakcg:f1b3a183366cbd0bd04843667274f8c1b5db7a887f4b0d2f2986adf1ce2fc741@ec2-3-218-171-44.compute-1.amazonaws.com:5432/d95ai3ag2ko9b0' + os.path.join(basedir, 'people.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cgbqctzsynakcg:f1b3a183366cbd0bd04843667274f8c1b5db7a887f4b0d2f2986adf1ce2fc741@ec2-3-218-171-44.compute-1.amazonaws.com:5432/d95ai3ag2ko9b0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)