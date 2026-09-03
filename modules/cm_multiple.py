#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class CmMultipleModule:
    """Micro-script for Count Modula Multiple splitter module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "CM_MULTIPLE"
        
        # 🚀 STRICT SYSTEM FIX: Exact runtime parameters per VCV Library requirements
        self.plugin = "CountModula"
        self.model = "Multiple"       # ➔ Clean legitimate name (no MkII or other suffixes!)
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        # 🪐 INPUT: Signal (Audio or CV) enters strictly through Socket 0
        broker.register_request(self.id, "AUDIO", 0, "Input Multi")
        
        # 🪐 OUTPUTS: Signal copies are taken from parallel sockets 1, 2, 3...
        broker.register_offer(self.id, "AUDIO", 1, "Parallel Out 1")
        broker.register_offer(self.id, "AUDIO", 2, "Parallel Out 2")
        broker.register_offer(self.id, "AUDIO", 3, "Parallel Out 3")