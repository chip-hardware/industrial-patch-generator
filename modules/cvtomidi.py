class CvtomidiModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CV-MIDI"
    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "V_OCT", 0, "V/OCT In")