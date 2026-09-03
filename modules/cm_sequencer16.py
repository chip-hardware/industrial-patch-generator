class CmSequencer16Module:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_SEQUENCER_16"
        self.plugin = "CountModula"
        self.model = "Sequencer16"
        self.version = "2.5.0"
        self.width = 28

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_request(self.id, "GATE", 1, "Reset In")
        broker.register_offer(self.id, "V_OCT", 2, "CV Out")     # ➔ Port 2 fix