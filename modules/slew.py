#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SlewModule:
    """Micro-script for native VCV Slew Limiter module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "SLEW"

    def register_signals(self, broker, clean_chain):
        # Takes volt-octave notes from quantizer on IN (Port 0)
        broker.register_request(self.id, "V_OCT", 0, "CV In")
        # Outputs smoothed glide (Portamento) from OUT (Port 0)
        broker.register_offer(self.id, "V_OCT", 0, "CV Out (Glide)")