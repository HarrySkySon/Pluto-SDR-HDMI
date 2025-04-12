#!/usr/bin/env python3
import binascii

def print_section_data(data, offset, length=64):
    # Друкуємо дані в hex і ASCII форматі
    hex_data = binascii.hexlify(data[offset:offset+length]).decode()
    print(f"\nOffset 0x{offset:08x}:")
    for i in range(0, len(hex_data), 32):
        hex_line = hex_data[i:i+32]
        bytes_data = data[offset+i//2:offset+i//2+16]
        ascii_line = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in bytes_data)
        print(f"{hex_line}  {ascii_line}")

def analyze_fit_structure(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        
    # Шукаємо всі основні секції
    sections = [
        (b'fdt@1', 'Device Tree 1'),
        (b'fdt@2', 'Device Tree 2'),
        (b'fdt@3', 'Device Tree 3'),
        (b'fpga@1', 'FPGA Bitstream'),
        (b'linux_kernel@1', 'Linux Kernel'),
        (b'ramdisk@1', 'RAM Disk')
    ]
    
    print("=== FIT Image Structure Analysis ===")
    
    for marker, description in sections:
        offset = data.find(marker)
        if offset != -1:
            print(f"\n=== {description} ===")
            print(f"Section marker '{marker.decode()}' found at offset: 0x{offset:x}")
            
            # Шукаємо метадані секції
            metadata_range = data[offset:offset+512]
            
            # Шукаємо розмір даних
            size_marker = b'Data Size'
            size_pos = metadata_range.find(size_marker)
            if size_pos != -1:
                print(f"Data Size marker found at relative offset: 0x{size_pos:x}")
                print_section_data(metadata_range, size_pos)
            
            # Шукаємо початок даних (зазвичай після нульових байтів)
            for i in range(len(metadata_range)-8):
                if metadata_range[i:i+8] == b'\x00' * 8:
                    print(f"Possible data start at relative offset: 0x{i:x}")
                    print_section_data(metadata_range, i)
                    break

if __name__ == "__main__":
    input_file = "pluto_txrx.bin"
    analyze_fit_structure(input_file)
