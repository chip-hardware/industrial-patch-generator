#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class AudiointerfaceModule:
    """Micro-script for Core Audio Interface system module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "AUDIO"

    def register_signals(self, broker, clean_chain):
        # Requires left channel audio on Port 0 (To Device CH1) and right on Port 1 (To Device CH2)
        broker.register_request(self.id, "AUDIO", 0, "Left Out to Monitors")
        broker.register_request(self.id, "AUDIO_RIGHT", 1, "Right Out to Monitors")