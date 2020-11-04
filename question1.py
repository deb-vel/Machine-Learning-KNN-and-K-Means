import csv
import methods
import matplotlib.pyplot as plt

#arrays that will store all data respective to their class
setosa1 = []  #stores sepal length for Iris-Setosa
setosa2 = []  #stores sepal width for Iris-Setosa
setosa3= []   #stores petal length for Iris-Setosa
setosa4 = []  #stores petal width for Iris-Setosa

versicolor1 = []  #stores sepal length for Iris-Versicolor
versicolor2 = []  #stores sepal width for Iris-Versicolor
versicolor3= []   #stores petal length for Iris-Versicolor
versicolor4 = []  #stores petal width for Iris-Versicolor

virginica1 = []  #stores sepal length for Iris-Virginica
virginica2 = []  #stores sepal width for Iris-Virginica
virginica3= []   #stores petal length for Iris-Virginica
virginica4 = []  #stores petal width for Iris-Virginica

#opening file an populating the arrays above
with open('iris.data.txt', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in plots:
            if(i < 50): #collect all features for iris-setosa
                    setosa1.append(float(row[0]))
                    setosa2.append(float(row[1]))
                    setosa3.append(float(row[2]))
                    setosa4.append(float(row[3]))
            elif(i<100): #collect all features for iris-versicolor
                    versicolor1.append(float(row[0]))
                    versicolor2.append(float(row[1]))
                    versicolor3.append(float(row[2]))
                    versicolor4.append(float(row[3]))
            elif(i<150): #collect all features for iris-virginica
                    virginica1.append(float(row[0]))
                    virginica2.append(float(row[1]))
                    virginica3.append(float(row[2]))
                    virginica4.append(float(row[3]))
            i += 1


choice = input('Choose number of features (e.g. 1,2,3): ')

if choice == '1': #caters for 1 feature
    methods.choose_one_feature() #displays choice of features
    feature = input()
    #according to the feature selected, the method one_scatter is called passing the chosen feature as parameter
    if feature == '1':
        x = 'Sepal Length cm'
        methods.one_scatter(setosa1, versicolor1, virginica1, plt,x)
    elif feature == '2':
        x = 'Sepal Width cm'
        methods.one_scatter(setosa2,versicolor2,virginica2,plt,x)
    elif feature == '3':
        x = 'Petal Length cm'
        methods.one_scatter(setosa3,versicolor3,virginica3,plt,x)
    elif feature == '4':
        x = 'Petal Width cm'
        methods.one_scatter(setosa4,versicolor4,virginica4,plt,x)
    else:
        print("Wrong input!")

elif choice == '2': #caters for 2 features
    #ask user to choose a feature twice
    methods.choose_one_feature()
    feature = input()
    no1 = methods.apply_nos_to_choice(feature) #according to what number was inputted, get a new number

    methods.choose_one_feature()
    feature2 = input()
    no2 = methods.apply_nos_to_choice(feature2) #according to what number was inputted, get a new number

    addition = no2 + no1 #add the numbers we get from the function methods.apply_nos_to_choice()

    if addition == 116: #It means that 1 and 2 where chosen irrispective of order
        x='Sepal Length cm'
        y='Sepal Width cm'
        methods.two_scatter(setosa1,setosa2,versicolor1,versicolor2,virginica1,virginica2,x,y,plt)
    elif addition == 90: #It means that 1 and 3 where chosen irrispective of order
        x = 'Sepal Length cm'
        y = 'Petal Length cm'
        methods.two_scatter(setosa1, setosa3, versicolor1, versicolor3, virginica1, virginica3,x,y, plt)
    elif addition == 145: #It means that 1 and 4 where chosen irrispective of order
        x = 'Sepal Length cm'
        y = 'Petal Width cm'
        methods.two_scatter(setosa1, setosa4, versicolor1, versicolor4, virginica1, virginica4,x,y ,plt)
    elif addition == 106: #It means that 2 and 3 where chosen irrispective of order
        x = 'Sepal Width cm'
        y = 'Petal Length cm'
        methods.two_scatter(setosa2, setosa3, versicolor2, versicolor3, virginica2, virginica3, x, y, plt)
    elif addition == 161: #It means that 2 and 4 where chosen irrispective of order
        x = 'Sepal Width cm'
        y = 'Petal Width cm'
        methods.two_scatter(setosa2, setosa4, versicolor2, versicolor4, virginica2, virginica4, x, y, plt)
    elif addition == 135: #It means that 3 and 4 where chosen irrispective of order
        x = 'Petal Length cm'
        y = 'Petal Width cm'
        methods.two_scatter(setosa3, setosa4, versicolor3, versicolor4, virginica3, virginica4, x, y, plt)
    else:
        print("Wrong input!")

elif choice == '3':
    methods.choose_one_feature()
    feature = input()
    no1 = methods.apply_nos_to_choice(feature)
    methods.choose_one_feature()
    feature2 = input()
    no2 = methods.apply_nos_to_choice(feature2)
    methods.choose_one_feature()
    feature3 = input()
    no3 = methods.apply_nos_to_choice(feature3)

    addition = no3 + no1 +no2

    if addition == 156:  # It means that 1,2 and 3 where chosen irrispective of order
        x = 'Sepal Length cm'
        y = 'Sepal Width cm'
        z = 'Petal Length cm'
        methods.three_scatter(setosa1, setosa2,setosa3, versicolor1, versicolor2,versicolor3, virginica1, virginica2,virginica3, x, y,z, plt)
    elif addition == 211:  # It means that 1,2 and 4 where chosen irrispective of order
        x = 'Sepal Length cm'
        y = 'Sepal Width cm'
        z = 'Petal Width cm'
        methods.three_scatter(setosa1, setosa2, setosa4, versicolor1, versicolor2, versicolor4, virginica1, virginica2, virginica4, x, y,z, plt)
    elif addition == 185:  # It means that 1, 3 and 4 where chosen irrispective of order
        x = 'Sepal Length cm'
        y = 'Petal Length cm'
        z = 'Petal Width cm'
        methods.three_scatter(setosa1, setosa3, setosa4, versicolor1, versicolor3, versicolor4, virginica1, virginica3, virginica4, x, y,z, plt)
    elif addition == 201:  # It means that 2, 3 and 4 where chosen irrispective of order
        x = 'Sepal Width cm'
        y = 'Petal Length cm'
        z = 'Petal Width cm'
        methods.three_scatter(setosa2, setosa3, setosa4, versicolor2, versicolor3, versicolor4, virginica2, virginica3, virginica4, x, y, z,plt)
    else:
        print("Wrong input!")
else:
   print("Wrong input!")