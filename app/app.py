from flask import Flask, render_template, request
from scrapers import open_payment

def create_app():
  app = Flask(__name__)


  @app.route('/')
  def home():
    open_payment.grab_json_data()
    data = open_payment.show_data()
    return render_template('home.html', data=data)


  @app.route('/search', methods=["POST"])
  def search():
    data = open_payment.show_data()
    json = open_payment.open_json_file('pay_data.json')
    question = request.form["search"]
    results = open_payment.search(question , json)
    open_payment.write_results_to_file(results)
    return render_template('home.html', data=data, results=results)


  @app.route('/full_name_search', methods=["POST"])
  def full_name_search():
    data = open_payment.show_data()
    json = open_payment.open_json_file('pay_data.json')
    name = request.form["full_name_search"]
    sanitised_name = open_payment.sanitise_name(name)
    results = open_payment.search_by_name(sanitised_name , json)
    open_payment.write_results_to_file(results)
    return render_template('home.html', data=data, results=results)  


  return app