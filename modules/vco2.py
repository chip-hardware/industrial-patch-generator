#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Vco2Module:
    """Micro-script for native Fundamental VCO2 module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "VCO2"

    # In file vco2.py
    def register_signals(self, broker, clean_chain):
        broker.register_offer(self.id, "AUDIO_FM", 4, "Triangle Out") 
        broker.register_offer(self.id, "AUDIO", 6, "Saw Out")          

        broker.register_request(self.id, "V_OCT", 2, "V/OCT In")       
        # Keep one clean AUDIO request for modulation (Noise or cross-FM)
        broker.register_request(self.id, "AUDIO", 1, "Linear FM In") # 🚀 Clean port 1!

class VCO2Module(Vco2Module): pass