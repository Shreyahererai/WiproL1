BookStore = {"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter","J K.Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
print ("\nBOOKSTORE\n")
for dic in BookStore.values():
	for i in dic.values():
		str1=str(i)
		str1=str1[1:len(str1)-1]
		print(str1)
print("\n")