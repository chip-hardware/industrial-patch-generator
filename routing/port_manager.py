#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class PortManager:
    """
    Global Rack Port Dispatcher & Collision Prevention Engine.
    Supports VCV Rack 2.5+ Stackable Inputs up to a defined saturation threshold.
    """
    def __init__(self, cables_array):
        self.cables = cables_array
        # Now storing not just port occupancy, but a cable counter: { module_id: { port_idx: count } }
        self.occupied_inputs = {} 

    def add_cable(self, out_mod_id, out_port, in_mod_id, in_port, color="#f3374b"):
        """
        Validates target input socket availability based on multi-cable stack headroom.
        """
        if out_mod_id is None or in_mod_id is None:
            return False
            
        if out_port is None or in_port is None:
            return False

        if in_mod_id not in self.occupied_inputs:
            self.occupied_inputs[in_mod_id] = {}
            
        if in_port not in self.occupied_inputs[in_mod_id]:
            self.occupied_inputs[in_mod_id][in_port] = 0
            
        # 🪐 STACK CONTROL: Limit density to 3 cables per ONE input port socket
        if self.occupied_inputs[in_mod_id][in_port] >= 3:
            return False
            
        # Duplicate protection: don't plug the exact same cable from the same output into the same socket
        for c in self.cables:
            if (c['outputModuleId'] == out_mod_id and c['outputId'] == int(out_port) and 
                c['inputModuleId'] == in_mod_id and c['inputId'] == int(in_port)):
                return False

        cable_id = random.randint(10**15, 10**16 - 1)
        self.cables.append({
            'id': cable_id,
            'outputModuleId': out_mod_id,
            'outputId': int(out_port),
            'inputModuleId': in_mod_id,
            'inputId': int(in_port),
            'color': color
        })
        
        # Increment the port occupancy counter inside the stack
        self.occupied_inputs[in_mod_id][in_port] += 1
        return True

    def is_input_free(self, module_id, in_port):
        """Check if there is still free space in the port stack (limit 3 cables)."""
        if module_id is None or module_id not in self.occupied_inputs:
            return True
        if in_port not in self.occupied_inputs[module_id]:
            return True
        return self.occupied_inputs[module_id][in_port] < 3

    def force_free_port(self, module_id, in_port):
        """Completely reset the port stack to zero."""
        if module_id in self.occupied_inputs and in_port in self.occupied_inputs[module_id]:
            self.occupied_inputs[module_id][in_port] = 0
            return True
        return False