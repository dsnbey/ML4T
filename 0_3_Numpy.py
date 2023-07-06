import numpy as np

def create_array():
    arr = np.array(([2,3,4],[4,3,2]))
    arr = np.empty(5)
    arr = np.empty((4,5,6))
    arr = np.ones((2,3))
    arr = np.zeros(9, dtype=int)
    arr = np.random.rand(5,4)
    #arr = np.random.normal(loc=0,scale=10,size=(2,2))
    return arr

def attr(arr: np.array):
    att = arr.shape
    att = arr.size # no of elements
    att = arr.dtype
    return att

def math_ops(arr: np.array):
    el = arr.sum(axis=0) # rows->0, colums->1
    el = arr.max(axis=0)
    el = arr.mean() #no axis, function applies to all elements
        
    return el
    
def indexing(arr: np.array):
    indices = np.array([1,3])
    return arr[indices],  arr

def mean_bool_arr(arr: np.array):
    mean_before = arr.mean()
    arr[arr < arr.mean()] = arr.mean() # replace num bers smaller than mean with mean
    mean_after = arr.mean()
    return arr, mean_before, mean_after

    
    
if __name__ == '__main__':
    #print(attr(create_array()))
    #print(math_ops(create_array()))
    #print(indexing(create_array()))
    print(mean_bool_arr(create_array()))
   