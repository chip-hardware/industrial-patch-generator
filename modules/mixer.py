#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MixerModule:
    """Micro-script v10.0 for native VCV Mix module (4-channel stereo hub)"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "MIXER"

    def register_signals(self, broker, clean_chain):
        # Register 4 independent input channels for parallel mixing (Wet/Dry)
        broker.register_request(self.id, "AUDIO_DRY", 0, "CH1 In (Clean Filter)")
        broker.register_request(self.id, "AUDIO_WET", 1, "CH2 In (Delay FX Echo)")
        broker.register_request(self.id, "AUDIO_SUB", 2, "CH3 In (Sub Oscillator)")
        broker.register_request(self.id, "AUDIO_NOISE", 3, "CH4 In (Noise Texture)")

        # Main summed master output MIX (Port 4)
        broker.register_offer(self.id, "AUDIO_MASTER", 4, "Master Mix Out")

class MIXERModule(MixerModule): pass