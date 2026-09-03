#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ReverbModule:
    """Micro-script for native Fundamental Reverb module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "REVERB"

    def register_signals(self, broker, clean_chain):
        # Accepts audio path on IN (Port 0)
        broker.register_request(self.id, "AUDIO", 0, "Audio In")
        # Outputs spatial signal from OUT L (Port 0)
        broker.register_offer(self.id, "AUDIO", 0, "Audio Out L")