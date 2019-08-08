import urllib, json, pandas as pd


def grab_json_data():
  response = urllib.request.urlopen('https://openpaymentsdata.cms.gov/resource/j3ph-dt9p.json')
  with open('pay_data.json', 'wb') as file:
    return file.write(response.read())


def show_data():
  with open('pay_data.json', 'rb') as file:
    return file.read()


def open_json_file(json_file):
   with open(json_file) as file:
    data = json.load(file)
    return data


def search(search_input, data):
  results = []
  for block in data:
    for information in block:
      if search_input.lower() == block[information].lower():
        results.append(block)
  return results      


def search_by_name(name_input, data):
  results = []
  for block in data:
    if 'physician_first_name' in block and 'physician_last_name' in block:
      if all([block['physician_first_name'].lower() == name_input[0] \
        and block['physician_last_name'].lower() == name_input[1]]):
        results.append(block)
  return results


def write_results_to_file(results):
  data_frame = pd.DataFrame(results)
  return data_frame.to_excel('app/static/results/results.xls')


def sanitise_name(name_input):
  name_input = name_input.lower()
  name_input = name_input.split()
  if len(name_input) < 2:
    raise Exception('string too short')
  elif len(name_input) > 2:
    raise Exception('string too long')
  else:
    return name_input