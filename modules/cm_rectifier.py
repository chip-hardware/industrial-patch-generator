class CmRectifierModule:
    """Micro-script for Count Modula Rectifier module"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_RECTIFIER"
        self.plugin = "CountModula"
        self.model = "Rectifier"
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "Signal In")
        broker.register_offer(self.id, "AUDIO", 1, "Full Wave Out")       # ➔ Port 1 fix
        broker.register_offer(self.id, "AUDIO", 2, "Positive Half Out")   # ➔ Valid AUDIO tag