#!/usr/bin/env python3
import struct
import binascii

def analyze_file(file_path):
    with open(file_path, 'rb') as f:
        # Читаємо перші 1024 байти для аналізу заголовка
        header = f.read(1024)
        
        print("=== FIT Header Analysis ===")
        # Шукаємо всі секції
        sections = [b'fdt@', b'fpga@', b'linux_kernel@', b'ramdisk@']
        
        for section in sections:
            pos = 0
            while True:
                pos = header.find(section, pos)
                if pos == -1:
                    break
                print(f"\nFound section {section.decode()} at offset: {pos}")
                # Показуємо 32 байти після знайденої секції
                print("Content after section:")
                print(binascii.hexlify(header[pos:pos+32]))
                pos += 1

        # Шукаємо специфічні маркери
        markers = [b'Description', b'Type', b'Compression', b'Data Size']
        for marker in markers:
            pos = header.find(marker)
            if pos != -1:
                print(f"\nFound {marker.decode()} at offset: {pos}")
                print("Content after marker:")
                print(binascii.hexlify(header[pos:pos+32]))

if __name__ == "__main__":
    input_file = "pluto_txrx.bin"
    analyze_file(input_file)
