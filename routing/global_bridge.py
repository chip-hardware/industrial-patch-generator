#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def process_inter_block_intelligence(clean_chain, module_rows, pm):
    """
    Inter-Block Cross-Row Intelligence Matrix Engine v3.0.
    Handles structural multi-brand macro patched connections between isolated rows.
    Bridges clock networks, sequencers, matrices, and triggers across the layers.
    """
    # Group modules into structural rack layers
    # Layout Blueprint Map: 0 - DRONE, 1 - BASS, 2 - RHYTHM, 3 - NOISE, 4 - MELODIC
    blocks = {i: [m for m in clean_chain if module_rows.get(m['id']) == i] for i in range(5)}
    
    def get_module_by_type(row_idx, meta_type):
        """Helper matrix utility to scan a targeted row for an active hardware type."""
        return next((m for m in blocks[row_idx] if m['meta_type'] == meta_type), None)

    # Global hardware tracker hooks across rows
    global_plateau = next((m for m in clean_chain if m['meta_type'] == 'PLATEAU'), None)
    global_quant_id = next((m['id'] for m in clean_chain if m['meta_type'] in ['QUANT', 'QUANTIZER']), None)

    # =========================================================================
    # 🧠 INTER-BLOCK INTELLECTUAL MODULATION MATRIX
    # =========================================================================

    # --- 1. RHYTHM TEMPO INJECTION TO REVERB MATRIX (RHYTHM ➔ PLATEAU SPACE) ---
    rhythm_clock = get_module_by_type(2, 'CLOCKED')
    if rhythm_clock and global_plateau:
        # Clock Pulse Out 1 (Port 4) ➔ Plateau Space CV input (Port 4)
        # Result: Reverb tail dimensions contract and breath in sync with the master drums!
        pm.add_cable(rhythm_clock['id'], 4, global_plateau['id'], 4, "#8b4ade")

    # --- 2. MULTI-LAYER COMPACT TEXTURE SUB-FEEDBACK HABS (NOISE ➔ GLOBAL MIXERS) ---
    global_mixer = next((m for m in clean_chain if m['meta_type'] in ['MIXER', 'VCMIXER']), None)
    if global_mixer:
        # Pull direct raw white noise floor from row 3 as a baseline backdrop for a mixer in another lane
        noise_source = get_module_by_type(3, 'NOISE')
        if noise_source:
            # White Noise Out (Port 0) ➔ Channel 4 Audio Input (Port 3)
            pm.add_cable(noise_source['id'], 0, global_mixer['id'], 3, "#ff5500")

    # --- 3. COUNT MODULA ALGORITHMIC CLOCK MULTI-CROSSING (RHYTHM ➔ NOISE / MELODIC) ---
    # Intercept master clocks to sync isolated sequence structures or trigger gates on other rows
    cm_divider = get_module_by_type(2, 'CM_CLOCK_DIVIDER')
    if rhythm_clock and cm_divider:
        # Sync Clock Divider clock input directly to the master tempo hub
        pm.add_cable(rhythm_clock['id'], 4, cm_divider['id'], 0, "#8b4ade") # Master Clock Out -> Divider In

    # --- 4. STEP SEQUENCER CASCADE CROSS-PITCH ROUTING (MELODIC ➔ BASS / DRONE) ---
    # Intercept pitch lines from Melodic controllers to synchronize Bass oscillators 
    melodic_control = get_module_by_type(4, 'SEQ3') or get_module_by_type(4, 'CM_SEQUENCER_8') or get_module_by_type(4, 'CM_SEQUENCER_16')
    bass_vco = get_module_by_type(1, 'VCO') or get_module_by_type(1, 'VCO2')
    
    if melodic_control and bass_vco:
        # Determine correct Pitch Output port index based on module manufacturer specifications
        pitch_port = 0 if melodic_control['meta_type'].startswith("CM_") else 9 # CM Pitch Out is 0, SEQ3 is 9
        
        # If an explicit Quantizer is grouped anywhere on the row, clean the tracking first
        if global_quant_id:
            pm.add_cable(melodic_control['id'], pitch_port, global_quant_id, 0, "#00b56e") # Pitch -> Quant In
            pm.add_cable(global_quant_id, 2, bass_vco['id'], 2, "#00b56e") # Quantized Pitch -> Bass V/OCT
        else:
            pm.add_cable(melodic_control['id'], pitch_port, bass_vco['id'], 2, "#00b56e") # Direct V/OCT link

    # --- 5. AUTOMATED HARSH WAVE MUTATION INTEGRATION (DRONE / NOISE ➔ MATRIX MIXER) ---
    cm_matrix = next((m for m in clean_chain if m['meta_type'] == 'CM_MATRIX_MIXER'), None)
    if cm_matrix:
        drone_osc = get_module_by_type(0, 'VCO') or get_module_by_type(0, 'VCO2')
        noise_osc = get_module_by_type(3, 'NOISE')
        drone_vcf = get_module_by_type(0, 'VCF') or get_module_by_type(0, 'FILTER')
        
        # Matrix Inputs (Feed sources)
        if drone_osc:
            dr_port = 6 if drone_osc['meta_type'] == "VCO2" else 1
            pm.add_cable(drone_osc['id'], dr_port, cm_matrix['id'], 0, "#f3374b") # Drone -> Input A (0)
        if noise_osc:
            pm.add_cable(noise_osc['id'], 0, cm_matrix['id'], 1, "#ff5500") # Noise -> Input B (1)
            
        # Create a hellish loop: take Plateau Reverb output and return it to the matrix
        if global_plateau:
            pm.add_cable(global_plateau['id'], 4, cm_matrix['id'], 2, "#3695ef") # Reverb Out L -> Input C (2)

        # Matrix Outputs (Where to send the mix)
        if drone_vcf:
            # Mixer Output A (Port 0) goes to modulate the drone filter frequency cutoff
            pm.add_cable(cm_matrix['id'], 0, drone_vcf['id'], 1, "#ff00ff") 
            # Mixer Output B (Port 1) goes to the filter audio input for wild overdrive
            pm.add_cable(cm_matrix['id'], 1, drone_vcf['id'], 0, "#f3374b")

    # --- 6. RHYTHMIC CHANCE PROBABILITY OVERRIDES (RHYTHM ➔ SELECTION SWITCHES) ---
    # Drive sequential switches across lanes dynamically using rhythmic probability outputs
    cm_chances = get_module_by_type(2, 'CM_CHANCES')
    cm_switch_node = next((m for m in clean_chain if m['meta_type'] in ['CM_SWITCH_1_8', 'CM_SWITCH_1_16']), None)
    
    if cm_chances and cm_switch_node:
        # Route a random probability gate outcome straight into the switch trigger advance slot
        pm.add_cable(cm_chances['id'], 0, cm_switch_node['id'], 0, "#3695ef") # Chance A Gate Out -> Switch Trigger Up

    # --- 7. RECTIFIER DISTORTION GENERATIVE INTER-BLOCK INFUSIONS ---
    # Route row signals into high-gain pre-processors to smash spatial feedback lines before the master deck
    cm_rectifier = next((m for m in clean_chain if m['meta_type'] == 'CM_RECTIFIER'), None)
    if cm_rectifier and global_plateau:
        # Route rectified harmonic overtones into the Right channel input of the studio reverb strip
        pm.add_cable(cm_rectifier['id'], 0, global_plateau['id'], 1, "#ff5500") # Full Wave Out -> Plateau In R