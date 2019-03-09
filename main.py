#Importing necessary package
import random

#Defining pigeonholeAlgo() with the array as the argument
def pigeonholeAlgo(array):

    # Finding the minimum, maximum of array and number of pigeonHoles
    minA = min(array)
    maxA = max(array)
    noOfHoles = maxA - minA + 1

    # Creating pigeonHoles array filled with Zeros
    pigeonHoles = [0] * noOfHoles

    # Iterate through unsorted array and add 1 to pigeonHoles array's
    # value at the index corresponding to unsorted array's value
    for element in array:
        pigeonHoles[element - minA] += 1

    # Putting the elements back into array in sorted order
    i = 0
    for count in range(noOfHoles):
        while pigeonHoles[count] > 0:
            pigeonHoles[count] -= 1
            array[i] = count + minA
            i += 1

# Driver Code
if __name__ == '__main__':

    # Generate an array of 15 numbers upto the range of 20
    randomArray = random.sample(range(20), 15)

    # Printing the unsorted array
    print("\nBEFORE SORTING : ", end=' ')
    for i in range(len(randomArray)):
        print(randomArray[i], end=' ')

    # Calling pigeonholeAlgo()
    pigeonholeAlgo(randomArray)

    # Printing the sorted array
    print("\n\nSORTED ARRAY : ", end=' ')
    for i in range(len(randomArray)):
        print(randomArray[i], end=' ')
