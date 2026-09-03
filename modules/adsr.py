#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class AdsrModule:
    """Мікро-скрипт для нативного модуля VCV ADSR EG"""
    def __init__(self, instance_id, row_idx):
        self.id = instance_id
        self.row = row_idx
        self.type = "ADSR"

    def register_signals(self, broker, clean_chain):
        # 1. ПОТРЕБИ: чекає ритмічний імпульс у вхід GATE (Порт 0)
        broker.register_request(self.id, "GATE", 0, "Gate In")
        
        # 2. ПРОПОЗИЦІЇ: віддає готову криву напруги з виходу OUT (Порт 0)
        broker.register_offer(self.id, "CV_FREQ", 0, "Envelope Out")
