class CmShepardgeneratorModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_SHEPARD_GENERATOR"
        self.plugin = "CountModula"
        self.model = "ShepardGenerator"
        self.version = "2.5.0"
        self.width = 8

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "GATE", 0, "Rate CV")
        broker.register_offer(self.id, "AUDIO", 1, "Ramp Out 1")  # ➔ Port 1 fix and AUDIO tag