class Vco3Module:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "VCO3"
    def register_signals(self, broker, clean_chain):
        broker.register_offer(self.id, "AUDIO", 1, "Saw Out")
        broker.register_request(self.id, "V_OCT", 0, "V/OCT In")