#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SignalBroker:
    """
    Rack Signal Broker Matrix Engine v9.0.
    Dynamically tracks, allocates, and bridges operational signals (Requests & Offers)
    strictly bounded within isolated row boundaries to feed downstream patch managers.
    """
    def __init__(self, port_manager):
        self.pm = port_manager
        self.offers = {}   # Schema: { module_id: { signal_type: [{"port": X, "row": Y, "label": L}] } }
        self.requests = {} # Schema: { module_id: { signal_type: [{"port": X, "row": Y, "label": L}] } }

    def register_offer(self, module_id, signal_type, port_idx, row_idx=0, label=""):
        """Registers a hardware output socket asset anchored to a specific rack row alignment."""
        if module_id not in self.offers: 
            self.offers[module_id] = {}
        if signal_type not in self.offers[module_id]: 
            self.offers[module_id][signal_type] = []
        self.offers[module_id][signal_type].append({"port": port_idx, "row": row_idx, "label": label})

    def register_request(self, module_id, signal_type, port_idx, row_idx=0, label=""):
        """Registers a vacant hardware input socket requirement tied to a specific row level."""
        if module_id not in self.requests: 
            self.requests[module_id] = {}
        if signal_type not in self.requests[module_id]: 
            self.requests[module_id][signal_type] = []
        self.requests[module_id][signal_type].append({"port": port_idx, "row": row_idx, "label": label})
        
    def auto_route_remaining_signals(self, clean_chain, target_row_idx):
        """
        Scans unlinked peripheral and semantic inputs/outputs on the active row layout.
        Pairs unmatched nodes (e.g., AUDIO_FM, V_OCT_STEP) instantly to avoid dead ports.
        """
        # Dynamic color coding for complex sub-signal pathways
        semantic_colors = {
            "AUDIO_FM": "#ff5500",
            "AUDIO_LPF": "#f3374b",
            "AUDIO_HPF": "#ffb437",
            "V_OCT_STEP1": "#00b56e",
            "V_OCT_STEP2": "#11faaa",
            "CLOCK_DIV2": "#8b4ade",
            "CLOCK_DIV4": "#ff00ff"
        }

        for mod_id, types in list(self.requests.items()):
            for sig_type, req_list in types.items():
                # Skip core infrastructure buses handled explicitly in Wave 1
                if sig_type in ["CLOCK", "GATE", "CV_FREQ", "CV_RES", "V_OCT"]: 
                    continue
                
                wire_color = semantic_colors.get(sig_type, "#ff5500")
                
                for req in req_list:
                    if req['row'] == target_row_idx and self.pm.is_input_free(mod_id, req['port']):
                        # Locate an matching source offering the same sub-signal signature on this level
                        for prov_id, prov_types in self.offers.items():
                            if sig_type in prov_types:
                                for offer in prov_types[sig_type]:
                                    if offer['row'] == target_row_idx:
                                        self.pm.add_cable(prov_id, offer['port'], mod_id, req['port'], wire_color)
                                        break

    def link_bus_signals(self, clean_chain, signal_type, target_row_idx, color):
        """
        Bridges main structural control buses (Clock/Pitch/Gates) across row lanes.
        Guarantees isolation to ensure row modules align to their corresponding sub-systems.
        """
        # 1. Harvest active signal nodes exclusively tracking on the target rail floor
        row_providers = []
        for m in clean_chain:
            m_id = m['id']
            if m_id in self.offers and signal_type in self.offers[m_id]:
                for offer in self.offers[m_id][signal_type]:
                    if offer['row'] == target_row_idx:
                        row_providers.append((m_id, offer['port']))

        # 2. Map discovered providers sequentially to vacant request endpoints inside the row boundaries
        for m in clean_chain:
            m_id = m['id']
            if m_id in self.requests and signal_type in self.requests[m_id]:
                for req in self.requests[m_id][signal_type]:
                    if req['row'] == target_row_idx and self.pm.is_input_free(m_id, req['port']):
                        if row_providers:
                            # Primary source indexing: links the baseline row node to the consumer target port
                            provider_id, out_port = row_providers[0]
                            self.pm.add_cable(provider_id, out_port, m_id, req['port'], color)
