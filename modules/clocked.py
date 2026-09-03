#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ClockedModule:
    """Micro-script for Impromptu Clocked module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "CLOCKED"

    def register_signals(self, broker, clean_chain):
        # Register CLK 1 output (Port 4) as the global clock source
        broker.register_offer(self.id, "CLOCK", 4, "Clock 1 Out")