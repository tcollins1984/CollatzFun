import pandas as pd
def collatz_df(x):
    if type(x) != int:
        print('your number must be a positive integer')
    elif (type(x) == int and x < 1):
        print('your number must be a positive integer')
    else:
        number_step =[[x,0]]
        steps = 0
        while x>1:
            if x%2 == 0:
                x = x/2
                steps +=1 
                
            else:
                x = 3*x + 1
                steps = steps + 1
            number_step.append([x,steps])
   
    df_collatz = pd.DataFrame(data=number_step,columns=['number','steps'])
    return df_collatz