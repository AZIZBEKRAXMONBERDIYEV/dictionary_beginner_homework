def sum_age_values(data:list) -> int:
    """
    Return the sum of all age values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all age values in the dictionary
    """
    l=0
    for i in data:
       if type(i['age'])==int:
           l+=i['age']
       
    return l
data=[{
    'name': 'John', 
    'age': 20
  }, 
{
    'name': 'Mary', 
    'age': 17
  },
{
    'name': 'Ban', 
    'age': 23
  },
{
    'name': 'John', 
    'age': 27
  }
]
print(sum_age_values(data))