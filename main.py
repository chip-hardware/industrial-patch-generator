#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
import random
import os
from datetime import datetime
from packager import pack_vcv_archive
import routing

def load_modules_database():
    try:
        with open("database/modules.json", "r", encoding="utf-8") as f: return json.load(f)
    except FileNotFoundError: return {}

def load_knobs_database():
    try:
        with open("database/knobs_default.json", "r", encoding="utf-8") as f: return json.load(f)
    except FileNotFoundError: return {}

def parse_input_line(line_str):
    line_str = re.sub(r'^(Block\s*\d+:|^\d+\.\s*|Row\s*\d+:)', '', line_str.strip(), flags=re.IGNORECASE)
    normalized = re.sub(r'(→|\+|\bplus\b|,)', '|', line_str)
    return [p.strip().upper() for p in normalized.split('|') if p.strip()]

def parse_concept_file(filepath="concept.txt"):
    if not os.path.exists(filepath): return None
    categories = {"DRONE": [], "BASS": [], "RHYTHM": [], "NOISE": [], "MELODIC": []}
    current_cat = None
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line_raw = line.strip()
            if not line_raw: continue
            line_upper = line_raw.upper()
            
            if line_raw.startswith("##"):
                if "DRONE" in line_upper or "ДРОН" in line_upper: current_cat = "DRONE"
                elif "BASS" in line_upper or "БАС" in line_upper: current_cat = "BASS"
                elif "RHYTHM" in line_upper or "РИТМ" in line_upper: current_cat = "RHYTHM"
                elif "NOISE" in line_upper or "НОЙЗ" in line_upper: current_cat = "NOISE"
                elif "MELODIC" in line_upper or "МЕЛОДІК" in line_upper: current_cat = "MELODIC"
                continue
            if current_cat and "→" in line_raw:
                clean = re.sub(r'^\s*\d+[\.\)]?\s*', '', line_raw).strip()
                clean = re.sub(r'^\d+\s*[\.\)]\s*', '', clean).strip()
                if clean and len(clean) > 3: categories[current_cat].append(clean)
    return categories

