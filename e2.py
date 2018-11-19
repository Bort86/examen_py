
"""
e2
"""

from typing import List, Tuple


#----------------------------------------------------------------------
def get_exon_ranges(genbank_txt_in: str) -> List[Tuple[int, int]]:
    """Analyzes the text of a genbank file and returns the ranges of the exons.
    Each range is a tuple of ints (start, end).
    Each tuple is like a python range.
    - Indexes start at zero.
    - The end index is excluded.
    Note that this is different from the genbank file format:
    - Indexes start at one.
    - The end index is included.
    """


    return f"PENDING TO DO SOMETHING WITH {genbank_txt_in}"


#----------------------------------------------------------------------
