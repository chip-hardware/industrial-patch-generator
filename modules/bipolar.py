#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BipolarModule:
    """Micro-script for native VCV Unipolar/Bipolar Converter module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "BIPOLAR"

    def register_signals(self, broker, clean_chain):
        # Receives raw CV modulation (e.g., from RandomValues)
        broker.register_request(self.id, "CV_FREQ", 0, "CV In")
        # Outputs balanced inverted signal from OUT port (Port 0)
        broker.register_offer(self.id, "CV_FREQ", 0, "Converted CV Out")