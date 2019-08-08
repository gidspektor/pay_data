from scrapers import open_payment
from tests.results import name_search_result


def test_full_name_search():
  expected = name_search_result.expected_full_name_search_results
  search_input = 'Halim Fadil'
  name = open_payment.sanitise_name(search_input)
  data = open_payment.open_json_file('tests/pay_data/data.json')
  results = open_payment.search_by_name(name, data)
  assert expected == results