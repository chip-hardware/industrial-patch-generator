class CmGatedelayModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_GATE_DELAY"
        self.plugin = "CountModula"
        self.model = "GateDelay"          # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 6

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "GATE", 0, "Gate In 1")
        broker.register_offer(self.id, "GATE", 1, "Delayed Gate Out 1")