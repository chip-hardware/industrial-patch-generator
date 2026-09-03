class CmGateSeq8Module:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_GATE_SEQ_8"
        self.plugin = "CountModula"
        self.model = "GateSequencer8MkII" # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 18

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_request(self.id, "GATE", 1, "Reset In")
        broker.register_offer(self.id, "GATE", 2, "Ch 1 Gate Out")         # ➔ Port 2 fix
        broker.register_offer(self.id, "CLOCK", 10, "Ch 1 Trigger Out")   # ➔ Port 10 fix