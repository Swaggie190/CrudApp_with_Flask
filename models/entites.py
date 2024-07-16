from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKeyConstraint

db= SQLAlchemy()

class Etudiant(db.Model):
    __tablename__= 'etudiant'
    matricule = db.Column(db.String(8), primary_key = True)
    nom = db.Column(db.String(50), nullable = False)
    prenom = db.Column(db.String(50), nullable = False)
    filiere = db.Column(db.String(50), nullable = False)
    niveau = db.Column(db.String(50), nullable = False)
    notes = db.relationship('Note', backref='etudiant', lazy='dynamic')


class Matiere(db.Model):
    __tablename__= 'matiere'
    code = db.Column(db.String(8), primary_key = True)
    titre = db.Column(db.String(70), nullable = False)
    credit = db.Column(db.Integer, nullable = False)

class Note(db.Model):
    __tablename__= 'note'
    matricule = db.Column(db.String(8), nullable = False)
    code = db.Column(db.String(8), nullable = False)
    valeur = db.Column(db.Numeric(4,2), nullable = False)
    __table_args__ = (
        ForeignKeyConstraint(['matricule'], ['etudiant.matricule']),
        ForeignKeyConstraint(['code'], ['matiere.code']),
        db.PrimaryKeyConstraint(matricule, code)
    )




