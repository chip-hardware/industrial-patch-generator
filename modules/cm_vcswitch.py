class CmVcswitchModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_VC_SWITCH"
        self.plugin = "CountModula"
        self.model = "VCSwitch"
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "GATE", 0, "CV Control In")  # ➔ Valid GATE tag
        broker.register_request(self.id, "AUDIO", 1, "Signal In")
        broker.register_offer(self.id, "AUDIO", 2, "Output A")       # ➔ Port 2 fix