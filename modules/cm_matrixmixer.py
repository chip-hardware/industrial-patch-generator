class CmMatrixmixerModule:
    """Micro-script for Count Modula Matrix Mixer 4x4"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_MATRIX_MIXER"
        self.plugin = "CountModula"
        self.model = "MatrixMixer"
        self.version = "2.5.0"
        self.width = 14

    def register_signals(self, broker, clean_chain):
        # 4 inputs (0-3)
        broker.register_request(self.id, "AUDIO", 0, "Matrix In 1")
        broker.register_request(self.id, "AUDIO", 1, "Matrix In 2")
        broker.register_request(self.id, "AUDIO", 2, "Matrix In 3")
        
        # 4 outputs (4-7) — collision resolved by offset from inputs!
        broker.register_offer(self.id, "AUDIO", 4, "Matrix Out 1")
        broker.register_offer(self.id, "AUDIO", 5, "Matrix Out 2")