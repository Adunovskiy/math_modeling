def average(array = [1, 3]):
    summary = 0
    element = 0
    average = 0
    element = len(array)
    for i in range(element):
        summary += array[i]
    average = summary / element
    print(average)
    
average([1, 2, 3, 4, 5])
        