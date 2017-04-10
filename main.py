#coding=utf-8
#+Author: Commoners
#+Email: a2550591@gmail.com
#+Date: <2017-04-06 星期四>

import kNN
from math import sqrt
import copy
import timeit
#print kNN.p_sqrt(float(10000))
#print sqrt(float(10000))
#t1= timeit.timeit('import kNN;kNN.p_sqrt(float(10000))')
#t2= timeit.timeit('from math import sqrt;sqrt(float(10000))')
#print t1,t2

group = [[1.0,1.1],
         [1.0,1.0],
         [0.0,0.0],
         [0.0,0.1]]
labels = ['A','A','B','B']
# sqrt(sum(pow(sub(x_n)),pow(sub(y_n))))
print [group[i] for i in range(len(group))]
print labels
sub = lambda x,y:abs(x-y)
SUM = lambda x,y:x+y
def distance(a,b):
    dist = kNN.p_sqrt(SUM(kNN.p_pow(sub(a[0],b[0]),2.0),kNN.p_pow(sub(a[1],b[1]),2.0)))
    return dist

test = [1.0,1.1]
#print distance(test,group[0])
result_distance = map(lambda x:distance(test,x),group)
print result_distance

def k_min(lst):
    k_mins = lst[0]
    for i in lst:
        if k_mins > i:
            k_mins = i
    return k_mins
def k_max(lst):
    k_maxs = lst[0]
    for i in lst:
        if k_maxs < i:
            k_maxs = i
    return k_maxs
def k_label(result,label):
    return label[result.index(k_min(result))]

print k_min(result_distance)
print k_label(result_distance,labels)

def k_NN(testdata,dataSet,label,k):
    rest = map(lambda x:distance(testdata,x),dataSet)
    print rest
    crest = sorted(rest)
#    crest = copy.deepcopy(rest)
#    crest.sort()
    print crest
#    crest[0:k]
    index = map(rest.index,crest[0:k])
    print index
    result = map(lambda x:label[x],index)
    print result
    result_count = map(result.count,result)
    print result_count
    print result[result_count.index(k_max(result_count))]

print 'result:',map(lambda x:labels[x],
                    map(result_distance.index,
                        sorted(result_distance)[0:3]))[map(map(lambda x:labels[x],
                                                               map(result_distance.index,
                                                                   sorted(result_distance)[0:3])).count,
                                                           map(lambda x:labels[x],
                                                               map(result_distance.index,
                                                                   sorted(result_distance)[0:3]))).index(max(map(map(lambda x:labels[x],
                                                                                                                     map(result_distance.index,sorted(result_distance)[0:3])).count,map(lambda x:labels[x],map(result_distance.index,sorted(result_distance)[0:3])))))]
k_NN(test,group,labels,3)


