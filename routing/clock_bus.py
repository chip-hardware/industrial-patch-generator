#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def process_clock_routing(clean_chain, raw_lines, module_rows, add_cable):
    """Clock, gate, and through-sync matrix layer v17.0"""
    global_clock_id = None
    for m in clean_chain:
        if m['meta_type'] == 'CLOCKED':
            global_clock_id = m['id']
            break

    for row_idx in range(len(raw_lines)):
        row_modules = [m for m in clean_chain if module_rows.get(m['id']) == row_idx]
        
        row_seq = None
        row_vca = None
        row_clocked = None
        row_logic = None
        row_midi = None
        row_randoms = [] # Convert to array for duplicate detection!
        
        for m in row_modules:
            if m['meta_type'] in ['SEQ', 'SEQUENCER', 'SEQ3']: row_seq = m
            if m['meta_type'] in ['VCA', 'VCA-1', 'VCA-2']: row_vca = m
            if m['meta_type'] == 'CLOCKED': row_clocked = m
            if m['meta_type'] == 'LOGIC': row_logic = m
            if m['meta_type'] == 'MIDI-CV': row_midi = m
            if m['meta_type'] in ['RANDOM', 'RANDOMVALUES', 'S&H']: row_randoms.append(m)
            
        # Through-sync for the sequencer
        if row_clocked and row_seq: 
            add_cable(row_clocked['id'], 4, row_seq['id'], 0, "#8b4ade")
        elif global_clock_id and row_seq:
            add_cable(global_clock_id, 4, row_seq['id'], 0, "#8b4ade")
            
        if row_clocked and row_logic:
            add_cable(row_clocked['id'], 4, row_logic['id'], 0, "#8b4ade")
        elif global_clock_id and row_logic:
            add_cable(global_clock_id, 4, row_logic['id'], 0, "#8b4ade")
            
        if row_seq and row_vca: 
            add_cable(row_seq['id'], 12, row_vca['id'], 0, "#00b56e")
            
        if row_midi and row_vca:
            add_cable(row_midi['id'], 1, row_vca['id'], 0, "#00b56e")
            
        # CLOCK ALL RANDOMIZERS ON THE FLOOR (Duplicate fix v17.0)
        for rand_mod in row_randoms:
            clock_source = row_clocked['id'] if row_clocked else global_clock_id
            if clock_source:
                add_cable(clock_source, 4, rand_mod['id'], 0, "#8b4ade")