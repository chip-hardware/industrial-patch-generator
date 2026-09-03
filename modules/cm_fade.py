class CmFadeModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_FADE"
        self.plugin = "CountModula"
        self.model = "Fade"               # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "Audio L In")
        broker.register_request(self.id, "GATE", 4, "Ctrl In")     # ➔ Port 4 fix
        broker.register_offer(self.id, "AUDIO", 2, "Audio L Out")   # ➔ Port 2 fix