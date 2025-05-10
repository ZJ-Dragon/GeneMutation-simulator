from Bio.Seq import Seq  # Biopython
CODON_TABLE = "Standard"

def complement(template: str) -> str:
    return str(Seq(template).reverse_complement())

def transcribe(coding: str) -> str:
    return str(Seq(coding).transcribe())

def translate(mrna: str) -> list[str]:
    seq = Seq(mrna)
    protein = seq.translate(table=CODON_TABLE, to_stop=False)
    return list(str(protein))  # 后面可映射到中文氨基酸

def mutate(template: str, mtype: str, pos: str, base: str | None = None) -> str:
    """
    Apply a point or range mutation on a DNA template strand (3'→5').

    Parameters
    ----------
    template : str
        Original DNA template sequence (only A/T/G/C, case‑insensitive).
    mtype : str
        Mutation type: "sub"  (substitution),
                       "ins"  (insertion),
                       "del"  (deletion).
    pos : str
        1‑based index or range. Examples:
            "7"     → position 7
            "3-5"   → positions 3 through 5 (inclusive)
        For insertion, the new base will be inserted *before* the index provided.
    base : str | None
        New nucleotide for "sub" or "ins". Ignored for "del".

    Returns
    -------
    str
        Mutated DNA template sequence.

    Raises
    ------
    ValueError
        If parameters are invalid.
    """
    seq = list(template.upper())
    valid_nt = {"A", "T", "G", "C"}

    if mtype not in {"sub", "ins", "del"}:
        raise ValueError(f"Unknown mutation type: {mtype}")

    # Validate base when required
    if mtype in {"sub", "ins"}:
        if base is None or base.upper() not in valid_nt:
            raise ValueError("A valid base (A/T/G/C) must be provided for substitution or insertion.")
        base = base.upper()

    # Helper to parse 1‑based index or range
    def _parse_pos(p: str) -> tuple[int, int]:
        if "-" in p:
            start, end = map(int, p.split("-"))
            if start > end:
                start, end = end, start
        else:
            start = end = int(p)
        return start - 1, end - 1  # convert to 0‑based

    start_idx, end_idx = _parse_pos(pos)

    if mtype == "sub":
        if start_idx < 0 or start_idx >= len(seq):
            raise ValueError("Substitution index out of range.")
        seq[start_idx] = base

    elif mtype == "ins":
        if start_idx < 0 or start_idx > len(seq):
            raise ValueError("Insertion index out of range.")
        seq.insert(start_idx, base)

    elif mtype == "del":
        if start_idx < 0 or end_idx >= len(seq):
            raise ValueError("Deletion range out of range.")
        del seq[start_idx : end_idx + 1]

    return "".join(seq)