class CmVoltageinverterModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_VOLTAGE_INVERTER"
        self.plugin = "CountModula"
        self.model = "VoltageInverterMkII"
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "V_OCT", 0, "Input 1")
        broker.register_offer(self.id, "V_OCT", 1, "Inverted Output 1") # ➔ Port 1 fix and V_OCT tag