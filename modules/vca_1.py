#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Vca1Module:
    """Micro-script for native Fundamental VCA-1 module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "VCA-1"

    def register_signals(self, broker, clean_chain):
        # Fully duplicates the base VCA class hardware logic
        broker.register_request(self.id, "AUDIO", 1, "Audio In")
        broker.register_request(self.id, "GATE", 0, "CV Amplitude In")
        broker.register_offer(self.id, "AUDIO", 2, "VCA Audio Out")