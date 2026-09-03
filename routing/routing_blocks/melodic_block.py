#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def route_melodic(local_mods, add_cable):
    """🚀 Music routing for BLOCK 4 (MELODIC). Pure melodic line."""
    seq3 = next((m for m in local_mods if m['meta_type'] == 'SEQ3' or 'SEQ3' in m.get('model', '')), None)
    quant = next((m for m in local_mods if m['meta_type'] in ['QUANT', 'QUANTIZER']), None)
    vco = next((m for m in local_mods if m['meta_type'] in ['VCO', 'WTVCO']), None)
    vcf = next((m for m in local_mods if m['meta_type'] in ['VCF', 'FILTER']), None)
    vca = next((m for m in local_mods if m['meta_type'] in ['VCA', 'VCA-1']), None)
    comp = next((m for m in local_mods if m['meta_type'] in ['CM_COMPARATOR', 'CM_GATED_COMPARATOR']), None)

    # 1. Send raw unquantized step voltages to the Quantizer input
    if seq3 and quant:
        add_cable(seq3['id'], 9, quant['id'], 0, "#8b4ade") # Row 1 CV -> Quantizer IN

    # 2. Perfectly tuned semitones from Quantizer feed into the VCO pitch bus
    if quant and vco:
        add_cable(quant['id'], 2, vco['id'], 0, "#3695ef") # Quantizer OUT -> VCO V/OCT

    # 3. Route the melody audio signal into the filter
    if vco and vcf:
        add_cable(vco['id'], 1, vcf['id'], 0, "#f3374b") # TRI -> Filter IN

    # 4. Logic comparator modulates filter opening depending on the sequence step
    if seq3 and comp:
        add_cable(seq3['id'], 11, comp['id'], 0, "#ff5500") # Row 3 CV -> Comparator IN
    if comp and vcf:
        add_cable(comp['id'], 0, vcf['id'], 1, "#00b56e") # Comp OUT -> Filter FREQ

    # 5. Melody exits through its own VCA
    if vcf and vca:
        add_cable(vcf['id'], 4, vca['id'], 1, "#f3374b") # Filter LPF -> VCA IN