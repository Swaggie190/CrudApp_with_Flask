from models.entites import Etudiant, Matiere, Note, db


# Ajouter un étudiant, des matières et des notes
def ajouter_etudiant(matricule, nom, prenom, filiere, niveau):
    etudiant = Etudiant(matricule=matricule, nom=nom, prenom=prenom, filiere=filiere, niveau=niveau)
    db.session.add(etudiant)
    db.session.commit()

def ajouter_matiere(code, titre, credit):
    matiere = Matiere(code=code, titre=titre, credit=credit)
    db.session.add(matiere)
    db.session.commit()

def ajouter_note(matricule, code, valeur):
    note = Note(matricule=matricule, code=code, valeur=valeur)
    db.session.add(note)
    db.session.commit()

# Lister les étudiants, leurs matières et leurs notes
def lister_etudiants():
    etudiants = Etudiant.query.all()
    for etudiant in etudiants:
        print(f"Matricule: {etudiant.matricule}, Nom: {etudiant.nom}, Prénom: {etudiant.prenom}, Filière: {etudiant.filiere}, Niveau: {etudiant.niveau}")
        print("Matières:")
        for note in etudiant.notes:
            matiere = Matiere.query.get(note.code)
            print(f"- Code: {matiere.code}, Titre: {matiere.titre}, Crédit: {matiere.credit}, Note: {note.valeur}")

# Lister les notes des etudiants
def get_notes_etudiant(matricule):
    etudiant = Etudiant.query.get(matricule)
    if etudiant:
        return etudiant.notes.all()
    else:
        return []


# Modifier les données des étudiants, des matières et des notes
def modifier_etudiant(matricule, nom=None, prenom=None, filiere=None, niveau=None):
    etudiant = Etudiant.query.get(matricule)
    if nom:
        etudiant.nom = nom
    if prenom:
        etudiant.prenom = prenom
    if filiere:
        etudiant.filiere = filiere
    if niveau:
        etudiant.niveau = niveau
    db.session.commit()

def modifier_matiere(code, titre=None, credit=None):
    matiere = Matiere.query.get(code)
    if titre:
        matiere.titre = titre
    if credit:
        matiere.credit = credit
    db.session.commit()

def modifier_note(matricule, code, valeur):
    note = Note.query.filter_by(matricule=matricule, code=code).first()
    note.valeur = valeur
    db.session.commit()

# Supprimer les étudiants, les matières et les notes
def supprimer_etudiant(matricule):
    etudiant = Etudiant.query.get(matricule)
    db.session.delete(etudiant)
    db.session.commit()

def supprimer_matiere(code):
    matiere = Matiere.query.get(code)
    db.session.delete(matiere)
    db.session.commit()

def supprimer_note(matricule, code):
    note = Note.query.filter_by(matricule=matricule, code=code).first()
    db.session.delete(note)
    db.session.commit()