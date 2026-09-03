#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class EightvertModule:
    """Micro-script for native VCV 8vert module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "8VERT"

    def register_signals(self, broker, clean_chain):
        # Register the first attenuator channel
        broker.register_request(self.id, "CV_FREQ", 0, "In 1")
        broker.register_offer(self.id, "CV_FREQ", 0, "Out 1")