class CmAttenuverterModule:
    """Micro-script per manual for Count Modula Attenuverter"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_ATTENUVERTER"
        self.plugin = "CountModula"
        self.model = "Attenuverter"     # ➔ Valid binary slug
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        # Switch to legitimate V_OCT tags for sequencer compatibility
        broker.register_request(self.id, "V_OCT", 0, "Input CH1")
        broker.register_offer(self.id, "V_OCT", 1, "Output CH1")  # ➔ Output port 1 fix