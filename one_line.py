
#map(lambda x:labels[x],map(result_distance.index,sorted(result_distance)[0:3]))[map(map(lambda x:labels[x],map(result_distance.index,sorted(result_distance)[0:3])).count,map(lambda x:labels[x],map(result_distance.index,sorted(result_distance)[0:3]))).index(max(map(map(lambda x:labels[x],map(result_distance.index,sorted(result_distance)[0:3])).count,map(lambda x:labels[x],map(result_distance.index,sorted(result_distance)[0:3])))))]
#map(lambda x:labels[x],
from math import sqrt;
# distance = lambda a,b:sqrt(sum(pow(a[0]-b[0],2.0),pow(a[1]-b[1],2.0)))
lambda testdata:sorted(map(lambda x:distance(testdata,x),dataSet))
# distance lambda (lambda x,y:abs(x-y))
lambda a,b:sqrt(
    (lambda x,y:x+y) # float sum 
    (pow((lambda x,y:abs(x-y))(a[0],b[0]),2.0),
     pow((lambda x,y:abs(x-y))(a[1],b[1]),2.0))
    )
# rest
((lambda distance:map(lambda x:distance([1.0,1.1],x),
                     [[1.0,1.1],
                     [1.0,1.0],
                     [0.0,0.0],
                     [0.0,0.1]]))
(lambda a,b:sqrt(
    (lambda x,y:x+y) # float sum 
    (pow((lambda x,y:abs(x-y))(a[0],b[0]),2.0),
     pow((lambda x,y:abs(x-y))(a[1],b[1]),2.0))
    ))
 )
# test time
import time
from math import sqrt
t1 = time.clock()
# data


group = [[1.0,1.1],
         [1.0,1.0],
         [0.0,0.0],
         [0.0,0.1]]
labels = ['A','A','B','B']
test = [1.0,1.1]
#(lambda distance:map(lambda x:distance(testdata,x),dataSet))


result = (lambda testdata,dataSet,label,k:
    (lambda x:x[0][x[1].index(max(x[1]))])
    ((lambda x:[x,map(x.count,x)])
    (map(lambda x:label[x],#result
    (lambda x:map(x[0].index,x[1][0:k]))#index
    (
        (lambda lst:[lst,sorted(lst)])# sorted and var
        ((lambda distance:map(lambda x:distance(testdata,x),dataSet))
            (lambda a,b:sqrt((lambda x,y:x+y) # float sum 
            (pow((lambda x,y:abs(x-y))(a[0],b[0]),2.0),
             pow((lambda x,y:abs(x-y))(a[1],b[1]),2.0))
            ))
        )
    )
         ))
     )
 )(test,group,labels,3)

print "%f,%s"%(time.clock()-t1,result)
# kNN just a line
print (lambda testdata,dataSet,label,k:(lambda x:x[0][x[1].index(max(x[1]))])((lambda x:[x,map(x.count,x)])(map(lambda x:label[x],(lambda x:map(x[0].index,x[1][0:k]))((lambda lst:[lst,sorted(lst)])((lambda distance:map(lambda x:distance(testdata,x),dataSet))(lambda a,b:sqrt((lambda x,y:x+y)(pow((lambda x,y:abs(x-y))(a[0],b[0]),2.0),pow((lambda x,y:abs(x-y))(a[1],b[1]),2.0))))))))))([1.0,1.1],[[1.0,1.1],[1.0,1.0],[0.0,0.0],[0.0,0.1]],['A','A','B','B'],3)
