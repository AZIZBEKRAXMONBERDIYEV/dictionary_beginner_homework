def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    """for i in data:"""
    l=[]
    for i in data:
        if type(i['age'])==int:
            l.append(i['age'])
    s=max(l)
    
    for w in data:
        if s==w['age']:
            d=w['name']
    x1="'"
    x2="'"
    x3=x1+d+x2       
    return x3
data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
print(get_max_age_user_name(data))