#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class VCFModule:
    """Micro-script v10.0 for native Fundamental VCF module"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "VCF"

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 3, "Audio Input")
        broker.register_request(self.id, "CV_FREQ", 0, "CV Frequency In")
        broker.register_request(self.id, "CV_RES", 1, "CV Resonance In")

        # Register port 4 both as specific LPF and as general AUDIO for mixers/VCA
        broker.register_offer(self.id, "AUDIO_LPF", 4, "Low-Pass Out")
        broker.register_offer(self.id, "AUDIO", 4, "Low-Pass Audio Output") # 🚀 Fix!
        broker.register_offer(self.id, "AUDIO_HPF", 5, "High-Pass Out")

class VCFModule_Upper(VCFModule): pass