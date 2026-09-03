#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import random

def process_audio_lanes(clean_chain, module_rows, pm):
    """
    Audio Lane Processing Engine v32.0 (Strict Default Recovery & Stability Fix).
    """
    m_master_mixer = next((m for m in clean_chain if m['model'] == 'rexmix'), None)
    m_master_comp = next((m for m in clean_chain if m['model'] == 'squinkylabs-comp'), None)
    m_master_verb = next((m for m in clean_chain if m['model'] == 'Plateau'), None)
    m_master_dist = next((m for m in clean_chain if m['model'] == 'SurgeXTFXDistortion'), None)
    m_global_io = next((m for m in clean_chain if m['meta_type'] in ['AUDIO', 'AUDIO2'] or m['model'] in ['AudioInterface', 'AudioInterface2']), None)

    has_global_master = all([m_master_mixer, m_master_comp, m_master_verb, m_master_dist, m_global_io])

    unique_rows = set(module_rows.values())
    
    for row_idx in unique_rows:
        row_mods = [m for m in clean_chain if module_rows.get(m['id']) == row_idx]
        
        m_vco, m_vco2, m_noise, m_delay, m_mixer, m_vca, m_lfo = None, None, None, None, None, None, None
        row_vcfs = []
        
        m_cm_rect, m_cm_sub, m_cm_mute, m_cm_freq_div, m_cm_fade = None, None, None, None, None
        m_cm_mangler, m_cm_morph, m_cm_gate_comp, m_cm_scaler, m_cm_att = None, None, None, None, None
        m_cm_switch1_8, m_cm_switch1_16, m_cm_switch8_1, m_cm_switch16_1, m_cm_slope = None, None, None, None, None
        
        # --- New strict mapper accounting for various module database variants ---
        for m in row_mods:
            m_meta = m.get('meta_type', '')
            m_model = m.get('model', '')

            if m_meta == 'VCO': m_vco = m
            if m_meta == 'VCO2': m_vco2 = m
            if m_meta == 'NOISE': m_noise = m
            if m_meta == 'DELAY': m_delay = m
            if m_meta == 'LFO' or m_model == 'LFO': m_lfo = m # 👈 LFO recognition fix
            if m_meta in ['MIXER', 'VCMIXER']: m_mixer = m
            if m_meta in ['VCA', 'VCA-1', 'VCA-2']: m_vca = m
            if m_meta in ['VCF', 'FILTER']: row_vcfs.append(m)
            
            if m_meta == 'CM_RECTIFIER' or m_model == 'Rectifier': m_cm_rect = m
            if m_meta == 'CM_SUBHARMONIC' or m_model == 'Subharmonic': m_cm_sub = m
            if m_meta == 'CM_MUTE' or m_model == 'Mute': m_cm_mute = m
            if m_meta == 'CM_FADE' or m_model == 'Fade': m_cm_fade = m
            if m_meta == 'CM_VC_FREQUENCY_DIVIDER': m_cm_freq_div = m
            if m_meta == 'CM_MANGLER' or m_model == 'Mangler': m_cm_mangler = m
            if m_meta == 'CM_MORPH_SHAPER' or m_model == 'MorphShaper': m_cm_morph = m
            if m_meta == 'CM_GATED_COMPARATOR': m_cm_gate_comp = m
            
            # 👈 Fix for VoltageScaler and Attenuverter (accounting for both name variants from the database)
            if m_meta in ['CM_VOLTAGE_SCALER', 'VoltageScaler'] or m_model == 'VoltageScaler': m_cm_scaler = m
            if m_meta in ['CM_ATTENUVERTER', 'Attenuverter'] or m_model == 'Attenuverter': m_cm_att = m
            
            if m_meta == 'CM_SWITCH_1_8' or m_model == 'Switch1To8': m_cm_switch1_8 = m
            if m_meta == 'CM_SWITCH_1_16' or m_model == 'Switch1To16': m_cm_switch1_16 = m
            if m_meta == 'CM_SWITCH_8_1' or m_model == 'Switch8To1': m_cm_switch8_1 = m
            if m_meta == 'CM_SWITCH_16_1' or m_model == 'Switch16To1': m_cm_switch16_1 = m
            if m_meta == 'CM_SLOPE_DETECTOR' or m_model == 'SlopeDetector': m_cm_slope = m

        m_vcf = row_vcfs if row_vcfs else None

        # ---------------------------------------------------------------------
        # 🧪 PHASE A: CHOOSE INITIAL AUDIO CORE GENERATION SOURCE
        # ---------------------------------------------------------------------
        src_module = m_vco2 if m_vco2 else (m_vco if m_vco else (m_noise if m_noise else None))
        if not src_module: continue
        
        current_id = src_module['id']
        current_port = 6 if src_module == m_vco2 else 1
        if src_module == m_noise: current_port = 0

        if m_cm_slope:
            slope_src_id = m_lfo['id'] if m_lfo else current_id
            slope_src_port = 0 if m_lfo else current_port
            pm.add_cable(slope_src_id, slope_src_port, m_cm_slope['id'], 0, "#3695ef")

        # ---------------------------------------------------------------------
        # 🧪 PHASE B: CASCADE THROUGH PRE-FILTER PROCESSING BLOCKS
        # ---------------------------------------------------------------------
        if m_cm_sub:
            sq_port = 3 if src_module == m_vco else current_port
            pm.add_cable(src_module['id'], sq_port, m_cm_sub['id'], 0, "#ff5500")
            current_id, current_port = m_cm_sub['id'], 0

        if m_cm_freq_div:
            pm.add_cable(current_id, current_port, m_cm_freq_div['id'], 0, "#f3374b")
            current_id, current_port = m_cm_freq_div['id'], 0

        if m_cm_mangler:
            pm.add_cable(current_id, current_port, m_cm_mangler['id'], 0, "#8b4ade")
            current_id, current_port = m_cm_mangler['id'], 0

        if m_cm_gate_comp:
            pm.add_cable(current_id, current_port, m_cm_gate_comp['id'], 1, "#ff5500")
            current_id, current_port = m_cm_gate_comp['id'], 0

        active_out_switch = m_cm_switch1_8 if m_cm_switch1_8 else m_cm_switch1_16
        if active_out_switch:
            pm.add_cable(current_id, current_port, active_out_switch['id'], 4, "#f3374b")
            current_id, current_port = active_out_switch['id'], 0 

        active_in_switch = m_cm_switch8_1 if m_cm_switch8_1 else m_cm_switch16_1
        if active_in_switch:
            pm.add_cable(current_id, current_port, active_in_switch['id'], 0, "#f3374b")
            current_id, current_port = active_in_switch['id'], 0 

        # ---------------------------------------------------------------------
        # 🧪 PHASE C: ROUTE AUDIO TIMBRE INTO FILTERS & FIX EMPTY OUTS
        # ---------------------------------------------------------------------
        if m_vcf and len(m_vcf) > 0:
            # 🚀 FIX: Take the first found filter from the row array [0]
            target_filter_mod = m_vcf[0] 
            
            pm.add_cable(current_id, current_port, target_filter_mod['id'], 3, "#f3374b")
            current_id, current_port = target_filter_mod['id'], 4
            
            if m_vco and m_vco2 and src_module == m_vco:
                pm.add_cable(m_vco2['id'], 6, target_filter_mod['id'], 0, "#ffb437")
                
            # Strict LFO fix we added last time:
            if m_lfo:
                pm.add_cable(m_lfo['id'], 0, target_filter_mod['id'], 1, "#3695ef") # LFO SIN -> VCF FREQ

        # ---------------------------------------------------------------------
        # 🧪 PHASE D: CASCADE THROUGH POST-FILTER MODIFIERS AND VCA TARGETS
        # ---------------------------------------------------------------------
        if m_cm_morph:
            pm.add_cable(current_id, current_port, m_cm_morph['id'], 0, "#ff00ff")
            current_id, current_port = m_cm_morph['id'], 0

        active_scaler = m_cm_scaler if m_cm_scaler else (m_cm_att if m_cm_att else None)
        if active_scaler:
            pm.add_cable(current_id, current_port, active_scaler['id'], 0, "#3695ef")
            current_id, current_port = active_scaler['id'], 0

        if m_cm_rect:
            pm.add_cable(current_id, current_port, m_cm_rect['id'], 0, "#8b4ade")
            current_id, current_port = m_cm_rect['id'], 0

        if m_delay:
            pm.add_cable(current_id, current_port, m_delay['id'], 0, "#ffb437")
            current_id, current_port = m_delay['id'], 0

        active_volume_mod = m_cm_mute if m_cm_mute else (m_cm_fade if m_cm_fade else None)
        if active_volume_mod:
            pm.add_cable(current_id, current_port, active_volume_mod['id'], 0, "#00b56e") 
            current_id, current_port = active_volume_mod['id'], 0 

        if m_vca:
            pm.add_cable(current_id, current_port, m_vca['id'], 1, "#f3374b")

        if m_vca and not has_global_master and m_global_io:
            pm.add_cable(m_vca['id'], 2, m_global_io['id'], 0, "#3695ef")
            pm.add_cable(m_vca['id'], 2, m_global_io['id'], 1, "#3695ef")

    # =========================================================================
    # 🌟 STEP 3: STUDIO RECORDING CONSOLE MATRIX MIX
    # =========================================================================
    if m_master_mixer and m_master_comp and m_master_verb and m_master_dist:
        for m in clean_chain:
            if m.get('meta_type') in ['VCA', 'VCA-1', 'VCA-2']:
                row = module_rows.get(m['id'], 0)
                if 0 <= row <= 4:
                    target_input_port = 4 + row
                    colors = ["#8b4ade", "#f3374b", "#ffb437", "#5555ff", "#00b56e"]
                    pm.add_cable(m['id'], 0, m_master_mixer['id'], target_input_port, colors[row])
        
        pm.add_cable(m_master_mixer['id'], 16, m_master_comp['id'], 0, "#8b4ade")
        pm.add_cable(m_master_mixer['id'], 17, m_master_comp['id'], 1, "#f3374b")
        pm.add_cable(m_master_comp['id'], 0, m_master_verb['id'], 0, "#8b4ade")
        pm.add_cable(m_master_comp['id'], 1, m_master_verb['id'], 1, "#ffb437")
        pm.add_cable(m_master_verb['id'], 4, m_master_dist['id'], 0, "#00b56e")
        pm.add_cable(m_master_verb['id'], 5, m_master_dist['id'], 1, "#3695ef")
        
        if m_global_io:
            pm.add_cable(m_master_dist['id'], 0, m_global_io['id'], 0, "#ffb437")
            pm.add_cable(m_master_dist['id'], 1, m_global_io['id'], 1, "#00b56e")
        
        print("  🔊 [AI Studio Matrix v38.0]: Cables hard-routed from VCA Port 0 to rexmix Ports 4-8!")

    # =========================================================================
    # 🪐 WAVE 4: ALGORITHMIC PORT STACKING (CLEAN DEFAULT v2)
    # =========================================================================
    print("  🎛️  Injecting programmatic multi-cable intra-block stacking (Target: 55%)...")
    
    floor_buckets = {r: [] for r in range(5)}
    for m in clean_chain:
        r_idx = module_rows.get(m['id'], -1)
        if r_idx in floor_buckets:
            floor_buckets[r_idx].append(m)

    colors_palette = ["#f3374b", "#ffb437", "#00b56e", "#3695ef", "#8b4ade"]

    for r_idx, floor_modules in floor_buckets.items():
        if not floor_modules: 
            continue

        outputs_pool = {
            "CV": [],
            "CLOCK": []
        }
        local_inputs = []
        
        for m in floor_modules:
            m_type = m.get('meta_type', '')
            m_id = m['id']
            
            if any(x in m_type for x in ["MATRIX", "SWITCH", "MULTIPLE", "LOGIC", "COMBINER", "SEQUENCER", "SEQ"]):
                continue
                
            # --- VCO / VCO2 / WTVCO ---
            if "VCO" in m_type:
                # Input 0 (V/OCT) FULLY DISABLED for cold-start protection
                local_inputs.append((m_id, 1, "CV")) # FM
                local_inputs.append((m_id, 2, "CV")) # PWM
                local_inputs.append((m_id, 3, "CLOCK")) # SYNC
                out_count = 8 if "VCO2" in m_type else 4
                for p in range(out_count):
                    outputs_pool["CV"].append((m_id, p))
                    
            # --- VCF / FILTER ---
            elif "VCF" in m_type or "FILTER" in m_type:
                local_inputs.append((m_id, 1, "CV"))    # FREQ
                local_inputs.append((m_id, 2, "CV"))    # RES
                local_inputs.append((m_id, 3, "CV"))    # DRIVE
                outputs_pool["CV"].append((m_id, 4))    # LPF Out
                outputs_pool["CV"].append((m_id, 5))    # HPF Out
                
            # --- CLOCKED / TIMERS ---
            elif "CLOCK" in m_type:
                for p in range(4): 
                    local_inputs.append((m_id, p, "CLOCK"))
                for p in range(4): 
                    outputs_pool["CLOCK"].append((m_id, p))
                    
            # --- LFO ---
            elif "LFO" in m_type:
                for p in range(2): 
                    local_inputs.append((m_id, p, "CV"))
                for p in range(4): 
                    outputs_pool["CV"].append((m_id, p))
                    
            # --- VCA ---
            elif "VCA" in m_type:
                local_inputs.append((m_id, 0, "CLOCK")) # GATE
                outputs_pool["CV"].append((m_id, 0)) # OUT
                
        if not outputs_pool["CV"] and not outputs_pool["CLOCK"]:
            continue
            
        for in_mod_id, in_port_id, sig_type in local_inputs:
            if random.random() < 0.55:
                compatible_outputs = outputs_pool.get(sig_type, [])
                if compatible_outputs:
                    out_mod_id, out_port_id = random.choice(compatible_outputs)
                    if out_mod_id == in_mod_id:
                        continue
                    pm.add_cable(
                        out_mod_id,
                        out_port_id,
                        in_mod_id,
                        in_port_id,
                        random.choice(colors_palette)
                    )