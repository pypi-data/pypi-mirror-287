import pytest
from cerina import search_text

def test_search_text():
    query = "Tecosys.in"
    results = search_text(query)
    assert isinstance(results, list)
    if results:
        assert "title" in results[0]
        assert "href" in results[0]
        assert "body" in results[0]
