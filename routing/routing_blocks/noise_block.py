#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def route_noise(local_mods, add_cable):
    """🎛️ Music routing for BLOCK 3 (NOISE). Textural and generative chaos."""
    noise = next((m for m in local_mods if m['meta_type'] == 'NOISE' or 'Noise' in m.get('model', '')), None)
    carousel = next((m for m in local_mods if m['meta_type'] == 'CM_CAROUSEL' or 'Carousel' in m.get('model', '')), None)
    vcf = next((m for m in local_mods if m['meta_type'] in ['VCF', 'FILTER']), None)
    vca = next((m for m in local_mods if m['meta_type'] in ['VCA', 'VCA-1']), None)

    # 1. Feed white or pink noise into Carousel (switcher) for random bursts
    if noise and carousel:
        add_cable(noise['id'], 0, carousel['id'], 0, "#3695ef") # White Noise -> Carousel IN 1
        add_cable(noise['id'], 1, carousel['id'], 1, "#00b56e") # Pink Noise -> Carousel IN 2

    # 2. Route the mangled noise output from Carousel to filtering
    if carousel and vcf:
        add_cable(carousel['id'], 2, vcf['id'], 0, "#f3374b") # Carousel OUT 1 -> Filter IN

    # 3. Use another noise output for non-linear dirty Drive boost on the filter
    if noise and vcf:
        add_cable(noise['id'], 2, vcf['id'], 3, "#ff5500") # Red Noise -> Filter DRIVE

    # 4. Texture output to the final row amplifier
    if vcf and vca:
        add_cable(vcf['id'], 5, vca['id'], 1, "#f3374b") # Filter HPF -> VCA IN