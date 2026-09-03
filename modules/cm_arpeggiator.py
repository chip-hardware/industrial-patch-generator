class CmArpeggiatorModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_ARPEGGIATOR"
        self.plugin = "CountModula"
        self.model = "SuperArpeggiator" # ➔ Valid binary slug
        self.version = "2.5.0"
        self.width = 12

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_request(self.id, "V_OCT", 1, "Poly CV In")
        broker.register_offer(self.id, "V_OCT", 4, "Mono CV Out") # ➔ Port 4 fix
        broker.register_offer(self.id, "GATE", 5, "Gate Out")     # ➔ Port 5 fix