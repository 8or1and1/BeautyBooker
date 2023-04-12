from flask import Flask
from app import app, db
from app.models import User, Master

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Master}

Flask.run(app)
