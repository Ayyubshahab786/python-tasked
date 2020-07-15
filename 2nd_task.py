def average_cal(*args):
    print(type(args))
    
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
print(average_cal([4,6,7], [7,2,5]))