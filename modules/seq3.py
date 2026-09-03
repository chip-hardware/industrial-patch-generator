#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

class Seq3Module:
    """
    Micro-script for native Fundamental SEQ3 module.
    v14.5: Added ROW C output (Port 11) for step-by-step microtonal dirt automation.
    """
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "SEQ3"

    def register_signals(self, broker, clean_chain):
        # 1. INPUTS (REQUESTS)
        broker.register_request(self.id, "CLOCK", 0, "Ext Clock In")
        broker.register_request(self.id, "CV_STEPS", 1, "Steps CV Input")

        # 2. OUTPUTS (OFFERS)
        broker.register_offer(self.id, "GATE", 12, "Gate Out")
        broker.register_offer(self.id, "V_OCT", 9, "Row A Out (Notes)")
        broker.register_offer(self.id, "CV_RES", 10, "Row B Out (Filter Resonance)")
        
        # NEW v14.5 ENHANCEMENT: Register ROW C (Port 11) for microtonal glitches!
        broker.register_offer(self.id, "CV_FINE", 11, "Row C Out (Microtonal Dirt)")

    def process_advanced_sync(self, clean_chain, port_manager):
        """Modulate STEPS length from Random or LFO on the floor"""
        modulator_id = None
        modulator_port = 0
        mod_type = ""

        for m in clean_chain:
            match = re.search(r'\d+', m.get('text', ''))
            m_row = int(match.group()) - 1 if match else 0
            
            if m_row == self.row:
                if m['meta_type'] in ['RANDOMVALUES', 'RANDOM', 'S&H']:
                    modulator_id = m['id']
                    modulator_port = 1
                    mod_type = "RandomValues"
                    break
                elif m['meta_type'] in ['LFO', 'LFO2', 'WTLFO'] and not modulator_id:
                    modulator_id = m['id']
                    modulator_port = 0
                    mod_type = m['meta_type']

        if modulator_id:
            port_manager.add_cable(modulator_id, modulator_port, self.id, 1, "#3695ef")

class SEQ3Module(Seq3Module): pass