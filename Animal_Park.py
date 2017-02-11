from Class import Animal

def menuChoice(nChoices):
	#used to collect the inputs for menuchoices
	while True:
		try:
			choice = input("Choose an alternative: ")
			choice = int(choice)
			if choice<=nChoices and choice>0:
				break
			else:
				print("Choose a valid option ")
		except ValueError:
			print("Invalid Input ")
	return choice

def readFile(fileName):
	#reads external files and returns the values in the form of a list
	list=[]
	with open(str(fileName)+".txt", "r") as externalFile:
		for line in externalFile:
			currentLine=line.rstrip("\n")
			list.append(currentLine)
	return list

def createObjects():
	#creates all the animal objects from an externally saved file
	lsInfo=readFile("animals")
	list=[]
	lsObjects=[]
	for n in range(len(lsInfo)):
		line=lsInfo[n].split(", ")
		list.append(line)
	for n in range(len(list)):
		animal=Animal(list[n][0],list[n][1],int(list[n][2]),list[n][3])
		lsObjects.append(animal)
	return lsObjects

"""def addAnimal():
	#menu that creats new animal objects and appends them to the list
	n=0
	for species in lsSpecies:
		n+=1
		print("%s. %s" % (n,species))
	speciesChoice=menuChoice(n)-1
	print("""
"""Choose Gender:
1. Male [M]
2. Female [F]"""
""")
	gender=menuChoice(2)
	if gender==1:
		gender="M"
	if gender==2:
		gender="F"
	while True:
		try:
			age=input("Input Age: ")
			age=int(age)
			break
		except ValueError:
			print("Choose a number ")
	unique=False
	while unique==False:
		unique	=True
		x=int(0)
		name=str(input("Choose a name: ")).title()
		for animal in lsAnimals:
			if animal.name!=name:
				pass
			else:
				print("Choose an unique name ")
				unique=False
		
			
	animal=Animal(name, lsSpecies[speciesChoice], age, gender)
	return animal"""

def start():
	#starts the main functions with the values from external files
	lsSpecies=readFile("species")
	lsAnimals=createObjects()
	maxCap=int(readFile("maxCap")[0])
	mainMenu(lsSpecies, lsAnimals, maxCap)

def saveFile(lsAnimals):
	#saves the objects in the list in a external file
	with open("animals.txt", "w") as externalFile:
		for animal in lsAnimals:
			externalFile.write("%s, %s, %s, %s\n" % (animal.name, animal.species, animal.age, animal.gender))


def search(lsAnimals):
	#search the list with the parameter that the user chooses
	while True:
		searchParameter=str(input('Search or type "cancel" to exit: ')).title()
		chosenAnimal=[]
		for animal in lsAnimals:
			if searchParameter==animal.name:
				chosenAnimal.append(animal)
			elif searchParameter==animal.age:
				chosenAnimal.append(animal)
			elif searchParameter==animal.gender:
				chosenAnimal.append(animal)
			elif searchParameter==animal.species:
				chosenAnimal.append(animal)
			else:
				pass
		if searchParameter=="Cancel":
			break
		elif chosenAnimal==[]:
			print("The animal doesn´t exist, try again ")
		else:
			break
	return chosenAnimal

def overviewMenu(lsAnimals, ascending):
	#the menu which the user chooses parameter to sort by
	while True:
		print("""
Sort by:
1. Name
2. Age
3. Gender
4. Species

5. Previous Menu""")

		choice=menuChoice(5)
		if choice==1:
			printOverview(lsAnimals, "name", ascending)
		elif choice==2:
			printOverview(lsAnimals, "age", ascending)
		elif choice==3:
			printOverview(lsAnimals, "gender", ascending)
		elif choice==4:
			printOverview(lsAnimals, "species", ascending)
		elif choice==5:
			break
	return lsAnimals


