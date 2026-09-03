#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class VcmixerModule:
    """Micro-script for native VCV VCMixer (4-channel mixer) module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "VCMIXER"
        
        # 🚀 SOLID SYSTEM FIX FOR YOUR SETTINGS.JSON:
        self.plugin = "Fundamental"
        self.model = "VCMixer"         # ➔ Exact official name from your whitelist!
        self.version = "2.6.4"
        self.width = 17

    def register_signals(self, broker, clean_chain):
        # 🪐 INPUT MAP (4 physical channels per Fundamental manual)
        # Channel 1: Audio = Port 2, CV = Port 6
        broker.register_request(self.id, "AUDIO", 2, "CH1 In")
        broker.register_request(self.id, "GATE", 6, "CH1 CV In")
        
        # Channel 2: Audio = Port 3, CV = Port 7
        broker.register_request(self.id, "AUDIO", 3, "CH2 In")
        broker.register_request(self.id, "GATE", 7, "CH2 CV In")
        
        # 🪐 OUTPUT MAP (MIX socket at the bottom)
        # Legitimate summed master mix output is strictly Port 1
        broker.register_offer(self.id, "AUDIO", 1, "Master Mix Out")