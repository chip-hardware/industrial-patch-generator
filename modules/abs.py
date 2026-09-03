#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class AbsModule:
    """Micro-script for native VCV Abs (Rectifier) module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "ABS"

    def register_signals(self, broker, clean_chain):
        # Takes raw oscillator sound waves on Port 0
        broker.register_request(self.id, "AUDIO", 0, "Wave In")
        # Outputs rectified dirty overdrive from OUT (Port 0)
        broker.register_offer(self.id, "AUDIO", 0, "Rectified Out")