class CmVcpulsedividerModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_VC_PULSE_DIVIDER"
        self.plugin = "CountModula"
        self.model = "VCPulseDivider"
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_offer(self.id, "CLOCK", 2, "Divided Out 1") # ➔ Port 2 fix