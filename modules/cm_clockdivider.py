class CmClockdividerModule:
    """Micro-script for Count Modula Clock Divider MkII"""
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_CLOCK_DIVIDER"
        self.plugin = "CountModula"
        self.model = "ClockDividerMkII" # ➔ Official MkII slug for Rack 2.x
        self.version = "2.5.0"
        self.width = 4

    def register_signals(self, broker, clean_chain):
        # Inputs: receives the main rack clock
        broker.register_request(self.id, "CLOCK", 0, "Clock In")
        broker.register_request(self.id, "GATE", 1, "Reset In")       # ➔ GATE tag for Reset
        
        # Outputs: route collision to legitimate ports 2, 3, 4, 5!
        broker.register_offer(self.id, "CLOCK", 2, "Divide by 2")
        broker.register_offer(self.id, "CLOCK", 3, "Divide by 4")
        broker.register_offer(self.id, "CLOCK", 4, "Divide by 8")
        broker.register_offer(self.id, "CLOCK", 5, "Divide by 16")