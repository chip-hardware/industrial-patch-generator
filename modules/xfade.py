#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class XfadeModule:
    """Micro-script for native VCV Crossfader (Slug: XFADE)"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "XFADE"

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO_CH1", 0, "Input A")
        broker.register_request(self.id, "AUDIO_CH2", 1, "Input B")
        broker.register_request(self.id, "CV_FREQ", 2, "Mix CV In")
        broker.register_offer(self.id, "AUDIO", 0, "Output")