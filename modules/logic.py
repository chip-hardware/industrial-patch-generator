#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class LogicModule:
    """Micro-script for native VCV Logic module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "LOGIC"

    def register_signals(self, broker, clean_chain):
        # 1. REQUESTS: receives Gate A (Port 0) and Gate B (Port 1)
        broker.register_request(self.id, "GATE", 0, "Gate Input A")
        
        # 2. OFFERS: offers generated broken gates (take XOR output for live techno bounce)
        broker.register_offer(self.id, "GATE_LOGIC", 6, "XOR Out")