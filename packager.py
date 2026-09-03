#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import tarfile
import zstandard as zstd
import io

def pack_vcv_archive(patch_data, target_filename):
    """
    Accepts a patch_data dictionary, converts it to JSON,
    wraps it in TAR format (USTAR), and compresses it using Zstandard.
    Fully compatible with VCV Rack 2.6.6+.
    """
    try:
        # 1. Convert the patch structure to indented JSON text bytes
        json_string = json.dumps(patch_data, indent=4, ensure_ascii=False)
        # FIX: Use the correct local variable json_string instead of json.string
        json_bytes = json_string.encode('utf-8')
        
        # 2. Create an in-memory TAR archive stream
        tar_stream = io.BytesIO()
        
        with tarfile.open(fileobj=tar_stream, mode='w', format=tarfile.USTAR_FORMAT) as tar:
            # Create meta-information about the patch.json file inside the archive
            tarinfo = tarfile.TarInfo(name='patch.json')
            tarinfo.size = len(json_bytes)
            tarinfo.mode = 0o644  # Standard read/write permissions
            tarinfo.type = tarfile.REGTYPE  # Regular file type
            
            # Add the patch structure bytes to the TAR stream
            tar.addfile(tarinfo, io.BytesIO(json_bytes))
            
    except Exception as e:
        print(f"❌ Internal error while forming TAR structure: {e}")
        return False

    try:
        # 3. Initialize the Zstandard compressor with compression level 3 (VCV default)
        cctx = zstd.ZstdCompressor(
            level=3, 
            write_content_size=True, 
            write_checksum=True
        )
        
        # Compress the entire generated TAR archive
        zstd_compressed_bytes = cctx.compress(tar_stream.getvalue())
        
        # 4. Write the final binary result to disk with .vcv extension
        with open(target_filename, 'wb') as f_out:
            f_out.write(zstd_compressed_bytes)
            
        return True
        
    except Exception as e:
        print(f"❌ Zstd compression or file write error: {e}")
        return False