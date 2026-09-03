#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class VCAModule:
    """Micro-script for native Fundamental VCA-1 module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "VCA"

    def register_signals(self, broker, clean_chain):
        # 1. INPUT REGISTRATION (REQUESTS)
        # Port 1 = Main audio input (expects signal after VCF or effects)
        broker.register_request(self.id, "AUDIO", 1, "Audio In")
        # Port 0 = CV amplitude control input (expects Gate from SEQ3 or MIDI-CV)
        broker.register_request(self.id, "GATE", 0, "CV Amplitude In")

        # 2. OUTPUT REGISTRATION (OFFERS)
        # Port 2 = Final output of processed audio signal for the floor
        broker.register_offer(self.id, "AUDIO", 2, "VCA Audio Out")