class CmMatrixcombinerModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_MATRIX_COMBINER"
        self.plugin = "CountModula"
        self.model = "MatrixCombiner"
        self.version = "2.5.0"
        self.width = 10

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "GATE", 0, "Gate Input 1")
        broker.register_offer(self.id, "GATE", 8, "Combined Output 1") # ➔ Port 8 fix