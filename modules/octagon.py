class OctagonModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "OCTAGON"
    def register_signals(self, broker, clean_chain):
        broker.register_offer(self.id, "CV_FREQ", 0, "Phase 1 Out")