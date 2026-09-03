class CmSwitch1to16Module:
    def __init__(self, instance_id, row_idx): self.id, self.row, self.type = instance_id, row_idx, "CM_SWITCH_1_16"
    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_request(self.id, "AUDIO", 4, "Signal Input")
        broker.register_offer(self.id, "AUDIO", 0, "Output 1")