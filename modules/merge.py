#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MergeModule:
    """Micro-script for native VCV Merge module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "MERGE"

    def register_signals(self, broker, clean_chain):
        # Takes mono audio on IN 1 (Port 0)
        broker.register_request(self.id, "AUDIO", 0, "Mono In 1")
        # Outputs summed POLY OUT (Port 0)
        broker.register_offer(self.id, "POLY_AUDIO", 0, "Poly Out")