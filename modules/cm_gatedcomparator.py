class CmGatedcomparatorModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_GATED_COMPARATOR"
        self.plugin = "CountModula"
        self.model = "GatedComparator"    # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_request(self.id, "AUDIO", 1, "Signal In 1")
        broker.register_offer(self.id, "GATE", 3, "Comparator Out")      # ➔ Signal type fix and port 3