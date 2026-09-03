class Vcf2Module:
    def __init__(self, instance_id, row_idx):
        self.id, self.row, self.type = instance_id, row_idx, "VCF2"
    def register_signals(self, broker, clean_chain):
        broker.register_request(self.id, "AUDIO", 0, "Audio In")
        broker.register_offer(self.id, "AUDIO", 1, "LPF Out")