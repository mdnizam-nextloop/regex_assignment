import pytest
from regex_solution import extract_citations, extract_with_typos


def test_extract_citations():
    text1 = "Pfizer, 2018 (2) SCC 39, it is held that exercise of power..."
    text2 = "State of H.P., (2018) 1 SCC 202."
    text3 = "in Rustom Cavasji Cooper ((1970) 1 SCC 248)."
    text4 = "[AIR 2019 SC 1296]."
    assert extract_citations(text1) == ["2018 (2) SCC 39"]
    assert extract_citations(text2) == ["2018 1 SCC 202"]
    assert extract_citations(text3) == ["1970 1 SCC 248"]
    assert extract_citations(text4) == ["AIR 2019 SC 1296"]


def test_extract_with_typos():
    text1 = "Pfizer, 2018 (2) SCCC 39, it is held that..."
    text2 = "[AIIR 2019 SC 1296]."
    assert extract_with_typos(text1, threshold=0.8) == ["(2) SCCC 39"]
    assert extract_with_typos(text2, threshold=0.8) == ["AIIR 2019 SC 1296"]
