class CmClockedrandomgatesModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_CLOCKED_RANDOM_GATES"
        self.plugin = "CountModula"
        self.model = "ClockedRandomGates" # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_request(self.id, "GATE", 1, "Reset In")
        broker.register_offer(self.id, "GATE", 2, "Out 1") # ➔ Port 2 fix
        broker.register_offer(self.id, "GATE", 3, "Out 2") # ➔ Port 3 fix