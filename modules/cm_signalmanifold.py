class CmSignalmanifoldModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_SIGNAL_MANIFOLD"
        self.plugin = "CountModula"
        self.model = "SignalManifold"
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "Input Mono")
        broker.register_offer(self.id, "AUDIO", 1, "Replicated Poly Out") # ➔ Port 1 fix