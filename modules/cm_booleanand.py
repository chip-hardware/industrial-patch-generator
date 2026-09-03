class CmBooleanandModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_BOOLEAN_AND"
        self.plugin = "CountModula"
        self.model = "BooleanAND"       # ➔ Valid binary slug
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "GATE", 0, "Input A")
        broker.register_request(self.id, "CLOCK", 1, "Input B")
        broker.register_offer(self.id, "GATE", 2, "AND Out") # ➔ Output port 2 fix