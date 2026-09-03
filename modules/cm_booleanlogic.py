#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class CmBooleanlogicModule:
    """Micro-script for Count Modula Polyphonic Boolean Logic Processor"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "CM_LOGIC"
        
        # 🚀 STRICT SYSTEM FIX: Exact binary slugs for VCV Rack 2.6+
        self.plugin = "CountModula"
        self.model = "PolyphonicLogic"   # ➔ The only legitimate technical model name!
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        # 🪐 INPUT MAP (Native logic ports)
        broker.register_request(self.id, "GATE", 0, "Input A")
        broker.register_request(self.id, "CLOCK", 1, "Input B")
        
        # 🪐 OUTPUT MAP (Collision routing for port 0)
        # Port 2 - AND, Port 3 - OR, Port 4 - XOR, Port 5 - NAND, Port 6 - NOR, Port 7 - XNOR
        # Since your concept requires OR, we take the signal from legitimate Port 3!
        broker.register_offer(self.id, "GATE", 3, "Logic OR Out")