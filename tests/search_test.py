from scrapers import open_payment,  tools
from tests.results import search_result


def test_search():
  expected = search_result.expected_search_results
  search_input = 'GlaxoSmithKline, LLC.'
  data = tools.open_json_file('tests/pay_data/data.json')
  results = open_payment.search(search_input, data)
  assert expected == results
