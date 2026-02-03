import time

def datarefiner(listx, callback): # first paremeter is list, second is function
    for x in listx:
        print("Refining data:", x)
        callback("Refined " + str(x))
        time.sleep(1)
    print("Data refining completed.")

def  processdata(data):
    print("Processing:", data)

def anotherprocess(data):
    print("Another processing:", data)

listnames = ["set1", "set2", "set3", "set4","batch1","batch2","batch3"]
datarefiner(listnames, processdata)
datarefiner(listnames, anotherprocess)  
datarefiner(listnames, lambda data: print("Lambda processing:", data))

