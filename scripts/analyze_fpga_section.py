#!/usr/bin/env python3
import struct
import binascii

def analyze_fpga_section(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        
        print("=== FPGA Section Analysis ===")
        
        # Шукаємо FPGA секцію
        fpga_marker = b'fpga@1'
        fpga_pos = data.find(fpga_marker)
        
        if fpga_pos == -1:
            print("FPGA section not found!")
            return
            
        print(f"FPGA section found at offset: 0x{fpga_pos:x}")
        
        # Шукаємо важливі маркери після позиції FPGA
        search_range = data[fpga_pos:fpga_pos+512]
        
        markers = [
            b'Description',
            b'Type',
            b'Compression',
            b'Data Size',
            b'Load Address',
            b'Hash algo',
            b'Hash value'
        ]
        
        section_info = {}
        for marker in markers:
            pos = search_range.find(marker)
            if pos != -1:
                # Читаємо 32 байти після маркера
                marker_data = search_range[pos:pos+64]
                # Конвертуємо в читабельний формат
                readable = marker_data.split(b'\0')[0].decode('utf-8', errors='ignore')
                section_info[marker.decode()] = readable
        
        # Виводимо знайдену інформацію
        print("\nFPGA Section Details:")
        for key, value in section_info.items():
            print(f"{key}: {value}")
            
        # Шукаємо початок даних
        # Зазвичай це після всіх заголовків та вирівнювання
        possible_data_start = fpga_pos + 512  # Приблизна позиція
        
        print(f"\nPossible data start: 0x{possible_data_start:x}")
        print(f"Expected size from dumpimage: 2386564 bytes")
        
if __name__ == "__main__":
    input_file = "pluto_txrx.bin"
    analyze_fpga_section(input_file)
