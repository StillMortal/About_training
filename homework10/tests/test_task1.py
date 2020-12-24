import asyncio
import os
from unittest.mock import patch

import pytest
from asynctest.mock import CoroutineMock
from bs4 import BeautifulSoup

from homework10.tasks.task1 import (
    getting_text_from_urls,
    processing_data_on_companies,
    ratio_of_ruble_to_dollar,
    sort_companies,
)


@pytest.fixture(scope="module")
def companies_data():
    companies = {
        "3A": ["AAA", 1000, 0.3, 50, 90],
        "3B": ["BBB", 1100, 0.2, -50, 75],
        "3C": ["CCC", 1200, 0.1, -25, 75],
    }

    return companies


def test_companies_are_sorted_by_price(companies_data):
    metrics = {1: "price"}

    assert list(sort_companies(companies_data, metrics)) == [
        [
            {"code": "3C", "name": "CCC", "price": 1200},
            {"code": "3B", "name": "BBB", "price": 1100},
            {"code": "3A", "name": "AAA", "price": 1000},
        ]
    ]


def test_companies_are_sorted_by_P_E(companies_data):
    metrics = {2: "P_E"}

    assert list(sort_companies(companies_data, metrics)) == [
        [
            {"code": "3C", "name": "CCC", "P_E": 0.1},
            {"code": "3B", "name": "BBB", "P_E": 0.2},
            {"code": "3A", "name": "AAA", "P_E": 0.3},
        ]
    ]


def test_companies_are_sorted_by_growth(companies_data):
    metrics = {3: "growth"}

    assert list(sort_companies(companies_data, metrics)) == [
        [
            {"code": "3A", "name": "AAA", "growth": 50},
            {"code": "3C", "name": "CCC", "growth": -25},
            {"code": "3B", "name": "BBB", "growth": -50},
        ]
    ]


def test_companies_are_sorted_by_potential_profit(companies_data):
    metrics = {4: "potential_profit"}

    assert list(sort_companies(companies_data, metrics)) == [
        [
            {"code": "3A", "name": "AAA", "potential_profit": 90},
            {"code": "3B", "name": "BBB", "potential_profit": 75},
            {"code": "3C", "name": "CCC", "potential_profit": 75},
        ]
    ]


@patch("homework10.tasks.task1.requests.get")
def test_ratio_of_ruble_to_dollar_func(mock_requests_get):
    mock_requests_get.return_value.text = """
    <?xml version="1.0" encoding="windows-1251"?>
    <html>
     <body>
      <valcurs daterange1="24.12.2020" daterange2="01.01.2049">
       <record date="24.12.2020" id="R01235">
        <nominal>
         1
        </nominal>
        <value>
         75,4571
        </value>
       </record>
      </valcurs>
     </body>
    </html>
    """

    assert ratio_of_ruble_to_dollar() == 75.4571


@patch("homework10.tasks.task1.aiohttp.ClientSession.get")
@pytest.mark.asyncio
async def test_getting_text_from_urls_func(mock_aiohttp_ClientSession_get):
    mock_aiohttp_ClientSession_get.return_value.__aenter__.return_value.text = (
        CoroutineMock(side_effect=["custom text"])
    )

    result = await getting_text_from_urls("url")

    assert result == "custom text"


def test_processing_data_on_companies():
    with open(
        os.path.abspath(os.path.dirname(__file__)) + "/company_for_the_test.html"
    ) as tag_tr:
        soup = BeautifulSoup(tag_tr, "lxml")
        company_data = soup.find_all("tr")

    result = asyncio.get_event_loop().run_until_complete(
        processing_data_on_companies(company_data)
    )

    assert result == {
        "ABT": ["Abbott Laboratories", 107.45, 27.22, 23.29, 86.85],
        "AOS": ["AO Smith", 55.11, 21.43, 17.67, 72.8],
        "MMM": ["3M", 173.99, 20.12, 0.17, 60.06],
    }
