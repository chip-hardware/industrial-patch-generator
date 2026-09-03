class CmSlopedetectorModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_SLOPE_DETECTOR"
        self.plugin = "CountModula"
        self.model = "SlopeDetector"
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "CV In")
        broker.register_offer(self.id, "GATE", 1, "Is Rising Out")   # ➔ Port 1 fix
        broker.register_offer(self.id, "GATE", 2, "Is Falling Out")  # ➔ Port 2 fix