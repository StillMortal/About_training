"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


>>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen

"""
import requests


def count_dots_on_i(url: str) -> int:
    """Accepts an URL as input
    and count how many letters `i` are present in the HTML by this URL.

        Args:
            url: URL for the search engine.

        Returns:
            The number of "i" characters.

    """
    try:
        response = requests.get(url)
        num_of_i = 0
        if response.ok:
            for sym in response.text:
                num_of_i += 1 if sym == "i" else 0
        else:
            raise Exception
        return num_of_i
    except Exception:
        raise ValueError(f"Unreachable {url}")
