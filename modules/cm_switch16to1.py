class CmSwitch16to1Module:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_SWITCH_16_1"
        self.plugin = "CountModula"
        self.model = "Switch16To1"
        self.version = "2.5.0"
        self.width = 6

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_request(self.id, "AUDIO", 2, "Input 1")       # ➔ Port 2 fix
        broker.register_offer(self.id, "AUDIO", 18, "Main Output")    # ➔ Port 18 fix