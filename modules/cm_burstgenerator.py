class CmBurstgeneratorModule:
    """Micro-script per manual for Count Modula Burst Generator"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_BURST_GENERATOR"
        self.plugin = "CountModula"
        self.model = "BurstGenerator"   # ➔ Official clean slug
        self.version = "2.5.0"
        self.width = 10

    def register_signals(self, broker, clean_chain):
        # 🪐 INPUT: Trigger In — Port 0
        broker.register_request(self.id, "CLOCK", 0, "Trigger In")
        
        # 🪐 OUTPUT: Burst Output — Port 2
        broker.register_offer(self.id, "GATE", 2, "Burst Output (Pulses)")