from collections import Counter

def Gini(a,b):
    a = float(a)
    b = float(b)
    if a==0 and b==0:
        return 0
    else:
        return (1-(a/(a+b))**2-(b/(a+b))**2)



def best_axis_cut(dataset,column,target):
    final_gini_low = 1000
    final_gini_upp = 1000
    
    #column_points = column_points[float(item) for item in dataset[column]]
    for i in dataset[column]:
        print(i)
        low = dataset[dataset[column]<=i]
        upp = dataset[dataset[column]>i]
        print( "Uncool: ",Counter(low[target])['uncool'],'\n\n')
        gini_low = Gini(Counter(low[target])['cool'],Counter(low[target])['uncool'])
        gini_upp = Gini(Counter(upp[target])[0],Counter(upp[target])[1])
        print(gini_low,gini_upp)
        if final_gini_low > gini_low:
            final_gini_low = gini_low

        if final_gini_upp > gini_upp:
            final_gini_upp = gini_upp
        
    return final_gini_low,final_gini_upp    

        