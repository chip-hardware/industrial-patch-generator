#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ResonatorModule:
    """Micro-script for native VCV Resonator module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "RESONATOR"

    def register_signals(self, broker, clean_chain):
        # Requires audio on IN (Port 0) and volt-octave notes on V/OCT (Port 1)
        broker.register_request(self.id, "AUDIO", 0, "Audio In")
        broker.register_request(self.id, "V_OCT", 1, "V/OCT Filter In")
        # Outputs formant screech from OUT (Port 0)
        broker.register_offer(self.id, "AUDIO", 0, "Resonated Audio Out")