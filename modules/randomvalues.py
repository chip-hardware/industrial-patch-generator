#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class RandomvaluesModule:
    """Unified micro-script for native VCV Random Values module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "RANDOMVALUES"

    def register_signals(self, broker, clean_chain):
        # Requires clock pulse on TRIG input (Port 0)
        broker.register_request(self.id, "CLOCK", 0, "Trig In")

        # Offers random CV voltage outputs (Channel 1, port 0 & Channel 2, port 1)
        broker.register_offer(self.id, "V_OCT", 0, "Rand CV 1 Out")
        broker.register_offer(self.id, "CV_FREQ", 1, "Rand CV 2 Out")

# Duplicate class in uppercase for 100% compatibility with pipeline auto-parser
class RANDOMVALUESModule(RandomvaluesModule):
    pass