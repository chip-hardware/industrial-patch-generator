class CmG2tModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_G2T"
        self.plugin = "CountModula"
        self.model = "G2T"                # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "GATE", 0, "Gate In")
        broker.register_offer(self.id, "CLOCK", 1, "Trigger Out") # ➔ Port 1 fix