#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib
import os

from routing.audio_core import process_audio_lanes
from routing.modulation_core import process_modulation_rings

def run_routing_pipeline(all_modules, raw_lines, module_rows, cables):
    """Main evolutionary routing pipeline Network Matrix Engine v47.0"""
    from routing.port_manager import PortManager
    from routing.signal_broker import SignalBroker

    pm = PortManager(cables)
    broker = SignalBroker(pm)

    # Isolate service modules
    clean_chain = [m for m in all_modules if m.get('meta_type') not in ['BLANK', 'rexmix', 'squinkylabs-comp', 'Plateau', 'SurgeXTFXDistortion']]

    module_objects = []
    
    print("\n[2/3] 🔌 Pipeline Engine: Dynamic hardware object import loop...")
    for m in clean_chain:
        meta_type = m.get('meta_type', 'UNKNOWN')
        if meta_type == 'UNKNOWN':
            continue

        filename_base = meta_type.lower().split('-')
        module_filename = "vca" if "vca" in filename_base else meta_type.lower().replace('-', '_')
        
        target_path = f"modules/{module_filename}.py"
        if os.path.exists(target_path):
            try:
                module_pack = importlib.import_module(f"modules.{module_filename}")
                module_class = None
                for attr in dir(module_pack):
                    if attr.lower() == f"{module_filename.replace('_', '')}module":
                        module_class = getattr(module_pack, attr)
                        break
                
                if module_class:
                    row_idx = module_rows.get(m['id'], 0)
                    mod_instance = module_class(m['id'], row_idx)
                    mod_instance.register_signals(broker, clean_chain)
                    module_objects.append(mod_instance)
            except Exception as e:
                print(f"    ⚠️  Initialization failure for modules/{module_filename}.py: {e}")

    # =========================================================================
    # ⚡ 🚀 NEW West-Coast ENGINE: DYNAMIC BLOCK SCRIPT INVOCATION (WAVE 0)
    # =========================================================================
    # Force-load floor sub-scripts and stuff their sockets with cables via pm.add_cable
    block_routing_files = {
        0: "drone_block",
        1: "bass_block",
        2: "rhythm_block",
        3: "noise_block",
        4: "melodic_block"
    }

    print("  🔌 Injecting high-density West-Coast block patch matrices...")
    for row_idx, block_name in block_routing_files.items():
        block_path = f"routing/routing_blocks/{block_name}.py"
        if os.path.exists(block_path) or os.path.exists(f"routing_blocks/{block_name}.py"):
            try:
                # Support dynamic import of sub-scripts from any folder location
                module_path_str = f"routing.routing_blocks.{block_name}" if os.path.exists("routing/routing_blocks") else f"routing_blocks.{block_name}"
                block_module = importlib.import_module(module_path_str)
                
                # Look for the routing function inside the file (route_drone, route_bass, etc.)
                route_func = None
                for attr in dir(block_module):
                    if attr.startswith("route_"):
                        route_func = getattr(block_module, attr)
                        break
                
                if route_func:
                    # Strictly filter modules for the current floor
                    floor_modules = [m for m in clean_chain if module_rows.get(m['id'], -1) == row_idx]
                    # Call total port stuffing, passing a direct link to pm.add_cable!
                    route_func(floor_modules, pm.add_cable)
            except Exception as e:
                print(f"    ⚠️  Failure executing block routing script [{block_name}]: {e}")

    # WAVE 1: CORE SYNCHRONIZATION AND STRIP BUS TRACKS
    for row_idx in range(len(raw_lines)):
        broker.link_bus_signals(clean_chain, "CLOCK", row_idx, "#8b4ade")
        broker.link_bus_signals(clean_chain, "GATE", row_idx, "#00b56e")
        broker.link_bus_signals(clean_chain, "V_OCT", row_idx, "#11faaa")
        broker.link_bus_signals(clean_chain, "CV_FREQ", row_idx, "#3695ef")
        broker.link_bus_signals(clean_chain, "CV_RES", row_idx, "#ff00ff")
        broker.auto_route_remaining_signals(clean_chain, row_idx)
        
    # WAVE 2: MAIN AUDIO LANES PROCESSING
    process_audio_lanes(all_modules, module_rows, pm)

    # WAVE 3: ADVANCED CROSS-MODULATION AND FEEDBACK RING MATRICES
    process_modulation_rings(clean_chain, module_rows, pm)

    # WAVE 3.5: CROSS-ROW BLOCK INTER-INTELLIGENCE INTERFACE
    try:
        from routing.global_bridge import process_inter_block_intelligence
        print("  🧠 Launching Inter-Block Intelligence System (Network Communication)...")
        process_inter_block_intelligence(clean_chain, module_rows, pm)
    except ImportError:
        pass

    # Global LFO drift
    global_lfo = next((m for m in clean_chain if m['meta_type'] in ['LFO', 'LFO2', 'WTLFO']), None)
    if global_lfo:
        for m in clean_chain:
            if m['meta_type'] in ['VCF', 'FILTER']: 
                pm.add_cable(global_lfo['id'], 0, m['id'], 2, "#3695ef")

    for obj in module_objects:
        if hasattr(obj, "process_advanced_sync"):
            obj.process_advanced_sync(clean_chain, pm)

    extracted_cables = pm.cables if hasattr(pm, 'cables') else cables
    print(f"  🔌 [Matrix Success]: Extraction loop complete. Total active industrial cables: {len(extracted_cables)}")
    
    return extracted_cables