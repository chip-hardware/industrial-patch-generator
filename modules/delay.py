#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class DelayModule:
    """Micro-script for native Fundamental Delay module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "DELAY"

    def register_signals(self, broker, clean_chain):
        # Requires audio signal on INPUT L (Port 0)
        broker.register_request(self.id, "AUDIO", 0, "Audio In L")
        # Offers processed effect signal from OUTPUT L (Port 0)
        broker.register_offer(self.id, "AUDIO", 0, "Audio Out L")