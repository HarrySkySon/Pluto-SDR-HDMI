#!/usr/bin/env python3
import struct
import os
import binascii

def find_section_data(file_path, section_name):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Шукаємо початок секції
    section_start = content.find(f"{section_name} {{")
    if section_start == -1:
        return None, None
    
    # Шукаємо поле data
    data_start = content.find("data = ", section_start)
    if data_start == -1:
        return None, None
    
    # Визначаємо формат даних
    if content[data_start:].startswith("data = ["):
        # Формат [d0 0d fe ed ...]
        data_start = content.find("[", data_start) + 1
        data_end = content.find("]", data_start)
        data_format = "hex"
    else:
        # Формат <0xa0e1 0xa0e1 ...>
        data_start = content.find("<", data_start) + 1
        data_end = content.find(">", data_start)
        data_format = "word"
    
    if data_end == -1:
        return None, None
    
    return content[data_start:data_end].strip(), data_format

def decode_hex_data(hex_data):
    # Конвертуємо hex рядок в бінарні дані
    hex_str = hex_data.replace("\n", "").replace(" ", "")
    try:
        return binascii.unhexlify(hex_str)
    except:
        return None

def decode_word_data(word_data):
    # Конвертуємо 0xa0e1 формат в бінарні дані
    words = word_data.split()
    try:
        binary = bytearray()
        for word in words:
            value = int(word, 16)
            binary.extend(value.to_bytes(4, 'little'))
        return binary
    except:
        return None

def main():
    sections = ['fdt@1', 'fdt@2', 'fdt@3', 'fpga@1', 'linux_kernel@1', 'ramdisk@1']
    input_file = "pluto.dts"
    
    print(f"Analyzing {input_file}...")
    for section in sections:
        print(f"\nProcessing section {section}")
        data, data_format = find_section_data(input_file, section)
        
        if data is None:
            print(f"Section {section} not found or no data field")
            continue
        
        # Створюємо бінарний файл в залежності від формату
        if data_format == "hex":
            binary = decode_hex_data(data)
            extension = ".dtb" if section.startswith("fdt@") else ".bin"
        else:
            binary = decode_word_data(data)
            extension = ".bin"
        
        if binary:
            output_file = f"{section}{extension}"
            with open(output_file, 'wb') as f:
                f.write(binary)
            print(f"Created {output_file} ({len(binary)} bytes)")
            
            # Якщо це FDT секція, конвертуємо в DTS
            if section.startswith("fdt@"):
                try:
                    os.system(f'dtc -I dtb -O dts -o {section}.dts {output_file}')
                    print(f"Converted to {section}.dts")
                except:
                    print(f"Failed to convert {output_file} to DTS")
        else:
            print(f"Failed to decode data for {section}")

if __name__ == '__main__':
    main()
