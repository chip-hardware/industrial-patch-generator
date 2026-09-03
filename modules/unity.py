#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class UnityModule:
    """Micro-script for native VCV Unity module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "UNITY"

    def register_signals(self, broker, clean_chain):
        # Takes CV signals or gates on Input 1 (0) and Input 2 (1)
        broker.register_request(self.id, "GATE", 0, "Gate In 1")
        broker.register_request(self.id, "CV_FREQ", 1, "CV In 2")
        # Immediately outputs the sum from OUT (Port 0)
        broker.register_offer(self.id, "GATE", 0, "Sum Out")