
"""
e1
"""
import re
import utilslib
from typing import List

#----------------------------------------------------------------------
def get_dna_seq(genbank_txt_in: str) -> str:
    """Analyzes a genbank text string and extracts the DNA string.
    The DNA string is output in capital letters, wihtout whitespace or newlines.
    All DNA letters are allowed.
    """
    f = ""
    final_string = ""
    
    reg = r'\s'
    pat = re.compile(reg)
    f = re.sub(pat, "", genbank_txt_in)
    
    reg2=r'ORIGIN(.*)//$'
    pat2 = re.compile(reg2)
    
    match = pat2.search(f)

    f= match.group(1)


    reg3 = r'[0-9]'
    pat3 = re.compile(reg3)
    
    f = re.sub(pat3, "", f)

    final_string = f.upper()

    return final_string
#----------------------------------------------------------------------

genbank_txt = utilslib.read_file('genbank/lysozyme-1-mus-musculus.gbff')

print(get_dna_seq(genbank_txt))
