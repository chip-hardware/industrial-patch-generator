#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def route_rhythm(local_mods, add_cable):
    """🎛️ Music routing for BLOCK 2 (RHYTHM). Stable rhythmic grid."""
    seq3 = next((m for m in local_mods if m['meta_type'] == 'SEQ3' or m.get('model', '') == 'SEQ3'), None)
    vco = next((m for m in local_mods if m['meta_type'] in ['VCO', 'WTVCO']), None)
    vca = next((m for m in local_mods if m['meta_type'] in ['VCA', 'VCA-1']), None)

    # 1. Align sequencer and oscillator pitch (Strict linear tracking)
    if seq3 and vco:
        add_cable(seq3['id'], 9, vco['id'], 0, "#8b4ade") # Row 1 CV -> VCO V/OCT

    # 2. Use the second sequencer row for dynamic amplitude modulation (VCA)
    if seq3 and vca:
        add_cable(seq3['id'], 10, vca['id'], 0, "#ff5500") # Row 2 CV -> VCA CV Level

    # 3. Feed percussion sound from oscillator to volume input
    if vco and vca:
        add_cable(vco['id'], 3, vca['id'], 1, "#f3374b") # SQR -> VCA IN