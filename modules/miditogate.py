class MiditogateModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "MIDI-GATE"
    def register_signals(self, broker, clean_chain):
        broker.register_offer(self.id, "GATE", 0, "Gate 1 Out")