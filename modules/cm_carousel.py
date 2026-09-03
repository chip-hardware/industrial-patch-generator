class CmCarouselModule:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "CM_CAROUSEL"
        self.plugin = "CountModula"
        self.model = "Carousel"         # ➔ Official binary slug
        self.version = "2.5.0"
        self.width = 8

    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "CLOCK", 0, "Trigger Up")
        broker.register_request(self.id, "AUDIO", 1, "Input 1")
        broker.register_offer(self.id, "AUDIO", 5, "Output 1") # ➔ Output port 5 fix