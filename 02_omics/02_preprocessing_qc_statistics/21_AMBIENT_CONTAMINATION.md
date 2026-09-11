# Ambient contamination

Ambient RNA is released material in a suspension or droplet background and can be captured by another cell; free antibody can similarly affect ADT. A weak marker in an otherwise incompatible profile may be contamination, but it may also be real low expression. Empty droplets help estimate background RNA but are not automatically equivalent to cells [S18,S47,S48].

SoupX estimates an ambient profile and contamination fraction; DecontX models native and contaminating expression. Both add assumptions and can remove genuine signal when populations resemble one another. ADT requires antibody-specific background controls [S07]. Record whether a matrix is corrected, the tool/version, inputs and parameters. Our source files are not corrected in this phase. Evidence: EmptyDrops [S18], Young et al. [S47], Yang et al. [S48], Mulè et al. [S07].
