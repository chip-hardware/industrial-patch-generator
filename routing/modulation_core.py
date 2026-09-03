#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def process_modulation_rings(clean_chain, module_rows, pm):
    """
    Advanced Cross-Modulation and Algorithmic Pitch-Bussing Layer v34.0.
    PART 1: Structure initialization, global macro-modules, and floor parsing.
    """
    # 🔍 GLOBAL SPACE & CONTROL MODULES (Affect the entire rack)
    m_global_reverb = next((m for m in clean_chain if m['meta_type'] == 'PLATEAU' or m['model'] == 'Plateau'), None)
    m_global_clouds = next((m for m in clean_chain if m['meta_type'] == 'CLOUDS' or m['model'] == 'Clouds'), None)
    m_global_clock  = next((m for m in clean_chain if m['meta_type'] == 'CLOCKED' or m['model'] == 'Clocked-Clkd'), None)
    m_global_xy     = next((m for m in clean_chain if m['meta_type'] == 'XYPAD' or m['model'] == 'XYPad'), None)
    m_global_sloth  = next((m for m in clean_chain if m['meta_type'] == 'SLOTHTORPOR' or m['model'] == 'SlothTorpor'), None)
    global_quant_id = next((m['id'] for m in clean_chain if m['meta_type'] in ['QUANT', 'QUANTIZER']), None)

    # Isolate floors for inter-block cross-injections
    blocks = {i: [m for m in clean_chain if module_rows.get(m['id']) == i] for i in range(5)}
    
    def get_row_mod(row_idx, meta_type):
        """Helper utility to find hardware on a specific floor."""
        return next((m for m in blocks.get(row_idx, []) if m['meta_type'] == meta_type), None)

    unique_rows = set(module_rows.values())
    
    for row_idx in unique_rows:
        row_mods = blocks.get(row_idx, [])
        
        # Hardware register on current floor
        m_vco, m_vco2, m_noise, m_vcf, m_delay, m_lfo, m_lfo2, m_seq, m_logic, m_mixer, m_quant, m_vca = None, None, None, None, None, None, None, None, None, None, None, None
        m_cm_div, m_cm_sandh, m_cm_att, m_cm_burst, m_cm_seq8, m_cm_seq16 = None, None, None, None, None, None
        m_cm_rand_gates, m_cm_gate_mod, m_cm_trig_seq, m_cm_g2t, m_cm_vc_switch = None, None, None, None, None
        m_cm_matrix, m_cm_switch, m_cm_rect = None, None, None
        m_cm_mute = next((m for m in row_mods if m['meta_type'] == 'CM_MUTE'), None)

        for m in row_mods:
            if m['meta_type'] in ['VCO', 'WTVCO']: m_vco = m
            if m['meta_type'] == 'VCO2': m_vco2 = m
            if m['meta_type'] == 'NOISE': m_noise = m
            if m['meta_type'] in ['VCF', 'FILTER', 'FREAK']: m_vcf = m
            if m['meta_type'] in ['LFO', 'LFO2', 'WTLFO']: m_lfo = m
            if m['meta_type'] == 'DELAY': m_delay = m
            if m['meta_type'] in ['VCA', 'VCA-1', 'VCA-2']: m_vca = m
            if m['meta_type'] in ['SEQ3', 'SEQ', 'SEQUENCER']: m_seq = m
            if m['meta_type'] == 'LOGIC': m_logic = m
            if m['meta_type'] in ['MIXER', 'VCMIXER']: m_mixer = m
            if m['meta_type'] in ['QUANT', 'QUANTIZER']: m_quant = m
            
            # Count Modula registration
            if m['meta_type'] == 'CM_MATRIX_MIXER': m_cm_matrix = m
            if m['meta_type'] in ['CM_SWITCH_1_8', 'CM_SWITCH_1_16']: m_cm_switch = m
            if m['meta_type'] == 'CM_RECTIFIER': m_cm_rect = m
            if m['meta_type'] == 'CM_SAMPLE_AND_HOLD': m_cm_sandh = m
            if m['meta_type'] == 'CM_CLOCK_DIVIDER': m_cm_div = m
            if m['meta_type'] == 'CM_G2T': m_cm_g2t = m
            if m['meta_type'] == 'CM_BURST_GENERATOR': m_cm_burst = m
            if m['meta_type'] == 'CM_ATTENUVERTER': m_cm_att = m
            if m['meta_type'] == 'CM_SEQUENCER_8': m_cm_seq8 = m
            if m['meta_type'] == 'CM_SEQUENCER_16': m_cm_seq16 = m
            if m['meta_type'] == 'CM_CLOCKED_RANDOM_GATES': m_cm_rand_gates = m
            if m['meta_type'] == 'CM_GATE_MODIFIER': m_cm_gate_mod = m
            if m['meta_type'] == 'CM_TRIGGER_SEQUENCER_8': m_cm_trig_seq = m

        # TRANSITION TO CONNECTIONS... (Code continues in second window)
        # ---------------------------------------------------------------------
        # 🪐 LAYER A: SUPER-MACRO MODULATION (SLOTH / XYPAD / LOOPBACK / FM)
        # ---------------------------------------------------------------------
        if m_global_sloth:
            if m_global_reverb: pm.add_cable(m_global_sloth['id'], 0, m_global_reverb['id'], 2, "#3695ef")
            if m_global_clouds: pm.add_cable(m_global_sloth['id'], 1, m_global_clouds['id'], 4, "#ff00ff")

        if m_global_xy:
            if m_vco:   pm.add_cable(m_global_xy['id'], 0, m_vco['id'], 1, "#ff5500")
            if m_vco2:  pm.add_cable(m_global_xy['id'], 0, m_vco2['id'], 1, "#ff5500")
            if m_vcf:   pm.add_cable(m_global_xy['id'], 1, m_vcf['id'], 1, "#ff00ff")

        if m_cm_matrix and m_delay:
            pm.add_cable(m_delay['id'], 0, m_cm_matrix['id'], 2, "#3695ef")

        if m_vco and m_vcf and not m_cm_matrix:
            pm.add_cable(m_vco['id'], 0, m_vcf['id'], 2, "#ff5500")

        # ---------------------------------------------------------------------
        # 🪐 LAYER B: CROSS-FLOOR PITCH & RHYTHM GATE ROUTING
        # ---------------------------------------------------------------------
        if row_idx == 1:  # BASS LINE
            melodic_seq = get_row_mod(4, 'SEQ3') or get_row_mod(4, 'CM_SEQUENCER_16')
            bass_vco = m_vco if m_vco else m_vco2
            if melodic_seq and bass_vco:
                pitch_src_id = global_quant_id if global_quant_id else melodic_seq['id']
                pitch_src_port = 2 if global_quant_id else 9
                if m_cm_att:
                    pm.add_cable(pitch_src_id, pitch_src_port, m_cm_att['id'], 0, "#11faaa")
                    pm.add_cable(m_cm_att['id'], 0, bass_vco['id'], 2, "#11faaa")
                else:
                    pm.add_cable(pitch_src_id, pitch_src_port, bass_vco['id'], 2, "#11faaa")

        if m_cm_mute and m_global_clock:
            pm.add_cable(m_global_clock['id'], 5, m_cm_mute['id'], 2, "#00b56e")

        if row_idx == 4 and m_delay:  # MELODIC LAYER
            noise_source = get_row_mod(3, 'NOISE')
            if noise_source: pm.add_cable(noise_source['id'], 0, m_delay['id'], 1, "#ff5500")

        # ---------------------------------------------------------------------
        # 🪐 LAYER C: POLYPHONIC & ALGORITHMIC COUNT MODULA ROUTING
        # ---------------------------------------------------------------------
        m_cm_inverter = next((m for m in row_mods if m['meta_type'] == 'CM_VOLTAGE_INVERTER'), None)
        if m_cm_inverter and m_lfo and m_vcf:
            pm.add_cable(m_lfo['id'], 0, m_cm_inverter['id'], 0, "#3695ef")
            pm.add_cable(m_cm_inverter['id'], 0, m_vcf['id'], 1, "#ff00ff")

        m_cm_carousel = next((m for m in row_mods if m['meta_type'] == 'CM_CAROUSEL'), None)
        if m_cm_carousel and m_global_clock:
            pm.add_cable(m_global_clock['id'], 4, m_cm_carousel['id'], 0, "#8b4ade")
            if m_noise and m_vco:
                pm.add_cable(m_vco['id'], 1, m_cm_carousel['id'], 1, "#f3374b")
                pm.add_cable(m_noise['id'], 0, m_cm_carousel['id'], 2, "#ff5500")
                if m_vcf: pm.add_cable(m_cm_carousel['id'], 0, m_vcf['id'], 3, "#f3374b")

        m_cm_offset = next((m for m in row_mods if m['meta_type'] == 'CM_OFFSET_GENERATOR'), None)
        if m_cm_offset and m_vco:
            pm.add_cable(m_cm_offset['id'], 0, m_vco['id'], 1, "#ff5500")

        if m_global_clock and m_cm_burst:
            pm.add_cable(m_global_clock['id'], 4, m_cm_burst['id'], 2, "#8b4ade")
            gate_src_id, gate_src_port = m_cm_burst['id'], 0
            if m_cm_gate_mod:
                pm.add_cable(m_cm_burst['id'], 0, m_cm_gate_mod['id'], 0, "#00b56e")
                gate_src_id, gate_src_port = m_cm_gate_mod['id'], 0
            if m_vca: pm.add_cable(gate_src_id, gate_src_port, m_vca['id'], 0, "#00b56e")

        if m_cm_rand_gates and m_global_clock:
            pm.add_cable(m_global_clock['id'], 4, m_cm_rand_gates['id'], 0, "#8b4ade")
            gate_src_id, gate_src_port = m_cm_rand_gates['id'], 0
            if m_cm_gate_mod:
                pm.add_cable(m_cm_rand_gates['id'], 0, m_cm_gate_mod['id'], 0, "#00b56e")
                gate_src_id, gate_src_port = m_cm_rand_gates['id'], 0
            if m_vca and not m_cm_burst: pm.add_cable(gate_src_id, gate_src_port, m_vca['id'], 0, "#00b56e")

        if m_cm_trig_seq and m_global_clock:
            pm.add_cable(m_global_clock['id'], 4, m_cm_trig_seq['id'], 0, "#8b4ade")
            if m_cm_g2t and not m_cm_burst:
                pm.add_cable(m_cm_trig_seq['id'], 0, m_cm_g2t['id'], 0, "#8b4ade")
                if m_vca: pm.add_cable(m_cm_g2t['id'], 0, m_vca['id'], 0, "#00b56e")

        if m_cm_trig_seq or m_cm_seq8 or m_cm_seq16:
            active_seq = m_cm_trig_seq if m_cm_trig_seq else (m_cm_seq8 if m_cm_seq8 else m_cm_seq16)
            if m_global_clock:
                pm.add_cable(m_global_clock['id'], 4, active_seq['id'], 0, "#8b4ade")
                if m_quant: pm.add_cable(active_seq['id'], 0, m_quant['id'], 0, "#00b56e")

        if m_cm_div and m_seq:
            pm.add_cable(m_cm_div['id'], 0, m_seq['id'], 0, "#8b4ade")
        elif m_cm_div and m_cm_seq8:
            pm.add_cable(m_cm_div['id'], 1, m_cm_seq8['id'], 0, "#8b4ade")

        if m_cm_sandh:
            sh_trigger_src = m_cm_div['id'] if m_cm_div else (m_global_clock['id'] if m_global_clock else None)
            sh_port = 2 if m_cm_div else 4
            if sh_trigger_src: pm.add_cable(sh_trigger_src, sh_port, m_cm_sandh['id'], 1, "#8b4ade")
            if m_vco: pm.add_cable(m_cm_sandh['id'], 0, m_vco['id'], 2, "#00b56e")

        active_cm_seq = m_cm_seq8 if m_cm_seq8 else (m_cm_seq16 if m_cm_seq16 else None)
        if active_cm_seq:
            target_quant_id = m_quant['id'] if m_quant else (global_quant_id if global_quant_id else None)
            if target_quant_id:
                pm.add_cable(active_cm_seq['id'], 0, target_quant_id, 0, "#00b56e")
                if m_vco: pm.add_cable(target_quant_id, 2, m_vco['id'], 2, "#00b56e")

        # ---------------------------------------------------------------------
        # 🪐 LAYER D: EMERGENCY SYSTEM FAILSAFES (SYSTEM FAILSAFES v34.0)
        # ---------------------------------------------------------------------
        if not m_seq and not m_cm_seq8 and not m_cm_seq16 and not m_cm_sandh and not m_cm_trig_seq:
            if m_vco and m_global_clock:
                pm.add_cable(m_global_clock['id'], 4, m_vco['id'], 1, "#8b4ade")
            if m_vco2 and global_quant_id:
                pm.add_cable(global_quant_id, 2, m_vco2['id'], 2, "#00b56e")
        
        if m_logic and not m_seq:
            if m_vco:   pm.add_cable(m_vco['id'], 3, m_logic['id'], 0, "#8b4ade")
            elif m_lfo: pm.add_cable(m_lfo['id'], 0, m_logic['id'], 0, "#8b4ade")