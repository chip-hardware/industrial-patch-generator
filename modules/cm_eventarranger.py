class CmEventarrangerModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_EVENT_ARRANGER"
        self.plugin = "CountModula"
        self.model = "EventArranger"       # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 6

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_offer(self.id, "GATE", 2, "Pattern Out") # ➔ Port 2 fix