class CmChancesModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_CHANCES"
        self.plugin = "CountModula"
        self.model = "Chances"           # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 6

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "GATE", 0, "Input Gate")
        broker.register_request(self.id, "GATE", 1, "Chance CV")     # ➔ Valid GATE tag
        broker.register_offer(self.id, "GATE", 2, "Output A")         # ➔ Port 2 fix
        broker.register_offer(self.id, "GATE", 3, "Output B")         # ➔ Port 3 fix