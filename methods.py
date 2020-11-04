import numpy as np
from mpl_toolkits.mplot3d import Axes3D
Axes3D = Axes3D

def choose_one_feature(): #prompt user to choose a feature
    print("Press 1 for Sepal Length")
    print("Press 2 for Sepal Width")
    print("Press 3 for Petal length")
    print("Press 4 for Petal Width")

def apply_nos_to_choice(feature):  #for each possible input return a particular number to then be added together in question 1.py
        if feature == '1':
            return 50
        elif feature == '2':
            return 66
        elif feature == '3':
            return 40
        elif feature == '4':
            return 95
        else:
            print("Wrong input!")
            return 0


def one_scatter(setosa,versicolor,virginica,plt,x): #plots for 1 feature
    y = np.zeros(np.shape(setosa))  # Make all y values set to zero
    plt.xlim(0, 10)
    plt.ylim(0, 0.2)
    plt.plot(setosa, y, 'ro', marker='o', markersize=4, c='r', label='Iris-setosa')
    plt.plot(versicolor, y, 'ro', marker='o', markersize=4, c='b', label='Iris-versicolor')
    plt.plot(virginica, y, 'ro', marker='o', markersize=4, c='g', label='Iris-virginica')
    plt.axis('auto')
    plt.xlabel(x)
    plt.ylabel('y')
    plt.legend(loc=2)
    plt.show()

#plots in 2D
def two_scatter(setosa1,setosa2,versicolor1,versicolor2,virginica1,virginica2,x,y,plt):
    plt.scatter(setosa1, setosa2, c='red',s=5, label='Iris-setosa')
    plt.scatter(versicolor1, versicolor2, s=5,c='blue', label='Iris-Versicolor')
    plt.scatter(virginica1, virginica2,s=5, c='green', label='Iris-Virginica')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend(loc=1)
    plt.show()

#plots in 3D
def three_scatter(setosa1,setosa2,setosa3,versicolor1,versicolor2,versicolor3, virginica1,virginica2,virginica3,x,y,z,plt):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(setosa1, setosa2, setosa3, c='r', marker='o',label='Iris-setosa')
    ax.scatter(versicolor1,versicolor2,versicolor3, c='b', marker='o', label='Iris-Versicolor')
    ax.scatter(virginica1,virginica2,virginica3,c='g', marker='o', label='Iris-Virginica')
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    plt.legend(loc=1)
    plt.show()