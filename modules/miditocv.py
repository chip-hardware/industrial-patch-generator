#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MiditocvModule:
    """Micro-script for Core MIDI to CV system module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "MIDI-CV"

    def register_signals(self, broker, clean_chain):
        # 1. OFFERS: offers precise external notes from V/OCT port (0)
        broker.register_offer(self.id, "V_OCT", 0, "V/OCT Note Out")
        # Offers key gate pulse from GATE port (1)
        broker.register_offer(self.id, "GATE", 1, "Gate Out")

# CLASS DUPLICATION FOR 100% CASE-INSENSITIVE PROTECTION IN PIPELINE.PY
class MIDIToCVModule(MiditocvModule): pass
class MiditocvModule_Upper(MiditocvModule): pass