"""def printOverview(lsAnimals, searchParameter="name", ascending=False):
	#prints all the animals in a userchosen order
	sortedList=sorted(lsAnimals, key=lambda animal: getattr(animal, searchParameter), reverse=ascending)
	if searchParameter=="name" or searchParameter=="age":
		for n in range(len(sortedList)):
			animal=sortedList[n]
			print("%s) %s (%s, %s y/o, %s)" % (n+1, animal.name, animal.species, animal.age, animal.gender))
	elif searchParameter=="gender" or searchParameter=="species":
		lsCategories=[]
		for animal in sortedList:
			lsCategories.append(getattr(animal, searchParameter))
		uniqueCategories=set(lsCategories)
		for category in uniqueCategories:
			print("""
"""+str(category)+"""""":""" """)
			for animal in sortedList:
				if getattr(animal, searchParameter)==category:
					print(animal.name)"""

def ascending(lsAnimals):
	#choose which way you want to sort the list, in ascending or descending order
	while True:
		print("""
1. Ascending
2. Descending

3. Previous Menu""")
		ascending=False
		choice=menuChoice(3)
		if choice==1:
			ascending=False
		elif choice==2:
			ascending=True
		elif choice==3:
			break
		overviewMenu(lsAnimals, ascending)	

"""def removeAnimal(lsAnimals):
	#prints the list of animals and lets the user choose an animal to delete, also possible to return to main menu
	printOverview(lsAnimals)
	print("""
"""%s) Return to Main Menu"""
""" % (len(lsAnimals)+1))
	userInput=menuChoice(len(lsAnimals)+1)
	if userInput!=len(lsAnimals)+1:
		animalToDelete=userInput-1
		lsAnimals.pop(animalToDelete)
	return lsAnimals"""

def checkUnique(lsAnimals, argument):
	#checks if attributes of an object in a list are unique, returns all unique attributes
	output=[]
	seen=set()
	for animal in lsAnimals:
		object=getattr(animal, argument)
		if object not in seen:
			output.append(object)
			seen.add(object)
		elif object in seen:
			output.remove(object)
	return output


def recommendations(lsAnimals, maxCap, lsSpecies):
	#gives recommendations based on the maxCap and the list
	if len(lsAnimals)<=maxCap:
		lonelySpecies=[]
		for species in lsSpecies:
			lsGenders=[]
			for animal in lsAnimals:
				if animal.species==species:
					lsGenders.append(animal.gender)
			if len(set(lsGenders))==1:
				for gender in lsGenders:
					if gender=="F":
						lonelySpecies.append("%s, M" %(species))
					else:
						lonelySpecies.append("%s, F" %(species))
		print("You should buy:")
		counter=0
		for object in lonelySpecies:
			counter+=1
			print("%s) %s"%(counter, object))

	if len(lsAnimals)>=maxCap:
		#recommendations for deleting animals
		numberOfAnimalsPerSpecies=[]
		tempList=[]
		for species in lsSpecies:
			speciesCounter=0
			for animal in lsAnimals:
				if animal.species==species:
					speciesCounter+=1
				numberOfAnimalsPerSpecies.append("*%ss* (You have: %s)"%(species, speciesCounter))
		for item in numberOfAnimalsPerSpecies:
			if int(item[-2])>2:
				tempList.append(item)
		print("You could remove some of these animals:")
		for item in tempList:
			print(item)
				
def mainMenu(lsSpecies, lsAnimals, maxCap):
	#main menu of the program
	while True:
		print("""
1. Add Animal
2. Remove Animals
3. Overview
4. Search
5. Recommendations

6. Save and Exit""")
		choice=menuChoice(6)
		if choice==1:
			#Add Animal
			if len(lsAnimals)<maxCap:
				lsAnimals.append(addAnimal(lsSpecies, lsAnimals))
			else: 
				print("Max capacity Reached, can´t add more animals ")

		elif choice==2:
			#Removes animals
			lsAnimals=removeAnimal(lsAnimals)

		elif choice==3:
			#Overview
			ascending(lsAnimals)

		elif choice==4:
			#Search
			chosenAnimal=search(lsAnimals)

			if chosenAnimal:
				printOverview(chosenAnimal)
			else:
				pass

		elif choice==5:
			recommendations(lsAnimals, maxCap, lsSpecies)

		elif choice==6:
			#Save And Exit
			saveFile(lsAnimals)
			break
			
