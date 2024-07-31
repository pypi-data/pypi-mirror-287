def lunshu(keyword): 

    import pandas as pd  
    file_path = 'lunshu.xlsx'
    df = pd.read_excel(file_path)  
      
    column1 = 'key'  
    column2 = 'values'  
      
    results = [df[column2][df[column1].str.contains(keyword, case=False, na=False)].tolist()]  

    results=[result[0] if result else [] for result in results]
    for result in results:  
        print(result)  


def get_yu():
    yu='''
    yu/
    '''
    print(yu)

def get_long():
    long='''
    long/
    '''
    print(long)