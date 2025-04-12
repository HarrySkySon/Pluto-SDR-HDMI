#!/usr/bin/env python3
import struct
import binascii

def print_section(name, data, offset, length=32):
    print(f"\n=== {name} ===")
    hex_data = binascii.hexlify(data[offset:offset+length]).decode()
    ascii_data = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in data[offset:offset+length])
    print(f"Offset: 0x{offset:08x}")
    print(f"Hex: {hex_data}")
    print(f"ASCII: {ascii_data}")

def analyze_boot_bin(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
            
    print("\n=== Boot.bin Analysis ===")
    print(f"File size: {len(data)} bytes")
        
    # Шукаємо заголовок Xilinx
    xilinx_header = b'Xilinx'
    pos = data.find(xilinx_header)
    if pos != -1:
        print_section("Xilinx Header", data, pos)
            
    # Шукаємо інформацію про конфігурацію
    config_markers = [b'FPGA', b'BOOT', b'CONF', b'DDR']
    for marker in config_markers:
        pos = data.find(marker)
        if pos != -1:
            print_section(f"{marker.decode()} Configuration", data, pos)

def analyze_fsbl_elf(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
            
    print("\n=== FSBL.elf Analysis ===")
    print(f"File size: {len(data)} bytes")
        
    # Перевіряємо ELF магічні числа
    if data[:4] == b'\x7fELF':
        print("Valid ELF file found")
            
        # Аналізуємо заголовок ELF
        e_machine = struct.unpack('H', data[18:20])[0]
        print(f"Target architecture: {hex(e_machine)}")
            
        # Шукаємо важливі конфігураційні рядки
        config_strings = [b'DDR', b'FPGA', b'CONFIG', b'BOOT']
        for string in config_strings:
            positions = []
            pos = 0
            while True:
                pos = data.find(string, pos)
                if pos == -1:
                    break
                positions.append(pos)
                pos += 1
                
            if positions:
                print(f"\nFound {string.decode()} related data at offsets:")
                for pos in positions[:3]:  # Показуємо перші 3 входження
                    print_section(f"{string.decode()} Configuration", data, pos)

if __name__ == "__main__":
    try:
        boot_file = "boot.bin"
        fsbl_file = "fsbl.elf"
    
        print("Analyzing boot files...")
        analyze_boot_bin(boot_file)
        analyze_fsbl_elf(fsbl_file)
    except Exception as e:
        print(f"Error: {e}")
