import numpy, sqlite3, json
from random import shuffle
from datetime import datetime

COMPDATA = []

websites = ["nos","nietspeld","nu","telegraaf","speld"]
for site in websites:
	headers = site+"headers.txt"
	with open("headersmap/"+headers,'r') as RMAT:
		RMATTXT = RMAT.read()
		LISTDATAph = RMATTXT.split("|")
		LISTDATA = LISTDATAph.pop(len(LISTDATA)-1)
#sql_transaction = []
#connection = sqlite3.connect('HeaderData.db')





	