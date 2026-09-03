class CmMorphshaperModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_MORPH_SHAPER"
        self.plugin = "CountModula"
        self.model = "MorphShaper"
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "Signal Input")
        broker.register_request(self.id, "GATE", 1, "Morph CV In")
        broker.register_offer(self.id, "AUDIO", 2, "Morph Out A") # ➔ Port 2 fix and universal AUDIO tag