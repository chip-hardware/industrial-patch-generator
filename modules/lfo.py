#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class LFOModule:
    """Micro-script for native Fundamental LFO module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "LFO"

    def register_signals(self, broker, clean_chain):
        # Register the first wave output Sine (Port 0) for filter cutoff modulation
        broker.register_offer(self.id, "CV_FREQ", 0, "Sine Out")