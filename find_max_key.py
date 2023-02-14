def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    l=[]
    for i in data:
        l.append(i)
        a=max(l) 
    return a
data = {
    1.4 :'a', 
    7.8 :'b', 
    4 : 'c'
  } 
print(find_max_key(data))