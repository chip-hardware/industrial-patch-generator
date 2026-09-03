class CmEventtimerModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_EVENT_TIMER"
        self.plugin = "CountModula"
        self.model = "Countdown"           # ➔ Official legitimate slug
        self.version = "2.5.0"
        self.width = 8

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Trigger In")
        broker.register_offer(self.id, "GATE", 2, "End Gate Out") # ➔ Port 2 fix