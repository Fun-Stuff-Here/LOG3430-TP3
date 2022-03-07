import json
import math
from decimal import Decimal

from text_cleaner import TextCleaning

MULTIPLICATION = 'multiplication'
SOMME_DES_LOGS = 'sommeDesLogs'
SOMME = 'somme'


class FormulaType:
    def __init__(self,calculDeProbabilite:int,combinaisonDeProbabilite:int):
        self.calculDeProbabilite = calculDeProbabilite
        self.combinaisonDeProbabilite = combinaisonDeProbabilite


class EmailAnalyzer:
	"""Classe pour classifier les e-mails comme spam ou non spam (ham)"""

	def __init__(self):
		self.vocab = "vocabulary.json"
		self.cleaning = TextCleaning()
		self.voc_data = {}

	def is_spam(self, subject_orig, body_orig, formulaType: FormulaType,clean_text:int):
		'''
        Description: fonction pour verifier si e-mail est spam ou ham,
        en calculant les probabilites d'etre spam et ham, 
        en fonction du sujet et du texte d'email.
        Sortie: 'True' - si l'email est spam, 'False' - si email est ham.
        '''
		# Clean email's subject and body
		email_subject = self.clean_text(subject_orig,clean_text)
		email_body = self.clean_text(body_orig,clean_text)

		# Get the spam/ham probabilities
		p_subject_spam, p_subject_ham = self.spam_ham_subject_prob(email_subject,formulaType)
		p_body_spam, p_body_ham = self.spam_ham_body_prob(email_body,formulaType)
        
		# Compute the merged probabilities

		if formulaType.combinaisonDeProbabilite == SOMME:
			p_spam = Decimal(0.6) * p_subject_spam + Decimal(0.4) * p_body_spam
		elif formulaType.combinaisonDeProbabilite == SOMME_DES_LOGS:
			p_spam =  Decimal(0.6) * Decimal.log10(Decimal(p_subject_spam)) + Decimal(0.4) * Decimal.log10(Decimal(p_body_spam))

		p_ham = Decimal(0.5) * (p_subject_ham + p_body_ham)

		# Decide is the email is spam or ham
		if p_spam > p_ham:
			return True
		else:
			return False



	def spam_ham_body_prob(self, body, formulaType: FormulaType):
		'''
        Description: fonction pour calculer la probabilite
        que le 'body' d'email est spam ou ham.
        Sortie: probabilite que email body est spam, probabilite
        que email body est ham.
        '''

		return self.spam_prob(body, "p_body_spam", formulaType)

	def spam_ham_subject_prob(self, subject,formulaType: FormulaType):
		'''
        Description: fonction pour calculer la probabilite
        que le sujet d'email est spam ou ham.
        Sortie: probabilite que email subject est spam, probabilite
        que email subject est ham.
        '''

		return self.spam_prob(subject, "p_sub_spam", formulaType)



	def spam_prob(self, text, dict_key, formulaType: FormulaType):
		'''
		Description: fonction pour calculer la probabilite
		que le text est spam ou ham.
		Sortie: probabilite que text est spam, probabilite
		que le text est ham.
		'''
		p_spam = Decimal(1.0)
		p_ham = Decimal(1.0)

		voc_data = self.load_dict()

		# Parse the text to compute the probability
		for word in text:
			# Check the spam probability
			if word in voc_data[dict_key]:
				if formulaType.calculDeProbabilite == MULTIPLICATION:
					p_spam *= Decimal(voc_data[dict_key][word])
				elif formulaType.calculDeProbabilite == SOMME_DES_LOGS:
					p_spam += Decimal.log10(Decimal(voc_data[dict_key][word]))
			else:
				p_spam *= Decimal(1.0) / (Decimal(len(voc_data[dict_key])) + Decimal(1.0))

			# Check the ham probability
			if word in voc_data[dict_key]:
				p_ham *= Decimal(voc_data[dict_key][word])
			else:
				p_ham *= Decimal(1.0) / (Decimal(len(voc_data[dict_key])) + Decimal(1.0))
		if formulaType.calculDeProbabilite == SOMME_DES_LOGS:
			p_spam = 10**p_spam
		p_spam *= Decimal(0.5925)
		p_ham *= Decimal(0.4075)

		return (p_spam, p_ham)

	def clean_text(self, text,clean_text:int):  # pragma: no cover
		return self.cleaning.clean_text(text,clean_text)

	def load_dict(self):  # pragma: no cover
		# Open vocabulary
		with open(self.vocab) as json_data:
			vocabu = json.load(json_data)

		return vocabu
