class CmManualcvModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_MANUAL_CV"
        self.plugin = "CountModula"
        self.model = "ManualCV"           # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        # Switch to valid V_OCT tag for Pitch bus compatibility
        broker.register_offer(self.id, "V_OCT", 0, "Out 1")