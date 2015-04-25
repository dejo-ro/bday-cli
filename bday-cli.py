#!/usr/bin/python3.4

import sys
import argparse
import json
from datetime import datetime

#this class is the primary object for holding information
#class Birthday(object):
#	def __init__(self, name='', date='', comment=''):
#		self.name = name
#		self.date = date
#		self.comment = comment


#def listBdays(all):

def main():
	
	#define the parser
	parser = argparse.ArgumentParser(description='Read and Write a birthday calendar.')
	
	#defining cli arguments	
	parser.add_argument('-j', dest='jsonFile', required=False, help='JSON file for storing/reading birthdays')	
	parser.add_argument('-l', dest='listMonthlyOption', action='store_true', help='List this week\'s birthdays')
	parser.add_argument('-ll', dest='listAllOption', action='store_true', help='List all birthdays')
	parser.add_argument('-a', dest='addBirthdayOption', nargs=3, help='Add new birthday ("Some N. Ame", MM-DD, "Comment")')
	

	args = parser.parse_args()
	
	with open(args.jsonFile, mode='r', encoding='utf-8') as input:
		bdayList = json.load(input)

			
	if args.addBirthdayOption:
		name = args.addBirthdayOption[0]
		date = args.addBirthdayOption[1].split('-', 1)
		month = int(date[0])
		day = int(date[1])
		comment = args.addBirthdayOption[2]
		
		with open(args.jsonFile, 'a') as output:
			json.dump({'name': name, 'date': {'month': month, 'day': day}, 'comment': comment}, output)
			output.write('\n')
	
		
	if args.listAllOption:
		with open(args.jsonFile) as input:
					bday = json.load(input)
					print('name')
					print(bday)
		

	if args.listMonthlyOption:
		currentDay = datetime.now().day
		currentMonth = datetime.now().month


		print([bday for bday in bdayList if bday['date']['month']==currentMonth])		

		print(currentDay)
		print(currentMonth)




if __name__ == "__main__":
    sys.exit(main())

