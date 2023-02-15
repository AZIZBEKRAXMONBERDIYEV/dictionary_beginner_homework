def sum_even_values(data: dict) -> int:
    '''
    Return the sum of all even values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all even values in the dictionary
    '''
    x=[]
    s=0
    l=[]
    for i in data.values():
        if type(i)==int:
            l.append(i)
    for w in l:
        if w %2==0:
            x.append(w)
    for d in x:
        s+=d
    return s
data = {
    1: 22, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  }
print(sum_even_values(data))