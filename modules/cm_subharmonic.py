class CmSubharmonicModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_SUBHARMONIC"
        self.plugin = "CountModula"
        self.model = "SubHarmonicGenerator" # ➔ Legitimate technical slug
        self.version = "2.5.0"
        self.width = 7

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "Audio Input")
        broker.register_offer(self.id, "AUDIO", 1, "Sub Mix Out")          # ➔ Port 1 fix