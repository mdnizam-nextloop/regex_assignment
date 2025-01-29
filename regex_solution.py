import re
from difflib import SequenceMatcher


def extract_citations(text):
    """
    Extracts citations matching SCC and AIR formats from the given text.
    Returns a list of matched citations.
    """
    pattern = r"(\d{4}\s?\(?.?\)?\s?(SCC|AIR|SC)\s?\(?.*?\)?\s?\d+)"
    matches = re.findall(pattern, text, re.IGNORECASE)
    return [" ".join(match).strip() for match in matches]


def extract_with_typos(text, threshold=0.8):
    """
    Extracts citations considering possible typos using a similarity ratio.
    Matches close variations of SCC or AIR formats from the text.
    """
    pattern = r"(\d{4}\s?\(?.?\)?\s?(SCC|AIR|SC)\s?\(?.*?\)?\s?\d+)"
    candidates = re.findall(r"(\S+)", text)
    valid_citations = []

    for candidate in candidates:
        for match in re.finditer(pattern, candidate, re.IGNORECASE):
            similarity = SequenceMatcher(None, match.group(0), candidate).ratio()
            if similarity >= threshold:
                valid_citations.append(match.group(0))

    return valid_citations
