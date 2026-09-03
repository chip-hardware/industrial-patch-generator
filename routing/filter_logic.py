#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from routing_blocks.drone_block import route_drone
from routing_blocks.bass_block import route_bass
from routing_blocks.rhythm_block import route_rhythm
from routing_blocks.noise_block import route_noise
from routing_blocks.melodic_block import route_melodic

def process_filter_routing(clean_chain, add_cable):
    """Master frequency filtering and cross-block routing dispatcher v42.0."""
    row_mixers = {}
    for m in clean_chain:
        if m['meta_type'] in ['MIXER', 'VCMIXER']:
            match = re.search(r'R(\d+)', m.get('text', ''))
            if match: row_mixers[int(match.group(1))] = m

    # Global floor mapper (Collect hardware by rails R0..R4)
    blocks = {r: [] for r in range(5)}
    for m in clean_chain:
        match = re.search(r'R(\d+)', m.get('text', ''))
        if match:
            r_idx = int(match.group(1))
            if r_idx in blocks: blocks[r_idx].append(m)

    # Detect presence of inline sound modifiers
    inline_modifiers_per_row = {r: False for r in range(5)}
    for r_idx, mods in blocks.items():
        for m in mods:
            if m['meta_type'] in ['CM_MANGLER', 'CM_RECTIFIER', 'CM_VOLTAGE_SCALER', 
                                  'CM_SWITCH_1_8', 'CM_SWITCH_1_16', 'CM_CAROUSEL', 
                                  'CM_SUBHARMONIC', 'CM_VC_FREQUENCY_DIVIDER']:
                inline_modifiers_per_row[r_idx] = True

    # 🔗 WAVE 1: STANDARD LINEAR AUDIO ROUTING
    for i in range(len(clean_chain) - 1):
        m_from, m_to = clean_chain[i], clean_chain[i + 1]
        f_type, t_type = m_from['meta_type'], m_to['meta_type']
        
        match_row = re.search(r'R(\d+)', m_from.get('text', ''))
        current_row_idx = int(match_row.group(1)) if match_row else 0
        has_inline_mod = inline_modifiers_per_row.get(current_row_idx, False)

        if current_row_idx == 0 and any(m['meta_type'] == 'CM_MATRIX_MIXER' for m in blocks[0]):
            continue

        if f_type in ['VCO', 'VCO2', 'WTVCO'] and t_type in ['VCF', 'FILTER', 'FREAK']:
            if not has_inline_mod:
                saw_p = 6 if f_type == 'VCO2' else 1
                sqr_p = 5 if f_type == 'VCO2' else 3
                add_cable(m_from['id'], saw_p, m_to['id'], 3, "#f3374b") 
                add_cable(m_from['id'], sqr_p, m_to['id'], 0, "#ffb437") 

        elif f_type == 'NOISE' and t_type in ['VCF', 'FILTER', 'FREAK']:
            if not has_inline_mod:
                add_cable(m_from['id'], 0, m_to['id'], 3, "#f3374b")

        elif f_type in ['MIXER', 'VCMIXER', 'CM_MATRIX_MIXER'] and t_type in ['VCF', 'FILTER', 'FREAK']:
            out_port = 4
            add_cable(m_from['id'], out_port, m_to['id'], 3, "#f3374b")

    master_lfo = next((m for m in clean_chain if m['meta_type'] in ['LFO', 'LFO2', 'WTLFO']), None)
    global_clock = next((m for m in clean_chain if m['meta_type'] == 'CLOCKED'), None)
        
    # 🔗 WAVE 2: DYNAMIC FLOOR DISPATCHER (Calls external blocks)
    route_drone(blocks.get(0, []), add_cable)
    route_bass(blocks.get(1, []), add_cable)
    route_rhythm(blocks.get(2, []), global_clock, add_cable)
    route_noise(blocks.get(3, []), global_clock, master_lfo, add_cable)
    route_melodic(blocks.get(4, []), global_clock, master_lfo, add_cable)

    # Fallback safety for filtering
    for r_idx in range(1, 5):
        for m_curr in blocks.get(r_idx, []):
            if m_curr['meta_type'] in ['VCF', 'FILTER', 'FREAK']:
                if master_lfo: add_cable(master_lfo['id'], 0, m_curr['id'], 2, "#3695ef")
                if global_clock: add_cable(global_clock['id'], 4, m_curr['id'], 2, "#8b4ade")