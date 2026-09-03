class CmSwitch1to8Module:
    """Micro-script per manual for Count Modula Switch 1->8"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_SWITCH_1_8"
        self.plugin = "CountModula"
        self.model = "Switch1To8"
        self.version = "2.5.0"
        self.width = 6

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_request(self.id, "GATE", 1, "Reset In")
        broker.register_request(self.id, "AUDIO", 2, "Main Signal Input")  # ➔ Port 2 fix
        
        # Outputs: route collision to legitimate ports 3 and 4!
        broker.register_offer(self.id, "AUDIO", 3, "Output 1")
        broker.register_offer(self.id, "AUDIO", 4, "Output 2")