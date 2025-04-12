#!/usr/bin/env python3
import struct
import hashlib

def find_fpga_section(file_path):
    with open(file_path, 'rb') as f:
        # Читаємо файл по блоках
        block_size = 4096
        fpga_signature = b'fpga@1'  # Шукаємо маркер fpga@1
        
        while True:
            block = f.read(block_size)
            if not block:
                break
                
            # Шукаємо сигнатуру в блоці
            pos = block.find(fpga_signature)
            if pos != -1:
                # Знайшли сигнатуру, зберігаємо позицію
                abs_pos = f.tell() - len(block) + pos
                print(f"Found FPGA signature at offset: {abs_pos}")
                return abs_pos
    
    return None

def extract_fpga_bitstream(file_path, output_path):
    fpga_size = 2386564  # Розмір FPGA секції
    
    # Знаходимо позицію FPGA секції
    fpga_pos = find_fpga_section(file_path)
    if fpga_pos is None:
        print("FPGA section not found!")
        return False
        
    # Читаємо та зберігаємо FPGA bitstream
    with open(file_path, 'rb') as f:
        # Пропускаємо заголовок секції
        f.seek(fpga_pos)
        header = f.read(256)  # Читаємо достатньо для заголовка
        
        # Шукаємо початок даних після заголовка
        data_offset = fpga_pos
        for i in range(256):
            if header[i:i+4] == b'\x00\x00\x00\x00':
                data_offset = fpga_pos + i + 4
                break
        
        # Переходимо до початку даних
        f.seek(data_offset)
        fpga_data = f.read(fpga_size)
        
        # Перевіряємо MD5
        md5_hash = hashlib.md5(fpga_data).hexdigest()
        print(f"Extracted data MD5: {md5_hash}")
        print(f"Expected MD5: b74948d6473c89ebd971e543c831c34d")
        
        # Зберігаємо дані
        with open(output_path, 'wb') as out:
            out.write(fpga_data)
            print(f"FPGA bitstream saved to {output_path}")
            
        return True

if __name__ == "__main__":
    input_file = "pluto_txrx.bin"
    output_file = "fpga.bit"
    extract_fpga_bitstream(input_file, output_file)
