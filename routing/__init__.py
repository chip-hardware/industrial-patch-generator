#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Системне ядро Органічного Комутатора v8.0.
Керує автоматичним розподілом сигналів через PortManager, SignalBroker та Pipeline.
"""

from .pipeline import run_routing_pipeline

__all__ = [
    'run_routing_pipeline'
]
