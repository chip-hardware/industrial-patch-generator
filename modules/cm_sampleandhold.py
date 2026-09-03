class CmSampleandholdModule:
    """Micro-script per manual for Count Modula Sample & Hold"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_SAMPLE_AND_HOLD"
        self.plugin = "CountModula"
        self.model = "SampleAndHold"
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "Signal Input")
        broker.register_request(self.id, "CLOCK", 1, "Trigger Input")
        broker.register_offer(self.id, "V_OCT", 2, "S&H Output")  # ➔ Port 2 fix