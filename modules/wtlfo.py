#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class WtlfoModule:
    """Micro-script for VCV Wavetable LFO module"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "WTLFO"

    def register_signals(self, broker, clean_chain):
        broker.register_offer(self.id, "CV_FREQ", 0, "Sine Out")
        broker.register_request(self.id, "CLOCK", 1, "Reset Phase In")