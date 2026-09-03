class CmGatemodifierModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_GATE_MODIFIER"
        self.plugin = "CountModula"
        self.model = "GateModifier"       # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "GATE", 0, "Trigger In")
        broker.register_offer(self.id, "GATE", 2, "Modified Length Out")  # ➔ Port 2 fix