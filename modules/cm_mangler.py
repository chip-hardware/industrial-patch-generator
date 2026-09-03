class CmManglerModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_MANGLER"
        self.plugin = "CountModula"
        self.model = "Mangler"            # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "Signal In")
        broker.register_request(self.id, "GATE", 1, "Slice CV")           # ➔ Valid GATE tag
        broker.register_offer(self.id, "AUDIO", 2, "Crushed Out")         # ➔ Port 2 fix