class MiditoccModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "MIDI-CC"
    def register_signals(self, broker, clean_chain):
        broker.register_offer(self.id, "CV_FREQ", 0, "CC 1 Out")