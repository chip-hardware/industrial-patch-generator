class PolymergeModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "POLY-MERGE"
    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 1, "Ch 1 In")
        broker.register_offer(self.id, "POLY_AUDIO", 0, "Poly Out")