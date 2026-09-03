#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class QuantModule:
    """Micro-script for quantizer synonyms (Slug: QUANT)"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "QUANT"

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "V_OCT", 0, "CV Note In")
        broker.register_offer(self.id, "V_OCT", 0, "Quantized V/OCT Out")