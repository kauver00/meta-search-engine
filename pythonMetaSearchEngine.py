"""
	A python search engine based on Google.
	The results can be displayed in the command prompt or in the browser.
	
	[Requires]:
				- Python3
				- yattag, it's a python module for rendering html page. It has used for the result page.
				- googlesearch: It provides many google's stuffs such as web search, image search, etc...
								It has been inclued in the Files directory.
								Just check out its README.md file for more details

"""
import os
from time import gmtime, strftime
try: 
	from googlesearch import search 
except ImportError: 
	print("googlesearch module not found or not installed!") 

from yattag import Doc


doc, tag, text = Doc().tagtext()

"""
	output variable init...
"""
results = []

def main():
	print("#-----------------------------------------#")
	print("#--------PYTHON META SEARCH ENGINE--------#")
	print("#-----------------------------------------#\n")
	query = input("$> Enter your request: ")
	"""
		Registering query to history file
	"""
	file = open("history.txt", "a")
	file.write('{0} {1}'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), query))
	file.write('\n')
	file.close()

	
	print("$> Searching...")

	try:
		results = search(query, tld="co.in", num=10, stop=1, pause=2) # Check the documentation for more details
	except TimeoutError:
		print("$> [error] Please check your internet connexion!")
	
	try:
		print('Results for : [ {} ]'.format(query))
		for j in results:
			print(j)
	except:
		print("$> [error] Please check your internet connexion!")
		return

#-----------------------------------------------
#					  MAIN
#-----------------------------------------------
if __name__ == '__main__':
	main()

