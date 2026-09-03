class CmGateSequencer16Module:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_GATE_SEQUENCER_16"
        self.plugin = "CountModula"
        self.model = "GateSequencer16MkII" # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 30

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_offer(self.id, "GATE", 2, "Gate Out")             # ➔ Port 2 fix