#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ScopeModule:
    """Micro-script for native VCV Scope module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "SCOPE"

    def register_signals(self, broker, clean_chain):
        # 1. REQUESTS: ready to accept audio or CV on X Input (0) and Y Input (2)
        broker.register_request(self.id, "AUDIO", 0, "X Input")
        broker.register_request(self.id, "CV_FREQ", 2, "Y Input")
        # Accepts clock for sweep sync on EXT TIME (4)
        broker.register_request(self.id, "CLOCK", 4, "Ext Time In")