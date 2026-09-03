class CmTriggerSequencer8Module:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_TRIGGER_SEQUENCER_8"
        self.plugin = "CountModula"
        self.model = "TriggerSequencer8MkII"
        self.version = "2.5.0"
        self.width = 16

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_offer(self.id, "CLOCK", 2, "Ch 1 Trigger Out") # ➔ Port 2 fix