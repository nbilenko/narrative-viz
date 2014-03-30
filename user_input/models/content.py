import os
import nltk
import subprocess
from collections import Counter

class Content():
	'''File text'''
	def __init__(self, filename):
		self.path = filename
		self.name = os.path.basename(self.path)

	def text(self):
		f = open(self.path)
		return f.read()
	def char_recognition(self):
		char_number = 100 # Make this user-specifiable
		ner_cmd = ["java", "-mx700m", "-cp", "/Users/nbilenko/NYB/stanford-ner-2014-01-04/stanford-ner.jar:", "edu.stanford.nlp.ie.crf.CRFClassifier", "-loadClassifier", "/Users/nbilenko/NYB/stanford-ner-2014-01-04/classifiers/english.all.3class.distsim.crf.ser.gz", "-textFile"]
		out = subprocess.check_output(ner_cmd + [self.path])
		words = out.split()
		names = [tuple(w.split("/")) for w in words]
		prev_tag = "O"
		prev_name = ""
		all_names = []
		for name in names:
			if len(name) == 2:
				cur_name, cur_tag = name
				if prev_tag != "O" and cur_tag == "O":
					all_names.append((prev_name, prev_tag))
				if prev_tag == cur_tag and cur_tag != "O":
					cur_name = " ".join((prev_name, cur_name))
				prev_tag = cur_tag
				prev_name = cur_name
		count = Counter([name for name in all_names])
		chars = []
		locs = []
		orgs = []
		for c in count.most_common(char_number):
			if c[0][1] == "PERSON":
				chars.append(c[0][0])
			elif c[0][1] == "LOCATION":
				locs.append(c[0][0])
			elif c[0][1] == "ORGANIZATION":
				orgs.append(c[0][0])
		return chars, locs, orgs