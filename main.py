import json
import pandas as pd
from vocabulary_creator import VocabularyCreator
from renege import RENEGE
from email_analyzer import EmailAnalyzer, FormulaType

INTERACTION_3 = './ACTS/interaction_3.csv'
INTERACTION_2 = './ACTS/interaction_2.csv'

def evaluate(formulaType:FormulaType,clean_text:int):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    total = 0
    analyzer = EmailAnalyzer()
    with open("test_set.json") as email_file:
        new_emails = json.load(email_file)

    i = 0
    email_count = len(new_emails["dataset"])

    print("Evaluating emails ")
    for e_mail in new_emails["dataset"]:
        i += 1
        print("\rEmail " + str(i) + "/" + str(email_count), end="")

        new_email = e_mail["mail"]
        subject = new_email["Subject"]
        body = new_email["Body"]
        spam = new_email["Spam"]

        if (analyzer.is_spam(subject, body,formulaType, clean_text)) and (spam == "true"):
            tp += 1
        if (not (analyzer.is_spam(subject, body, formulaType,clean_text))) and (spam == "false"):
            tn += 1
        if (analyzer.is_spam(subject, body, formulaType,clean_text)) and (spam == "false"):
            fp += 1
        if (not (analyzer.is_spam(subject, body,formulaType, clean_text))) and (spam == "true"):
            fn += 1
        total += 1

    if (tp + tn + fp + fn) == 0:
        print("\nAccuracy: infinity")
    else:
        print("\nAccuracy: ", round((tp + tn) / (tp + tn + fp + fn), 2))
    if(tp + fp) == 0:
        print("Precision: infinity")
    else :
        print("Precision: ", round(tp / (tp + fp), 2))
    if (tp + fn) == 0:
        print("Recall: infinity")
    else:
        print("Recall: ", round(tp / (tp + fn), 2))
    print("")
    return True


def run(creationDuVocabulaire: int, formulaType: FormulaType, clean_text: int):
    # 1. Creation de vocabulaire.
    vocab = VocabularyCreator()
    vocab.create_vocab(creationDuVocabulaire, clean_text)

    # 2. Classification des emails et initialisation des utilisateurs et des groupes.
    renege = RENEGE()
    renege.classify_emails(formulaType, clean_text)

    # 3. Evaluation de performance du modele avec la fonction evaluate()
    evaluate(formulaType, clean_text)


if __name__ == "__main__":
    # utilise pandas pour lire le csv
    df = pd.read_csv(INTERACTION_3)
    for index, row in df.iterrows():
        calculDeProbabilite = row['calculDeProbabilite']
        combinaisonDeProbabilite = row['combinaisonDeProbabilite']
        creationDuVocabulaire = row['creationDuVocabulaire']
        nettoyageDuTexte = row['nettoyageDuTexte']
        print(f"Test Case #{index}: calculDeProbabilite = {calculDeProbabilite}, combinaisonDeProbabilite = {combinaisonDeProbabilite}, creationDuVocabulaire = {creationDuVocabulaire}, nettoyageDuTexte = {nettoyageDuTexte}")
        # run le test case avec les bons parametre
        try:
            run(creationDuVocabulaire, FormulaType(calculDeProbabilite=calculDeProbabilite, combinaisonDeProbabilite=combinaisonDeProbabilite), nettoyageDuTexte)
        except Exception as e:
            print(e.with_traceback())



