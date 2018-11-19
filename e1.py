
"""
e1
"""
import re

#----------------------------------------------------------------------
def get_dna_seq(genbank_txt_in: str) -> str:
    """Analyzes a genbank text string and extracts the DNA string.
    The DNA string is output in capital letters, wihtout whitespace or newlines.
    All DNA letters are allowed.
    """
    f = ""
    
    f=genbank_txt_in.replace('\s','')
    f=f.replace(r'[0-9]*', "")
    
    """
    I tried to erase all whitespace from genbank file, then look for ORIGIN, then
    everything else until the end, then try not to get either numbers or special chars (//)
    but I can't, I'm sorry
    """
    f= f.upper()
    return f

#----------------------------------------------------------------------
