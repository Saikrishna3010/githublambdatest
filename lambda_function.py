import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [1,2], 'col2': [5,6]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')
    print('sai')
    #todo 
