#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MutesModule:
    """Micro-script for native VCV Mutes module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "MUTES"

    def register_signals(self, broker, clean_chain):
        # Blindly passes audio or CV through channel 1
        broker.register_request(self.id, "AUDIO", 0, "In 1")
        broker.register_offer(self.id, "AUDIO", 0, "Out 1")