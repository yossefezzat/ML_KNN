import csv
import math
import operator


def loadTrainData(trainSet=[]):
     with open(r'TrainData.txt')as csvfile:
        lines=csv.reader(csvfile)
        data=list(lines)
        for row in range (len(data)-1):
        
            for coloumn in range(8):
                data[row][coloumn]=float(data[row][coloumn])
                
            trainSet.append(data[row]) 
            
            #print(row)
        return None
            
def loadTestData(testSet=[]):
     with open(r'TestData.txt')as csvfile:
        lines=csv.reader(csvfile)
        data=list(lines)
        for row in range (len(data)-1):
        
            for coloumn in range(8):
                data[row][coloumn]=float(data[row][coloumn])
                
            testSet.append(data[row])
            
        return None
        
def Euclidean(obj1,obj2,features):
    distance=0
    for i in range(features):
        distance+=pow((obj1[i]-obj2[i]),2)
    return math.sqrt(distance)     
 
def NN(test,trainSet,k):
    distances=[]
    for i in range(len(trainSet)-1):
        temp=Euclidean(test,trainSet[i],(len(test)-1))
        distances.append((trainSet[i],temp))
    distances.sort(key=operator.itemgetter(1))    
    NN=[]
    for x in range(k):
        #distance fyha two features l data w distance w bsbt zero 3shn yrg3 data bs awl coloumn
        NN.append(distances[x][0])
    return NN   
def predict(NN,trainSet):
    #used sets 3shan a3ml access bl value
    ExistanceNo={}
    for i in range(len(NN)):
        #-1 hna 3shn 23ml access l a5er feature el label
        test=NN[i][-1]
        if test in ExistanceNo:
            ExistanceNo[test]+=1
        else:
            ExistanceNo[test]=1
            #da array mn lkber aktr 7aga etkrrt fl awal
    choosen=sorted(ExistanceNo.items(),key=operator.itemgetter(1),reverse=True)
    
    if len(choosen)>1:
        similar=[]
        index=[]
        
        for z in range(len(choosen)):
            if choosen[0][1] ==choosen[z][1]:
                #print(choosen[z][0])
                #print(choosen[0][0])
                similar.append(choosen[z])
        for k in range(len(similar)):
             for j in range(len(trainSet)):
                 if (similar[k][0] ==trainSet[j][-1]):
                     
                     index.append((similar[k][0],j))
                     break
              
        index.sort(key=operator.itemgetter(1)) 
        #print(len(index))
        #print(index[0][0])
        return index[0][0]

    else:
        #print(choosen[0][0])
        return choosen[0][0]
        
    
         
  
        
def Accuracy(testSet,predicted):
    count=0
    for i in range(len(testSet)):
        
        if testSet[i][-1] == predicted[i]:
            count+=1
    print('Number of correctly classified instances :'+repr(count))
    print('Total number of instances :'+repr(len(testSet)))        
    val=(count/float(len(testSet)))    
    return val
        
def KNN():
    k=[3]
    for x in range(len(k)):
        print('K ='+repr(k[x]))
        TrainData=[]
        TestData=[]           
        loadTrainData(TrainData)  
        loadTestData(TestData) 
        
        predicted=[]
        for i in range(len(TestData)):
           nearestNeighbours=NN(TestData[i],TrainData,k[x])
           result=predict(nearestNeighbours,TrainData)
           predicted.append(result)
           print('Predicted class'+repr(result)+'Actual class'+repr(TestData[i][-1]))
        acc=Accuracy(TestData,predicted)
        print('Accuracy : '+repr(acc))
        
KNN()  
    
  
    
     
        
       