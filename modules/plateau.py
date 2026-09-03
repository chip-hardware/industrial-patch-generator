#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PlateauModule:
    """Micro-script for Valley Plateau Reverb spatial module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "PLATEAU"

    def register_signals(self, broker, clean_chain):
        # 1. REQUESTS: expects audio on INPUT L (Port 0)
        broker.register_request(self.id, "AUDIO", 0, "In L")
        # Expects modulation for space automation on CV SIZE (Port 4)
        broker.register_request(self.id, "CV_FREQ", 4, "CV Size In")

        # 2. OFFERS: outputs stereo reverb tail from OUT L (Port 0)
        broker.register_offer(self.id, "AUDIO", 0, "Out L")