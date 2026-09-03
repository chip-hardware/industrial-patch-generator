#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SwitchesModule:
    """Micro-script for native VCV Sequential Switch module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "SWITCHES"

    def register_signals(self, broker, clean_chain):
        # Requires clock for step switching on CLK input (Port 0)
        broker.register_request(self.id, "CLOCK", 0, "Switch Clock In")
        # Takes main audio path on common COM socket (Port 1)
        broker.register_request(self.id, "AUDIO", 1, "Common I/O")
        
        # Outputs switched step from Output 1 (Port 2)
        broker.register_offer(self.id, "AUDIO", 2, "Channel 1 Out")