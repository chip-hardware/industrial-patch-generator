#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BlankModule:
    """Safety micro-script for native VCV Blank panel"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "BLANK"

    def register_signals(self, broker, clean_chain):
        # Passive placeholder, offers nothing and requires nothing
        pass