from flask import Flask
from models.entites import Etudiant, Note
from DAO.etudiant_dao import get_notes_etudiant

def MoyenneEtudiant(matricule):
    etudiant = Etudiant.query.get(matricule)
    if etudiant:
        notes = get_notes_etudiant(matricule)
        total_notes = sum(note.valeur for note in notes)
        nombre_notes = len(notes)
        if nombre_notes > 0:
            moyenne = total_notes / nombre_notes
            return moyenne
        else:
            return 0
    else:
        return None

def passerClasseSup(matricule):
    etudiant = Etudiant.query.get(matricule)
    if etudiant:
        if etudiant.niveau == "L1":
            etudiant.niveau = "L2"
        elif etudiant.niveau == "L2":
            etudiant.niveau = "L3"
        elif etudiant.niveau == "L3":
            etudiant.niveau = "M1"
        elif etudiant.niveau == "M1":
            etudiant.niveau = "M2"
        db.session.commit()
        return True
    else:
        return False

def orienterEtudiant(matricule, option):
    etudiant = Etudiant.query.get(matricule)
    if etudiant:
        etudiant.filiere = option
        db.session.commit()
        return True
    else:
        return False