#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class VCOModule:
    """Micro-script for native Fundamental VCO module"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "VCO"

    def register_signals(self, broker, clean_chain):
        # 1. OUTPUT REGISTRATION (OFFERS)
        # Port 0 = Triangle (perfect for FM)
        broker.register_offer(self.id, "AUDIO_FM", 0, "Triangle Out")
        # Port 1 = Saw (classic industrial meat)
        broker.register_offer(self.id, "AUDIO", 1, "Saw Out")
        # Port 3 = Square (overdrive for filters)
        broker.register_offer(self.id, "AUDIO_SQR", 3, "Square Out")

        # 2. INPUT REGISTRATION (REQUESTS)
        # Port 2 = V/OCT input (expects melody or random)
        broker.register_request(self.id, "V_OCT", 2, "V/OCT In")
        # Port 1 = Linear FM input (expects triangle from adjacent VCO or Noise)
        broker.register_request(self.id, "LINEAR_FM", 1, "Linear FM In")

    def process_advanced_sync(self, clean_chain, port_manager):
        """Custom Hard Sync logic: if another VCO is to the left, lock phase to it"""
        for i, m in enumerate(clean_chain):
            if m['id'] == self.id and i > 0:
                prev_mod = clean_chain[i - 1]
                if prev_mod['meta_type'] in ['VCO', 'VCO2', 'WTVCO']:
                    # Take Saw (1) from previous VCO and feed into SYNC input (0) of current
                    port_manager.add_cable(prev_mod['id'], 1, self.id, 0, "#ff00ff")
                    print(f"    ⚙️  OOP Sync Engine: {prev_mod['meta_type']} ➔ {self.type} (Hard Sync)")