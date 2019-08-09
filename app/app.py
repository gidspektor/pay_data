from flask import Flask, render_template, request
from scrapers import open_payment, tools

def create_app():
  app = Flask(__name__)

  
  @app.route('/2015_open_payment')
  def home():
    '''
    This is the 2015 open payment endpoint that does an api
    call to grab json data for 2015 from open payment.
    Then it opens that data and displays it at open_payment.html.
    '''
    tools.api_call_to_grab_data('https://openpaymentsdata.cms.gov/resource/j3ph-dt9p.json', 'pay_data.json')
    data = tools.show_data('pay_data.json')
    return render_template('open_payment.html', data=data)


  @app.route('/open_payment_search', methods=["POST"])
  def search():
    '''
    This opens the pay data json file to be displayed then
    it loads a json object and grabs the user input string from
    the post which is then run through a search function
    and then the search results go to the write to xls file
    function and finally the results are displayed in the html.
    '''
    data = tools.show_data('pay_data.json')
    json = tools.open_json_file('pay_data.json')
    question = request.form["search"]
    results = open_payment.search(question , json)
    tools.write_results_to_xls_file(results)
    return render_template('open_payment.html', data=data, results=results)


  @app.route('/open_payment_full_name_search', methods=["POST"])
  def full_name_search():
    '''
    This opens the pay data json file to be displayed then
    it loads a json object and grabs the user input string from
    the post which is then run through a sanitise function and that is
    put through the search function and then the search results go to
    the write to xls file function and finally the results are
    displayed in the html.
    '''
    data = tools.show_data('pay_data.json')
    json = tools.open_json_file('pay_data.json')
    name = request.form["full_name_search"]
    sanitised_name = open_payment.sanitise_name(name)
    results = open_payment.search_by_name(sanitised_name , json)
    tools.write_results_to_xls_file(results)
    return render_template('open_payment.html', data=data, results=results)  


  return app