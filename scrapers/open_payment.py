

def search(search_input, data):
  '''
  This takes in a search input string and some data
  in a dictionary. It then for each's over it 
  to check if the input string matches a value inside
  of the dictionary. If it matches it appends the data block
  to results and returns an array containing dictionaries.
  '''
  results = []
  for block in data:
    for information in block:
      if search_input.lower() == block[information].lower():
        results.append(block)
      else:
        pass  
  return results      


def search_by_name(name_input, data):
  '''
  This takes in name input which is a full name in a
  list and it takes in the data a dictionary which
  it then for each's over and checks if there are keys
  of first names and last names in the block. It then checks
  if the input first name and last name match the ones in the block,
  if it returns true then it appends it to results and returns results.
  '''
  results = []
  for block in data:
    if 'physician_first_name' in block and 'physician_last_name' in block:
      if all([block['physician_first_name'].lower() == name_input[0] \
        and block['physician_last_name'].lower() == name_input[1]]):
        results.append(block)
  return results


def sanitise_name(name_input):
  '''
  This takes in a first and last name string
  which it puts into lower case and then splits it
  into a list and checks if the length is less than 2
  characters or longer than 2 then it reaises an exception.
  It returns a list containing the name.
  '''
  name_input = name_input.lower()
  name_input = name_input.split()
  if len(name_input) < 2:
    raise Exception('string too short')
  elif len(name_input) > 2:
    raise Exception('string too long')
  else:
    return name_input