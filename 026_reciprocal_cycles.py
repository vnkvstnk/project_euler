# Project Euler, problem #26
# Find the value of d < 1000 for which 1/d contains the longest
# recurring cycle in its decimal fraction part.

def long_divide(num, den):
    # Calculate the entier and create mantissa list
    entier = num // den
    mantissa = []
    # Calculate the first residue and save it
    residues = []
    residue = num % den
    residues.append(residue)
    # While residue is not zero
    while residue != 0:
        # Multiply residue by 10 and extract enterier (which is a part of mantissa now)
        # and append it to mantissa list
        next_entier = (residue * 10) // den
        mantissa.append(str(next_entier))
        # Calculate new residue and check if it's already in residues
        residue = (residue * 10) % den
        if residue in residues:
        # If yes, the number has a recurring part
        # Print (optional) the product of division and return the recurring part as a string
            index = residues.index(residue)
            # print(f"{entier}.{''.join(mantissa[0:index])}({''.join(mantissa[index:])})")
            return (''.join(mantissa[index:]))
        # If no, append residue to the residues and continue to calculate
        else:
            residues.append(residue)
    # Print (optional) the product of divisiion and return empty string (length of recurring part is 0)
    # print(f"{entier}.{''.join(mantissa)}")
    return ''


lengths = []
for d in range(1, 1001, 2):
    lengths.append(len(long_divide(1, d)))

print(f"Number {1} / {lengths.index(max(lengths)) * 2 + 1} has the recurring "
      f"cycle of length {max(lengths)}.\n")
