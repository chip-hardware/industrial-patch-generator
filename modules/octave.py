#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class OctaveModule:
    """Micro-script for native VCV Octave module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "OCTAVE"

    def register_signals(self, broker, clean_chain):
        # 1. REQUESTS: takes volt-octave notes from sequencer into IN (Port 0)
        broker.register_request(self.id, "V_OCT", 0, "V/OCT Note In")
        
        # 2. OFFERS: outputs shifted voltage from OUT (Port 0) to oscillators
        broker.register_offer(self.id, "V_OCT", 0, "Shifted V/OCT Out")