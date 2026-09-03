#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Lfo2Module:
    """Micro-script for native Fundamental LFO2 module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "LFO2"

    def register_signals(self, broker, clean_chain):
        # Offers Sine output (Port 0) for modulations
        broker.register_offer(self.id, "CV_FREQ", 0, "Sine Out")
        # Requires clock pulse on RESET (Port 1) for phase stability
        broker.register_request(self.id, "CLOCK", 1, "Reset Phase In")