#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SandhModule:
    """Micro-script for native Fundamental Sample & Hold module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "S&H"

    def register_signals(self, broker, clean_chain):
        # Requires clock pulse for step capture on TRIG input (Port 1)
        broker.register_request(self.id, "CLOCK", 1, "Trig In")
        # Takes raw noise or wave source on IN input (Port 0)
        broker.register_request(self.id, "AUDIO_FM", 0, "Signal In")
        
        # Offers random stepped notes from OUT (Port 0)
        broker.register_offer(self.id, "V_OCT", 0, "S&H Out")