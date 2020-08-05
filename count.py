from collections import Counter

def Gini(a,b):
    a = float(a)
    b = float(b)
    if a==0 and b==0:
        return 0
    else:
        return (1-(a/(a+b))**2-(b/(a+b))**2)



def best_axis_cut(dataset,column,target):
   
    final_gini_index = 1
    key_1 = dataset[target].unique()[0]
    key_2 = dataset[target].unique()[1]
   
    for i in dataset[column]:
        low = dataset[dataset[column]<=i]
        upp = dataset[dataset[column]>i]
        gini_low = Gini(Counter(low[target])[key_1],Counter(low[target])[key_2])
        gini_upp = Gini(Counter(upp[target])[key_1],Counter(upp[target])[key_2])
        
        M_1 = len(low.index)
        M_2 = len(upp.index)
        gini_index = gini_low*(M_1/(M_1+M_2)) + gini_upp*(M_2/(M_1+M_2))
        
        if gini_index <final_gini_index:
            final_gini_index = gini_index
        else:
            final_gini_index = final_gini_index
        
    return final_gini_index    

        