
"""
e3
"""


#----------------------------------------------------------------------
def make_fasta_str(comment_in: str, seq_in: str) -> str:
    """Writes comment_in and seq_in to to filename_in in the FASTA format.
    The FASTA format is as follows:
    - The first line starts with a '>' and is comment_in.
    - The rest of the lines contain seq_in.
    Checks:
    - Each line must be 70 chars long.
      - The comment line can be shorter.
      - The last line can be shorter.
    - Each line must end in a newline
      - Except the last line.
      - The newline can be the 71th char.
      - There must be no blank lines.
    - If there is any kind of error, throw a ValueError exception.
    """


    return f"PENDING TO DO SOMETHING WITH {comment_in} and {seq_in}"


#----------------------------------------------------------------------
