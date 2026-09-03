class CmManualcv2Module:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_MANUAL_CV2"
        self.plugin = "CountModula"
        self.model = "ManualCV"
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_offer(self.id, "V_OCT", 0, "Out 1")