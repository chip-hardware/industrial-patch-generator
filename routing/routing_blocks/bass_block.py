#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def route_bass(local_mods, add_cable):
    """🎹 West-Coast routing for BLOCK 1 (BASS). Stable audio core injection."""
    vco = next((m for m in local_mods if m['meta_type'] in ['VCO', 'WTVCO']), None)
    vco2 = next((m for m in local_mods if m['meta_type'] == 'VCO2'), None)
    vcf = next((m for m in local_mods if m['meta_type'] in ['VCF', 'FILTER']), None)
    vca = next((m for m in local_mods if m['meta_type'] in ['VCA', 'VCA-1']), None)
    matrix = next((m for m in local_mods if m['meta_type'] in ['VCMIXER', 'CM_MATRIX_MIXER'] or m.get('model', '') in ['VCMixer', 'MatrixMixer']), None)
    inv = next((m for m in local_mods if m['meta_type'] in ['CM_VOLTAGE_INVERTER', 'CM_INVERTER'] or 'Inverter' in m.get('model', '')), None)

    # 1. Route oscillators into MatrixMixer
    if matrix:
        if vco: add_cable(vco['id'], 2, matrix['id'], 0, "#3695ef") 
        if vco2: add_cable(vco2['id'], 2, matrix['id'], 1, "#ff5500") 
        if vcf: add_cable(matrix['id'], 4, vcf['id'], 0, "#f3374b") # Matrix OUT -> Filter IN
    elif vco and vcf:
        add_cable(vco['id'], 2, vcf['id'], 0, "#f3374b") 

    # 2. Modulation through inverter
    if vco and inv and vcf:
        add_cable(vco['id'], 0, inv['id'], 0, "#3695ef")  
        add_cable(inv['id'], 0, vcf['id'], 1, "#00b56e")  

    # 3. Output to VCA
    if vcf and vca:
        add_cable(vcf['id'], 4, vca['id'], 1, "#f3374b")