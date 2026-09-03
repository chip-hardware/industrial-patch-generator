#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NoiseModule:
    """Micro-script for native Fundamental Noise module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "NOISE"

    def register_signals(self, broker, clean_chain):
        # Port 0 = White Noise output (for filtering or Noise FM)
        broker.register_offer(self.id, "AUDIO", 0, "White Noise Out")