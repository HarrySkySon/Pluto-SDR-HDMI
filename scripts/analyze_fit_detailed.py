#!/usr/bin/env python3
import struct
import binascii

def print_hex_ascii(data, offset):
    hex_line = ' '.join(f'{b:02x}' for b in data)
    ascii_line = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in data)
    print(f"{offset:08x}: {hex_line:<48} {ascii_line}")

def analyze_file(file_path):
    with open(file_path, 'rb') as f:
        print("=== FIT Image Analysis ===")
        
        # Читаємо весь файл
        data = f.read()
        
        # Шукаємо секції та їх структуру
        sections = {
            b'fdt@': "Device Tree",
            b'fpga@': "FPGA Bitstream",
            b'linux_kernel@': "Linux Kernel",
            b'ramdisk@': "Initial RAM Disk"
        }
        
        for marker, desc in sections.items():
            pos = 0
            while True:
                pos = data.find(marker, pos)
                if pos == -1:
                    break
                    
                print(f"\n=== Found {desc} section at offset 0x{pos:x} ===")
                print("Header content:")
                # Показуємо 64 байти до і після знайденої позиції
                start = max(0, pos - 64)
                end = min(len(data), pos + 64)
                
                # Виводимо дані у форматі hex dump з ASCII
                for i in range(start, end, 16):
                    chunk = data[i:i+16]
                    print_hex_ascii(chunk, i)
                
                # Шукаємо розмір секції
                size_marker = b'Data Size'
                size_pos = data.find(size_marker, pos, pos + 256)
                if size_pos != -1:
                    # Пробуємо знайти число після "Data Size"
                    size_data = data[size_pos:size_pos+64]
                    print(f"\nSize information at offset 0x{size_pos:x}:")
                    print_hex_ascii(size_data, size_pos)
                
                pos += len(marker)

if __name__ == "__main__":
    input_file = "pluto_txrx.bin"
    analyze_file(input_file)
