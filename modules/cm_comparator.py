class CmComparatorModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_COMPARATOR"
        self.plugin = "CountModula"
        self.model = "Comparator"         # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "Signal Input A")
        broker.register_offer(self.id, "GATE", 2, "Over Threshold Out") # ➔ Port 2 fix