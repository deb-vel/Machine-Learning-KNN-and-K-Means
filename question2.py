import numpy as np
import methods
import csv
import matplotlib.pyplot as plt
from copy import deepcopy
from mpl_toolkits.mplot3d import Axes3D
Axes3D = Axes3D

def dist(p, q, ax=1):
    return np.linalg.norm(p - q, axis=ax) #calculates euclidean distance

def k_means(data, num_features, number):
    k = 3

    centroids_x = []
    centroids_y = []
    x = 0
    if number == 4: #For when the fourth feature is chosen.  This requires different ranges from which random numbers can be picked
        #else, one of the centroid will get a position from where it can never get a cluster of its own
        while x < 3:
            if num_features == 3: # pick random numbers for centroids for 3D space
                centroids_x = np.random.uniform(low=4.1, high=6.1, size=(3,))#x values
                centroids_y = np.random.uniform(low=0.0, high=2.0, size=(3,))#y values
                centroids_z = np.random.uniform(low=0.0, high=2.5, size=(3,))#z values
            elif num_features == 1: # pick random numbers for centroids for 1D space
                centroids_x = np.random.uniform(low=0.1, high=6.1, size=(3,)) #x values
                centroids_y = np.zeros(len(centroids_x))#y values all zeros
            else: ## pick random numbers for centroids for 2D space
                centroids_x = np.random.uniform(low=4.1, high=6.1, size=(3,))#x values
                centroids_y = np.random.uniform(low=0.0, high=2.0, size=(3,))#y values
            x += 1
    else:#if feature 4 is never chosen execute the below with different ranges for random centroids
        while x < 3:
            if num_features == 3:
                centroids_x = np.random.uniform(low=4.1, high=6.1, size=(3,))
                centroids_y = np.random.uniform(low=0.0, high=1.0, size=(3,))
                centroids_z = np.random.uniform(low=2.1, high=4.5, size=(3,))
            elif num_features == 1:
                centroids_x = np.random.uniform(low=0.1, high=6.1, size=(3,))
                centroids_y = np.zeros(len(centroids_x))
            else:
                centroids_x = np.random.uniform(low=4.1, high=6.1, size=(3,))
                centroids_y = np.random.uniform(low=2.1, high=4.5, size=(3,))

            x += 1

    #join the arrays into one array of centroids x,y,z positions
    if num_features == 3:
        centroids_new = np.array(list(zip(centroids_x, centroids_y, centroids_z)), dtype=np.float32)
    else: #join the arrays into one array of centroids x,y positions
        centroids_new = np.array(list(zip(centroids_x, centroids_y)), dtype=np.float32)


    # To store the value of centroids when it updates
    centroids_old = np.zeros(centroids_new.shape) #set to zeros for the first time
    # Cluster labels(0, 1, 2)
    clusters = np.zeros(len(data))

    # calculate distances between old centres and new centers.
    converge = dist(centroids_new, centroids_old, None)

    # Loop will run till the error becomes zero
    while converge != 0:
        # Assigning each value to its closest cluster
        for i in range(len(data)):
            distances = dist(data[i], centroids_new) #calculate distance between all data and each centroid
            cluster = np.argmin(distances) #returns 0,1 or 2 according to which is the smallest distance
            clusters[i] = cluster #stores values of 0,1 and 2 denoting each cluster

        # update the old centroids with the current centroids
        centroids_old = deepcopy(centroids_new)

        #for each cluster
        for i in range(k):
            # get the points of the cluster i
            ith_cluster_points = [data[j] for j in range(len(clusters)) if clusters[j] == i]

            if ith_cluster_points:  # if list is not empty
                centroids_new[i] = np.mean(ith_cluster_points, axis=0) #calculate mean of that cluster for new centroids
            else:#if empty
                #find another random position for the centroid to eventually have points to collect in its cluster
                if (number == 4):
                    centroids_new[i] = np.random.uniform(low=0.0, high=2.0)
                else:
                    centroids_new[i] = np.random.uniform(low=3.1, high=6.1)
        #calculate the distance between new centroids and old ones
        converge = dist(centroids_new, centroids_old, None)

    #to be used when plotting the clusters
    colors = ['r', 'g', 'b']

    if num_features == 1: #plot for 1D
        plt.figure()
        for i in range(k): #plot a cluster at a time
            points = np.array([data[j] for j in range(len(clusters)) if clusters[j] == i])
            y = np.zeros(np.shape(points))  # Make all y values the same
            plt.xlim(0, 10)
            plt.ylim(0, 0.2)
            plt.plot(points, y, 'ro', marker='o', markersize=4,c=colors[i])#plot point in i'th cluster
            plt.axis('tight')
        y = [0, 0, 0]
        plt.plot(centroids_new[:, 0], y, 'ro', marker='*', c='#050505')#plot centroids
    elif num_features == 2: #plot for 2D
        for i in range(k):#plot a cluster at a time
            points = np.array([data[j] for j in range(len(clusters)) if clusters[j] == i])
            plt.scatter(points[:, 0], points[:, 1], s=20, c=colors[i])#plot point in i'th cluster
            plt.scatter(centroids_new[:, 0], centroids_new[:, 1], marker='*', s=100, c='#050505')
    elif num_features == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for i in range(k):#plot a cluster at a time
            points = np.array([data[j] for j in range(len(clusters)) if clusters[j] == i])
            ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=colors[i])#plot point in i'th cluster
            ax.scatter(centroids_new[:, 0], centroids_new[:, 1], centroids_new[:, 2], marker='*', s=180, c='#050505') #plot centroids
    plt.show()


