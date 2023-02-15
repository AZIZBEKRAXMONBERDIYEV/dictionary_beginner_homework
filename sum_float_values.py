def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    s=0
    l=[]
    for i in data.values():
        if type(i)==float:
            l.append(i)
    for w in l:
        s+=w
    return s
data  = data = {
    1: 22.4, 
    2: 3.5, 
    4: 1, 
    6: 7.6, 
    5: 2, 
    7: 3
  }
print(sum_float_values(data))