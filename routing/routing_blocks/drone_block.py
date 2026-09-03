#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def route_drone(local_mods, add_cable):
    """🪐 Music routing for BLOCK 0 (DRONE). Basic generative line startup."""
    vco = next((m for m in local_mods if m['meta_type'] == 'VCO'), None)
    vco2 = next((m for m in local_mods if m['meta_type'] == 'VCO2'), None)
    vcf = next((m for m in local_mods if m['meta_type'] in ['VCF', 'FILTER']), None)
    vca = next((m for m in local_mods if m['meta_type'] in ['VCA', 'VCA-1', 'VCA-2']), None)
    div = next((m for m in local_mods if m['meta_type'] == 'CM_VC_FREQUENCY_DIVIDER' or 'Divider' in m.get('model', '')), None)
    matrix = next((m for m in local_mods if m['meta_type'] in ['VCMIXER', 'CM_MATRIX_MIXER'] or m.get('model', '') in ['VCMixer', 'MatrixMixer']), None)

    # 1. Form the primary audio core: send waves to frequency divider or filter
    if vco and div:
        add_cable(vco['id'], 2, div['id'], 0, "#f3374b") # SAW -> Divider IN
    
    if vco2 and matrix:
        add_cable(vco2['id'], 1, matrix['id'], 0, "#ffb437") # TRI -> Matrix CH1 IN
        add_cable(vco2['id'], 2, matrix['id'], 1, "#3695ef") # SAW -> Matrix CH2 IN

    # 2. Filter feedbacks (Filter LPF = 4, HPF = 5)
    if vcf and matrix:
        add_cable(matrix['id'], 4, vcf['id'], 0, "#f3374b") # Matrix OUT -> Filter IN
        add_cable(vcf['id'], 4, matrix['id'], 2, "#00b56e") # Filter LPF -> Matrix CH3 (Cyber-feedback)

    # 3. Final output to the VCA line
    if vcf and vca:
        add_cable(vcf['id'], 4, vca['id'], 1, "#f3374b") # Filter LPF -> VCA IN