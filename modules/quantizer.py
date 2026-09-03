#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class QuantizerModule:
    """Micro-script for native Fundamental Quantizer module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "QUANTIZER"

    def register_signals(self, broker, clean_chain):
        # Requires raw step CV voltages on IN input (Port 0)
        broker.register_request(self.id, "V_OCT", 0, "CV Note In")
        # Offers crystal-clear tonal output on OUT (Port 0)
        broker.register_offer(self.id, "V_OCT", 0, "Quantized V/OCT Out")