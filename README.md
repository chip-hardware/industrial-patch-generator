# vcv_patch – Industrial Patch Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![VCV Rack](https://img.shields.io/badge/VCV%20Rack-2.6.6%2B-blue)](https://vcvrack.com/)

This project is my personal tool for generating starter patches in VCV Rack. It was built for my own needs, but I've decided to share it because it can give beginners a great head start or serve as a solid foundation for your own experiments.

A generated patch is a raw technical structure. It contains no music or even a hint of it. Think of it as a "skeleton" that you fill with sound, tweak knobs, and repatch cables to discover your own industrial sound. 

Currently, the patch generation relies on a curated set of modules that I find most expressive and versatile for shaping dark, textured timbres: **Count Modula** modules for logic, sequencing, and complex modulation, **native VCV Rack** modules for the core utility and synthesis backbone, **Plateau** as a lush and gritty reverb to give space and depth, **Surge XT** effects—specifically its distortion units—for adding weight, harmonics, and aggressive bite, and **REX-MIX** as the final mixing and routing hub to glue everything together. This combination gives you a powerful, noise-friendly playground right out of the box.

**A generated patch is a raw technical structure.** It contains no music or even a hint of it. Think of it as a "skeleton" that you fill with sound, tweak knobs, and repatch cables to discover your own industrial sound.

---

## Who is this for?

### 🎯 For VCV Rack beginners
Instead of a blank screen, you get a ready-made, logically structured patch that you can load and start exploring immediately. It's like being handed a pre-assembled modular synth rather than just a box of parts.

### 🧠 For experienced users
It's a great way to quickly get a complex structure (5 blocks + a master section) so you can jump straight into sound design instead of spending time on the tedious work of building a patch from scratch.

---

## How it works

1. The generation is based on the `concept.txt` file. It contains **hundreds of signal chain variations** for different blocks:
   - **DRONE**
   - **BASS**
   - **RHYTHM**
   - **NOISE**
   - **MELODIC**

2. Run `main.py` from the project folder.

3. The generator randomly picks one chain from each block.

4. It builds a single patch, automatically:
   - Placing modules across 5 horizontal rows
   - Routing cables according to the selected chains
   - Adding a master section (mixer, compressor, reverb, distortion)
   - Producing a ready-to-use `.vcv` file that you can open in VCV Rack

```plaintext
vcv_patch/
├── main.py
├── packager.py
├── concept.txt
├── database/
│   ├── modules.json
│   └── knobs_default.json
├── routing/
│   ├── audio_core.py
│   ├── clock_bus.py
│   ├── filter_logic.py
│   ├── global_bridge.py
│   ├── modulation_core.py
│   ├── pipeline.py
│   ├── port_manager.py
│   ├── signal_broker.py
│   └── routing_blocks/
│       ├── drone_block.py
│       ├── bass_block.py
│       ├── rhythm_block.py
│       ├── noise_block.py
│       └── melodic_block.py
└── modules/
    ├── vco.py
    ├── vcf.py
    ├── vca.py
    └── ... (95+ module files)
```
- `main.py` — Main script that triggers generation
- `packager.py` — Creates the .vcv file from JSON
- `concept.txt` — Database of signal chains (you can add your own!)
- `database/` — Module and knob settings
- `routing/` — Automatic cable routing logic
- `modules/` — Descriptor scripts for each module

---

## A note on stability

> ⚠️ **The generated patch might not open on the first try.**

This can happen due to the sheer complexity of the resulting structure. If it doesn't load, simply **try opening it 2-3 times** – it usually works on the second or third attempt. This is normal behavior for this kind of complex, auto-generated patch.

---

## Expanding the project

The project is continuously evolving by adding new modules to the database. With **over 95 modules already supported**, this process could theoretically become **infinite** – there's always another module to add, another chain to create, another experiment to run.

If you want to add support for a new module:
1. Add its entry to `database/modules.json` (plugin, model, version, width)
2. Create a descriptor script in `modules/` (e.g., `my_module.py`)
3. Register its inputs and outputs using the `SignalBroker` API

The more modules you add, the more possibilities the generator can explore.

---

## Important disclaimer

This project was created **solely for personal use** and is shared **"AS-IS"**. It works stably for my tasks, but I do not guarantee it will work flawlessly with every VCV Rack configuration or set of installed modules.

If a module is missing from your system, the generator will simply skip it or fail to build the patch.

---

## Getting started

1. Clone or download this repository
2. Make sure you have the required Python packages:
   pip install zstandard
3. Run the generator:
   python main.py
4. Open the generated .vcv file in VCV Rack
5. Experiment! Twist knobs, repatch cables, make noise

---

## Philosophy

There are no right or wrong decisions here – just a space for experimentation.

If you're a beginner, start by opening a generated patch and just turn the knobs. See what each module does. Follow the cables. Break them and re-patch them. This is how you learn.

If you're experienced, use this as a rapid prototyping tool. Generate a complex structure in seconds, then mutate it into something entirely your own.

---

## License

MIT License – feel free to use, modify, and share.

---

Happy patching! 🎛️🔊
