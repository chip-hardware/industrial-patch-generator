#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Audiointerface2Module:
    """Micro-script for extended Core Audio Interface 2 system module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "AUDIO2"

    def register_signals(self, broker, clean_chain):
        # Requires left and right channels for final rack mixdown
        broker.register_request(self.id, "AUDIO", 0, "To Device CH1")
        broker.register_request(self.id, "AUDIO_RIGHT", 1, "To Device CH2")