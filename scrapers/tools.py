import urllib, json, pandas as pd


def api_call_to_grab_data(url, file_name):
  '''
  This takes in a url and the name of a file.
  It does an api call to the url and takes the data 
  it receives to then store it in a bytes file 
  defined by file_name.
  '''
  response = urllib.request.urlopen(url)
  with open(file_name, 'wb') as file:
    return file.write(response.read())


def show_data(file_name):
  '''
  This takes in a file name and then 
  opens the file and returns the read file.
  '''
  with open(file_name, 'rb') as file:
    return file.read()


def open_json_file(json_file):
  '''
  This takes in the name of a json file 
  and then does a json load to load the file
  and returns it.
  '''
  with open(json_file) as file:
    data = json.load(file)
  return data


def write_results_to_xls_file(results):
  '''
  This takes in a list or a dictionary or a list
  filled with dictionairies and then uses pandas
  to put that data into rows and columns and saves it
  to an xls file in results.
  '''
  data_frame = pd.DataFrame(results)
  return data_frame.to_excel('app/static/results/results.xls')    