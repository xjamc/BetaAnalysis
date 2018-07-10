#! /usr/bin/env python3

def get_scaffold_variants(data, chrom_call, pos_call, scaff_id, filt):
    chrom = data[chrom_call][:]
    pos = data[pos_call][:]
    scaff = chrom == scaff_id
    vfilt = np.logical_and(filt, scaff)
    chromf = chrom.compress(vfilt, axis=0)
    posf = pos.compress(vfilt, axis=0)
    scaff_pos = np.cumsum(vfilt)
    variant_positions = allel.SortedIndex(
        posf[scaff_pos[0]:scaff_pos[-1]]
    )
    return variant_positions