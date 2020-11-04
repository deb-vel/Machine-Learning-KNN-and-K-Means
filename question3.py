import csv
import random
import math
import operator
import numpy as np

def calculate_distance(p, q, length): #calculates euclidian distance
    distance = 0
    for i in range(length):#for all test data
        distance += np.square(p[i] - q[i]) #calculate this part of equation: (p-q)^2 + (b-a)^2+....
    return np.sqrt(distance) #square root the total of distances


def nearest_neighbors(testData, trainingData):
    k = math.sqrt(len(trainingData)) #square root of the amount of training data
    k = int(k)#in case the answer is float change it to integer

    distances = []
    length = len(testData)-1 # length of testData minus one as it starts from 0

    #for every training data instance
    for data in range(len(trainingData)):
        #calculate the distance between the testing instance and the training data
        distance = calculate_distance(testData, trainingData[data], length)
        #populate the array with the distances and their corresponding training data
        distances.append((trainingData[data], distance))

    #sort the array distances in ascending order
    distances.sort(key=operator.itemgetter(1))

    nearest_neighbors = []
    #store the first k distances which are the smallest
    for kvalue in range(k):
        nearest_neighbors.append(distances[kvalue][0])

    return nearest_neighbors


def getResult(neighbors):
    neighborClasses = []
    #for all first k distances (loops through all neighbours)
    for x in range(len(neighbors)):
        flowerClass = neighbors[x][-1] #gets the class of each neighbor i.e Iris-setosa, iris-virginica or Iris-versicolor
        neighborClasses.append(flowerClass) #add each flower class to the array of all found classes
    result = max(neighborClasses, key = neighborClasses.count) #find most common class in the array
    return result


def main():

    trainingData = []
    testingData = []
    split = 0.8 #set to 0.8 to generate accurate results

    #read text file
    with open('iris.data.txt', 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        dataset = list(lines) #stored in an array, each element contains a line from the txt file
        #randomly splitting the dataset into training data and test data
        for x in range(len(dataset) - 1):
            for y in range(4):
                 dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingData.append(dataset[x])
            else:
                testingData.append(dataset[x])

    #output amount of training set and test set for the user to know
    print('Number of data for training set: ' + repr(len(trainingData)))
    print('Number of data to test: ' + repr(len(testingData)))

    for x in range(len(testingData)): # for each testing data
        neighbors = nearest_neighbors(testingData[x], trainingData) #get the nearest neighbors
        result = getResult(neighbors) #get the class the test set should belong to
        #print results and test data to compare the actual class with the predicted one
        print('Test data: ')
        print(testingData[x])
        print('K-NN result=' + result)
    input("Press enter to exit ;)")


main()