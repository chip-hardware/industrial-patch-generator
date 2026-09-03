class CmMuteModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_MUTE"
        self.plugin = "CountModula"
        self.model = "Mute"
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "Audio Input 1")
        broker.register_request(self.id, "GATE", 2, "Mute Control In")
        broker.register_offer(self.id, "AUDIO", 1, "Muted Audio Out 1") # ➔ Port 1 fix