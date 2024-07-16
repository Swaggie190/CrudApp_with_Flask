from models.entites import Etudiant, Matiere, Note, db
from DAO.etudiant_dao import *
from metier.etudiant_metier import *

def menu():
    db.create_all()
    while True:
        print("\n--- Gestion des étudiants ---")
        print("1. Ajouter un étudiant")
        print("2. Ajouter une matière")
        print("3. Ajouter une note")
        print("4. Lister les étudiants")
        print("5. Modifier un étudiant")
        print("6. Supprimer un étudiant")
        print("7. Calculer la moyenne d'un étudiant")
        print("8. Orienter un étudiant")
        print("9. Faire passer un étudiant en classe supérieure")
        print("0. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            matricule = input("Entrez le matricule de l'étudiant : ")
            nom = input("Entrez le nom de l'étudiant : ")
            prenom = input("Entrez le prénom de l'étudiant : ")
            filiere = input("Entrez la filière de l'étudiant : ")
            niveau = input("Entrez le niveau de l'étudiant : ")
            ajouter_etudiant(matricule, nom, prenom, filiere, niveau)
            print("Étudiant ajouté avec succès.")

        elif choix == "2":
            code = input("Entrez le code de la matière : ")
            titre = input("Entrez le titre de la matière : ")
            credit = int(input("Entrez le crédit de la matière : "))
            ajouter_matiere(code, titre, credit)
            print("Matière ajoutée avec succès.")

        elif choix == "3":
            matricule = input("Entrez le matricule de l'étudiant : ")
            code = input("Entrez le code de la matière : ")
            valeur = float(input("Entrez la valeur de la note : "))
            ajouter_note(matricule, code, valeur)
            print("Note ajoutée avec succès.")

        elif choix == "4":
            lister_etudiants()

        elif choix == "5":
            matricule = input("Entrez le matricule de l'étudiant à modifier : ")
            nom = input("Entrez le nouveau nom (ou appuyez sur Entrée pour ne pas le modifier) : ")
            prenom = input("Entrez le nouveau prénom (ou appuyez sur Entrée pour ne pas le modifier) : ")
            filiere = input("Entrez la nouvelle filière (ou appuyez sur Entrée pour ne pas la modifier) : ")
            niveau = input("Entrez le nouveau niveau (ou appuyez sur Entrée pour ne pas le modifier) : ")
            modifier_etudiant(matricule, nom=nom if nom else None, prenom=prenom if prenom else None, filiere=filiere if filiere else None, niveau=niveau if niveau else None)
            print("Étudiant modifié avec succès.")
        
        elif choix == "6":
            matricule = input("Entrez le matricule de l'étudiant à supprimer : ")
            supprimer_etudiant(matricule)
            print("Étudiant supprimé avec succès.")

        elif choix == "7":
            matricule = input("Entrez le matricule de l'étudiant : ")
            moyenne = MoyenneEtudiant(matricule)
            if moyenne is not None:
                print(f"La moyenne de l'étudiant {matricule} est : {moyenne}")
            else:
                print(f"L'étudiant avec le matricule {matricule} n'existe pas.")

        elif choix == "8":
            matricule = input("Entrez le matricule de l'étudiant : ")
            option = input("Entrez la nouvelle option : ")
            if orienterEtudiant(matricule, option):
                print(f"L'étudiant {matricule} a été orienté vers l'option {option} avec succès.")
            else:
                print(f"L'étudiant avec le matricule {matricule} n'existe pas.")

        elif choix == "9":
            matricule = input("Entrez le matricule de l'étudiant : ")
            if passerClasseSup(matricule):
                print(f"L'étudiant {matricule} a été fait passer en classe supérieure avec succès.")
            else:
                print(f"L'étudiant avec le matricule {matricule} n'existe pas.")

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/studentdata'
    db.init_app(app)
    with app.app_context():
        menu()