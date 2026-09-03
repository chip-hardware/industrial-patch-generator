class CvtogateModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CV-GATE"
    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "GATE", 0, "Gate In")