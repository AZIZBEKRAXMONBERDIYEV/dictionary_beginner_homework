def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    l=[]
    for i in data:
        if type(i['age'])==int:
            l.append(i['age'])
    s=min(l)
    for w in data:
        if s==w['age']:
            d=w['name']
    return str(d) 
data = [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  },
  {
    'name': 'Ban', 
    'age': 29
  }
]
print(get_min_age_user_name(data)) 