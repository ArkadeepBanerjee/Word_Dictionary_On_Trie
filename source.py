'''------------------------------------------------------------------
Program description: A Data Structure that allows user to key in a 
string, one character at a time and shows a list of string starting
with the text entered thus far,if any. If the current string doesnot
exists, it provides user the option to insert the string
Acknowledgements: 
--------------------------------------------------------------------'''

__author__ = 'Arkadeep Banerjee'
__ver__ = 'Python 3.3.2'

import sys
import string


ctr = 0

def getInput():
	print("Enter the Character:")
	user_Input = str(input())
	while (len(user_Input) != 1):
		print("\nERROR\nPlease Enter a Single Character.")
		user_Input = str(input())
	return user_Input.lower()



def findItem(trie,ch):
	if ch in trie[1]:
		return trie[1][ch]
	return None



def printTrie(trie,string):
	global ctr
	if len(trie[1]) == 0 and trie[0] == True:
		ctr += 1
		print(string)
		return
	if(trie[0] == True):
		ctr += 1
		print(string)
	for item in trie[1].keys():
		printTrie(trie[1][item],str(string+str(item)))
	return
	
	
	
def searchTrie(trie):
	global ctr
	current = trie
	string = ''
	print("\n------------------------------------------------------------------------------")
	print("\nWelcome to the Dictionary Portal")
	print("\nEnter A Character of the Intended String one at a time: ")
	char = getInput()
	string = string + str(char)
	current = findItem(current,char)

	while current != None:
		print("\n------------------------------------------------------------------------------")
		print("\nString entered thus far: '"+string+"'")
		print("\nStrings in dictionary starting with the above prefix:")
		ctr = 0
		printTrie(current,string)
		print("\nThere are "+str(ctr)+" string(s).\n")
		
		if(current[0] == False):
			print("\n---------------------------------------------------------------------------")
			print("\nHowever, the Entered String '"+string+"' does not exist in the dictionary.")
			print("Press i to insert the string into the Dictionary.")
			print("Press m to cancel and return to Main Menu.")
			print("Press c to Continue Entering the Next Character in Sequence.")
			char = getInput()
			while char != 'i' and char != 'm' and char != 'c':
				char =getInput()
			if(char == 'i'):
				current[0] = True
				print("\n'"+string+"' has been saved.\nGoing Back to Main Menu\n\n")
				return
			if(char == 'm'):
				return
		else:
			print("\n---------------------------------------------------------------------------")
			print("\nNow, the Entered String '"+string+"' exists in the dictionary.")
			print("Press d to delete the string from the Dictionary.")
			print("Press m to cancel and return to Main Menu.")
			print("Press c to Continue Entering the Next Character in Sequence.")
			char = getInput()
			while char != 'd' and char != 'm' and char != 'c':
				char =getInput()
			if(char == 'd'):
				print("\n'"+string+"' has been deleted.\nGoing Back to Main Menu\n\n")
				current[0] = False
				return
			if(char == 'm'):
				return

		print("\nEnter A Character of the Intended String one at a time: ")
		char = getInput()
		string  = string + str(char)
		current = findItem(current,char)
		
		
	while True:
		print("\n------------------------------------------------------------------------------")
		print("\n'"+string+"' or any string having the given prefix never existed in the Dictionary.")
		print("\nPress i to insert the string into the Dictionary.")
		print("Press m to cancel and return to Main Menu.")
		print("Press c or any other character to continue entering the next character.")
		char = getInput()
		while char != 'i' and char != 'm' and char != 'c':
			print ("\nWrong Input Choice.\nPlease Enter Again")
			char =getInput()
		if (char == 'i' or char == 'm'):
			break
		print("\nEnter A Character of the Intended String one at a time: ")
		char = getInput()
		string  = string + str(char)
	if(char == 'i'):
		insertTrie(trie[1],string)
		print("\n'"+string+"' has been saved.\nGoing Back to Main Menu\n\n")
	return



def insertTrie(trie,string):
	if len(string) == 1:
		ch = string[0]
		if ch in trie:
			trie[ch][0] = True
		else:
			trie[ch] = [True,dict()]
		return
	ch = string[0]
	if ch in trie:
		trie = trie[ch][1]
		insertTrie(trie,string[1:])
	else:
		trie[ch] = [False,dict()]
		trie = trie[ch][1]
		insertTrie(trie,string[1:])
	return




def main():
	__TRIE__ = [False,dict()]
	while True:
		print("\n------------------------------------------------------------------------------")
		print("\nMAIN MENU:")
		print("Press u to Use the Dictionary:");
		print("Press x to Exit");
		char = getInput()
		
		if(char == 'x'):
			break
		if(char != 'u'):
			continue
		searchTrie(__TRIE__)
	print("\n------------------------------------------------------------------------------")
	print("\n\nThanks for using the Dictionary.\nHave a Good Day!!")


main()

	
