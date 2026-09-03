#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SplitModule:
    """Micro-script for native VCV Split module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "SPLIT"

    def register_signals(self, broker, clean_chain):
        # Accepts summed poly cable on POLY IN (Port 0)
        broker.register_request(self.id, "POLY_AUDIO", 0, "Poly In")
        # Outputs first decoded mono channel from OUT 1 (Port 0)
        broker.register_offer(self.id, "AUDIO", 0, "Mono Out 1")