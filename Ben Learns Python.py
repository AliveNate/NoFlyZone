

#Data files are found here: C:\Users\terry\BattleScribe\data\Warhammer 40,000 9th Edition

with open("D:\\Programming\\PythonProjects\\Battlescribe Replacement\\NoFlyZone\\10000passwords.txt") as f:
	#f is a file object
	#f.read returns a string
	f_contents = f.read()
	#break the string apart by new line and create a list
	list = f_contents.split('\n')
	list.sort()
	print(list)
	