def build_industrial_patch(raw_lines):
    db, knobs_db = load_modules_database(), load_knobs_database()
    if not db: return
    all_modules, all_cables, current_x, module_rows = [], [], 0, {}

    patch_unit_number = f"{random.randint(1, 99):02d}"
    patch_serial_tag = f"FACTORIAL_UNIT_{patch_unit_number}_DECAY"
    block_names = ["DRONE", "BASS", "RHYTHM", "NOISE", "MELODIC"]

    print(f"\n[1/3] 🏗️  Building Monolith: {patch_serial_tag}...")
    for row_idx, line in enumerate(raw_lines):
        module_names = parse_input_line(line)
        if not module_names: continue
        
        current_block_type = block_names[row_idx] if row_idx < len(block_names) else "HAZARD"
        print(f"  ⚡ Row {row_idx + 1} [{current_block_type}]: {' → '.join(module_names)}")
        
        if row_idx > 0:
            blank_id = random.randint(10**15, 10**16 - 1)
            visual_presets = [
                {"plugin": "Biset", "model": "Biset-Blank", "width": 14, "version": "2.0.14"},
                {"plugin": "VultModulesFree", "model": "BlackPanel", "width": 6, "version": "2.0.16"},
                {"plugin": "Extratone", "model": "XtrtnBlank", "width": 4, "version": "2.0.0"},
                {"plugin": "SIM", "model": "Blank", "width": 8, "version": "2.1.2"}
            ]
            preset = visual_presets[row_idx - 1] if (row_idx - 1) < len(visual_presets) else {"plugin": "VultModulesFree", "model": "BlackPanel", "width": 6, "version": "2.0.16"}
            
            all_modules.append({
                'id': blank_id, 'plugin': preset["plugin"], 'model': preset["model"], 'version': preset["version"], 
                'pos': [int(current_x), 0], 'text': f"UNIT_{patch_unit_number}_BRIDGE", 'data': {}, 'meta_type': 'BLANK'
            })
            current_x += int(preset["width"] - 1)
            
        for name in module_names:
            if name not in db:
                print(f"  ⚠️  Warning: Module [{name}] missing in database/modules.json! Skipped.")
                continue
            mod_id = random.randint(10**15, 10**16 - 1)
            
            target_meta = "SEQ3" if name == "MIDI-CV" else name
            module_data = {"params": knobs_db[target_meta]["params"]} if target_meta in knobs_db else {}
            
            if name == "MIDI-CV":
                target_plugin = "Fundamental"
                target_model = "SEQ3"
                target_version = "2.0.0"
                target_width = 27
            else:
                target_plugin = db[name]['plugin']
                target_model = db[name]['model']
                target_version = db[name]['version']
                target_width = db[name].get('width', 12)

            all_modules.append({
                'id': mod_id, 'plugin': target_plugin, 'model': target_model, 'version': target_version, 
                'pos': [int(current_x), 0], 'text': f"R{row_idx} // U_{patch_unit_number} // {current_block_type}",
                'data': module_data, 'meta_type': target_meta
            })
            module_rows[mod_id] = row_idx
            current_x += int(target_width - 1)

    print("  🏗️  Integrating Master FX rack into active hardware structures...")
    blank_id = random.randint(10**15, 10**16 - 1)
    all_modules.append({
        'id': blank_id, 'plugin': "VultModulesFree", 'model': "BlackPanel", 'version': "2.0.16",
        'pos': [int(current_x), 0], 'text': "MASTER_BRIDGE", 'data': {}, 'meta_type': 'BLANK'
    })
    current_x += 5

    master_pack = [
        {"model": "rexmix", "plugin": "repelzen", "version": "2.0.0", "width": 17, "meta": "rexmix"},
        {"model": "squinkylabs-comp", "plugin": "squinkylabs-plug1", "version": "2.1.9", "width": 9, "meta": "squinkylabs-comp"},
        {"model": "Plateau", "plugin": "Valley", "version": "2.4.5", "width": 19, "meta": "Plateau"},
        {"model": "SurgeXTFXDistortion", "plugin": "SurgeXTRack", "version": "2.2.9.0", "width": 12, "meta": "SurgeXTFXDistortion"}
    ]

    for fx in master_pack:
        fx_id = random.randint(10**15, 10**16 - 1)
        if fx["model"] == "rexmix":
            fx_module_block = {
                'id': fx_id, 'plugin': fx["plugin"], 'model': fx["model"], 'version': fx["version"],
                'pos': [int(current_x), 0], 'text': f"U_{patch_unit_number} // MASTER_FX",
                'meta_type': fx["meta"], 'params': [], 'data': {}
            }
        else:
            fx_data = {"params": knobs_db[fx["meta"]]["params"]} if fx["meta"] in knobs_db else {}
            fx_module_block = {
                'id': fx_id, 'plugin': fx["plugin"], 'model': fx["model"], 'version': fx["version"],
                'pos': [int(current_x), 0], 'text': f"U_{patch_unit_number} // MASTER_FX",
                'meta_type': fx["meta"], 'data': fx_data
            }
        all_modules.append(fx_module_block)
        module_rows[fx_id] = 5
        current_x += int(fx["width"])

    # 🚀 CALL ROUTING BEFORE CLEANING SERVICE TAGS!
    print("\n[2/3] 🔌 Pipeline Engine: Initializing dynamic signal routing matrix...")
    all_cables = routing.run_routing_pipeline(all_modules, raw_lines, module_rows, all_cables)

    # 🛡️ SYSTEMATIC AUTO-REPLACEMENT OF SLUGS AND BRANDS AFTER ALL ROUTING IS COMPLETE
    MODEL_SLUG_FIXES = { 
        "Multiple": "Mult",    
        "VCA Mix": "VCMixer", "VCAMix": "VCMixer", "VCA-Mix": "VCMixer", "Vcmixer": "VCMixer", "Mix": "VCMixer",
        "VoltageInverterMkII": "VoltageInverter", "VoltageInverterMk2": "VoltageInverter",
        "SampleAndHoldMkII": "SampleAndHold", "CarouselMkII": "Carousel",
        "SuperArpeggiator": "Arpeggiator", "Super Arpeggiator": "Arpeggiator",
        "Switch1To8MkII": "Switch1To8", "Switch8To1MkII": "Switch8To1"
    }

    for m in all_modules:
        current_model = m.get('model')
        if current_model in MODEL_SLUG_FIXES: 
            m['model'] = MODEL_SLUG_FIXES[current_model]

        # 🚀 CLEAN FIX: For ALL Count Modula modules, restore camelCase!
        if m.get('plugin') in ["CountModula", "countmodula"]:
            m['plugin'] = "CountModula"

        if m.get('model') == 'rexmix': m['plugin'] = 'repelzen'

        # 🚀 FINAL CLEANUP
        m.pop('meta_type', None)
        if 'leftModuleId' in m: del m['leftModuleId']
        if 'rightModuleId' in m: del m['rightModuleId']

    print("\n[3/3] 📦 Archiving... Compressing industrial preset block...")
    patch_data = {'version': "2.6.6", 'modules': all_modules, 'cables': all_cables}
    filename = f"{patch_serial_tag}_{datetime.now().strftime('%H%m%S')}.vcv"
    
    if pack_vcv_archive(patch_data, filename):
        print("=" * 60 + f"\n🔥 {patch_serial_tag} GENERATED SUCCESSFULLY!\n  📄 File: {filename}\n" + "=" * 60)

def main():
    print("=" * 60 + "\n🏭 INDUSTRIAL PATCH GENERATOR v14.0 (100% Native Output)\n" + "=" * 60)
    concepts = parse_concept_file("concept.txt")
    if concepts and all(concepts.values()):
        build_industrial_patch([
            random.choice(concepts["DRONE"]), random.choice(concepts["BASS"]), 
            random.choice(concepts["RHYTHM"]), random.choice(concepts["NOISE"]), random.choice(concepts["MELODIC"])
        ])

if __name__ == "__main__": main()