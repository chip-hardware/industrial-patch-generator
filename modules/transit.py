class TransitModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "TRANSIT"
    def register_signals(self, broker, clean_chain): pass