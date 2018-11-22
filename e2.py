
"""
e2
"""

from typing import List, Tuple

import re

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

    reg = r'exon\s*([0-9]+)..([0-9]+)'
    pat = re.compile(reg)
    matches = pat.finditer(genbank_txt_in)

    array_exon = [(int(e.group(1))-1, int(e.group(2))-1)  for e in matches]

    return array_exon
#----------------------------------------------------------------------
