from tkinter import *
from Animal_Park import*
from tkinter import messagebox

lsSpecies=readFile("species")
maxCap=int(readFile("maxCap")[0])
lsAnimals=createObjects()



class AnimalProgram:
	def __init__(self, master):
		frame=Frame(master)
		frame.grid
		self.welcomeText=Label(root, text="Welcome to the Animal Park™", )
		self.welcomeText.grid(row=1)
		self.addAnimalButton=Button(root, text="Add Animals", command=self.addAnimal)
		self.addAnimalButton.grid(row=2)
		self.removeAnimalButton=Button(root, text="Remove Animals", command=self.removeAnimal)
		self.removeAnimalButton.grid(row=3)
		self.overViewButton=Button(root, text="Show Overview", command=self.showOverview)
		self.overViewButton.grid(row=4)
		self.searchButton=Button(root, text="Search", command=self.searchAnimals)
		self.searchButton.grid(row=5)


	def addAnimal(self):
		addAnimalFrame=Toplevel()
		addAnimalFrame.attributes("-topmost", 1)

		self.name=StringVar()
		self.age=IntVar()
		self.gender=StringVar()
		self.gender.set("M")
		
		addAnimalFrame.nameLabel=Label(addAnimalFrame, text="Name:")
		addAnimalFrame.nameLabel.grid(row=1, column=1)

		addAnimalFrame.name=Entry(addAnimalFrame, textvariable=self.name)
		addAnimalFrame.name.grid(row=1, column=2)

		addAnimalFrame.genderSelect1=Radiobutton(addAnimalFrame, text="Male", variable=self.gender, value="M")
		addAnimalFrame.genderSelect1.grid(row=3, column=1)
		addAnimalFrame.genderSelect2=Radiobutton(addAnimalFrame, text="Female", variable=self.gender, value="F")
		addAnimalFrame.genderSelect2.grid(row=3, column=2)

		addAnimalFrame.ageSelect=Label(addAnimalFrame, text="Age:")
		addAnimalFrame.ageSelect.grid(row=2, column=1)

		addAnimalFrame.ageSelect=Spinbox(addAnimalFrame, from_=1, to=100, textvariable=self.age)
		addAnimalFrame.ageSelect.grid(row=2, column=2)

		addAnimalFrame.speciesScrollBar=Scrollbar(addAnimalFrame, orient=VERTICAL)
		addAnimalFrame.speciesSelect=Listbox(addAnimalFrame,height=5, yscrollcommand=addAnimalFrame.speciesScrollBar.set, selectmode=SINGLE)
		for item in lsSpecies:
			addAnimalFrame.speciesSelect.insert(END, item)
		addAnimalFrame.speciesScrollBar.config(command=addAnimalFrame.speciesSelect.yview)
		addAnimalFrame.speciesScrollBar.grid(row=4, column=3, ipady=10)
		addAnimalFrame.speciesSelect.grid(row=4, column=2)
		addAnimalFrame.speciesSelect.bind("<<ListboxSelect>>", self.speciesSelector)


		addAnimalFrame.createAnimalButton=Button(addAnimalFrame, text="Add Animal", command=self.createAnimal)
		addAnimalFrame.createAnimalButton.grid(row=5, column=2)



	def speciesSelector(self, listBox):
		listBox=listBox.widget
		self.species=listBox.get(listBox.curselection())

	def createAnimal(self):
		name=str(self.name.get())
		gender=str(self.gender.get())
		try:
			age=int(self.age.get())
			species=str(self.species)
			for animal in lsAnimals:
				if name==animal.name:
					raise DuplicateNameError

			if not name:
				messagebox.showinfo("Error", "Please enter a name")
			else:
				lsAnimals.append(Animal(name, species, age, gender))
				messagebox.showinfo("Success", "%s was successfully added" %(name))

		except TclError:
			messagebox.showwarning("Error", "Input a number as the age")

		except AttributeError:
			messagebox.showwarning("Error", "Choose a species")

		except DuplicateNameError:
			messagebox.showinfo("Error", "Please choose an unique name for your animal")

	def removeAnimal(self):
		removeAnimalFrame=Toplevel()
		removeAnimalFrame.attributes("-topmost", 1)

		removeAnimalFrame.speciesScrollbar=Scrollbar(removeAnimalFrame, orient=VERTICAL)
		removeAnimalFrame.animalsToDelete=Listbox(removeAnimalFrame, yscrollcommand=removeAnimalFrame.speciesScrollbar.set, selectmode=MULTIPLE, width=40)
		for animal in lsAnimals:
			removeAnimalFrame.animalsToDelete.insert(END, "%s, %s, %s, %s" %(animal.name, animal.gender, animal.age, animal.species))
		removeAnimalFrame.speciesScrollbar.config(command=removeAnimalFrame.animalsToDelete.yview)
		removeAnimalFrame.speciesScrollbar.grid(row=1, column=2, ipady=40)
		removeAnimalFrame.animalsToDelete.grid(row=1, column=1)
		removeAnimalFrame.animalsToDelete.bind("<<ListboxSelect>>", self.listBoxSelector)

		removeAnimalFrame.removeButton=Button(removeAnimalFrame, text="Remove Animal(s)", command=lambda:self.deleteAnimalsFromList(removeAnimalFrame))
		removeAnimalFrame.removeButton.grid(row=2, columnspan=2)

	def deleteAnimalsFromList(self, frame):
		result = messagebox.askquestion("Delete", "Are You Sure?")
		if result=="yes":
			for index in self.animalsToDelete:
				lsAnimals.pop(int(index))
				frame.destroy()
			messagebox.showinfo("Success", "Animal(s) was successfully removed")
		elif result=="no":
			pass

	def listBoxSelector(self, listBox):
		listBox=listBox.widget
		self.animalsToDelete=list(reversed(listBox.curselection()))


	def showOverview(self):
		overviewFrame=Toplevel()
		overviewFrame.attributes("-topmost", 1)
		self.ascending=StringVar()
		self.ascending.set(False)
		self.sortingOrder=StringVar()
		self.sortingOrder.set("name")
		overviewFrame.ascending=Radiobutton(overviewFrame, text="Ascending", variable=self.ascending, value=False)
		overviewFrame.ascending.grid(row=1, column=1)
		overviewFrame.descending=Radiobutton(overviewFrame, text="Descending", variable=self.ascending, value=True)
		overviewFrame.descending.grid(row=1, column=2)
		parameterList=["name", "age", "gender", "species"]
		n=1
		for parameter in parameterList:
			overviewFrame.sortingOrder=Radiobutton(overviewFrame, text=parameter, variable=self.sortingOrder, value=parameter)
			overviewFrame.sortingOrder.grid(row=2, column=n)
			n+=1
		self.showAnimals=Button(overviewFrame, text="Show Animals", command=self.printOverview)
		self.showAnimals.grid(row=3)

	def printOverview(self):
		printOverview=Toplevel()
		printOverview.attributes("-topmost", 1)
		sortingOrder=self.sortingOrder.get()
		ascending=self.ascending.get()
		sortedList=sorted(lsAnimals, key=lambda animal: getattr(animal, sortingOrder), reverse=int(ascending))
		info=Text(printOverview)
		if sortingOrder=="name" or sortingOrder=="age":
			for n in range(len(sortedList)):
				animal=sortedList[n]
				info.insert(END, "%s) %s (%s, %s y/o, %s)\n" % (n+1, animal.name, animal.species, animal.age, animal.gender))

		elif sortingOrder=="gender" or sortingOrder=="species":
			lsCategories=[]
			for animal in sortedList:
				lsCategories.append(getattr(animal, sortingOrder))
				uniqueCategories=set(lsCategories)
			for category in uniqueCategories:
				info.insert(END, "\n%s: \n" % (category))
				for animal in sortedList:
					if getattr(animal, sortingOrder)==category:
						info.insert(END, "%s \n"%(animal.name))
		info.pack()


	def searchAnimals(self):
		searchFrame=Toplevel()
		searchFrame.attributes("-topmost", 1)
		searchParameter=StringVar()
		searchBox=Entry(searchFrame, textvariable=searchParameter)
		searchBoxLabel=Label(searchFrame, text="What animal do you want to find?")
		searchButton=Button(searchFrame, text="Search")
		searchBoxLabel.grid(row=1)
		searchBox.grid(row=2)
		searchButton.grid(row=3)

class Error(Exception):
	pass

class DuplicateNameError(Error):
	pass


root = Tk()
mainMenu=AnimalProgram(root)
root.mainloop()