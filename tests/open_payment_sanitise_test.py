from scrapers import open_payment
import pytest


def test_sanitise():
  search_input = 'Brian Bernard'
  expected = ['brian', 'bernard']
  results = open_payment.sanitise_name(search_input)
  assert expected == results


def test_sanitise_string_too_short():
  search_input = 'brian'
  with pytest.raises(Exception):
    assert open_payment.sanitise_name(search_input)


def test_sanitise_string_too_long():
  search_input = 'brian h bernard '
  with pytest.raises(Exception):
    assert open_payment.sanitise_name(search_input)    