def main():
    #each column will contain all date of one particular feature
    column1 = [] #contains Sepal Length
    column2 = [] #contains Sepal Width
    column3 = [] # contains Petal Length
    column4 = [] # Contains Petal Width

    #read text file and populate arrays above
    with open('iris.data.txt', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            column1.append(float(row[0]))
            column2.append(float(row[1]))
            column3.append(float(row[2]))
            column4.append(float(row[3]))

    choice = input('Choose number of features (e.g. 1,2,3): ')

    if choice == '1':  # caters for 1 feature
        methods.choose_one_feature()  # displays choice of features
        feature = input()
        # according to the feature selected, the method one_scatter is called passing the chosen feature as parameter
        if feature == '1':
            np.array(column1)
            k_means(column1, 1, 0) #pass column 1, number of features, and if Petal width is chosen
        elif feature == '2':
            k_means(column2, 1, 0) #pass column 1, number of features, and if Petal width is chosen
        elif feature == '3':
            k_means(column3, 1, 0) #pass column 1, number of features, and if Petal width is chosen
        elif feature == '4':
            k_means(column4, 1, 4) #pass column 1, number of features, and if Petal width is chosen, in this case yes so pass number 4


    elif choice == '2':  # caters for 2 features

        methods.choose_one_feature()
        feature = input()
        no1 = methods.apply_nos_to_choice(feature)
        methods.choose_one_feature()
        feature2 = input()
        no2 = methods.apply_nos_to_choice(feature2)

        addition = no2 + no1

        if addition == 116:  # It means that 1 and 2 where chosen irrispective of order
            data = np.array(list(zip(column1, column2))) #join the 2 arrays into one 2D array
            k_means(data, 2, 0)  #pass 2Darray of data, number of features, pass 0 cause 4th feature not chosen
        elif addition == 90:  # It means that 1 and 3 where chosen irrispective of order
            data = np.array(list(zip(column1, column3)))#join the 2 arrays into one 2D array
            k_means(data, 2, 0) #pass 2Darray of data, number of features, pass 0 cause 4th feature not chosen
        elif addition == 145:  # It means that 1 and 4 where chosen irrispective of order
            data = np.array(list(zip(column1, column4)))#join the 2 arrays into one 2D array
            k_means(data, 2, 4)  #pass 2Darray of data, number of features, pass 4 cause 4th feature is chosen
        elif addition == 106:  # It means that 2 and 3 where chosen irrispective of order
            data = np.array(list(zip(column2, column3)))#join the 2 arrays into one 2D array
            k_means(data, 2, 0)  #pass 2Darray of data, number of features, pass 0 to later choose the right random centroids
        elif addition == 161:  # It means that 2 and 4 where chosen irrispective of order
            data = np.array(list(zip(column2, column4)))#join the 2 arrays into one 2D array
            k_means(data, 2, 4)  #pass 2Darray of data, number of features, pass 4 cause 4th feature is chosen
        elif addition == 135:  # It means that 3 and 4 where chosen irrispective of order
            data = np.array(list(zip(column3, column4)))#join the 2 arrays into one 2D array
            k_means(data, 2, 4)  #pass 2Darray of data, number of features, pass 4 cause 4th feature is chosen

    elif choice == '3':  #caters for 3 features
        methods.choose_one_feature()
        feature = input()
        no1 = methods.apply_nos_to_choice(feature)
        methods.choose_one_feature()
        feature2 = input()
        no2 = methods.apply_nos_to_choice(feature2)
        methods.choose_one_feature()
        feature3 = input()
        no3 = methods.apply_nos_to_choice(feature3)

        addition = no3 + no1 + no2

        if addition == 156:  # It means that 1,2 and 3 where chosen irrispective of order
            data = np.array(list(zip(column1, column2, column3))) #join 3 arrays into one 3D array
            k_means(data, 3, 0)#pass 3D array of data, number of features, pass 0 cause 4th feature not chosen
        elif addition == 211:  # It means that 1,2 and 4 where chosen irrispective of order
            data = np.array(list(zip(column1, column2, column4)))#join 3 arrays into one 3D array
            k_means(data, 3, 0)#pass 3D array of data, number of features, pass 0 cause 4th feature not chosen
        elif addition == 185:  # It means that 1, 3 and 4 where chosen irrispective of order
            data = np.array(list(zip(column1, column3, column4)))#join 3 arrays into one 3D array
            k_means(data, 3, 4)#pass 3D array of data, number of features, pass 4 cause 4th feature is chosen
        elif addition == 201:  # It means that 2, 3 and 4 where chosen irrispective of order
            data = np.array(list(zip(column2, column3, column4)))#join 3 arrays into one 3D array
            k_means(data, 3, 4)#pass 3D array of data, number of features, pass 4 cause 4th feature is chosen
        else:
            print("Wrong input!")
    else:
        print("Wrong input!")


main() #execute main