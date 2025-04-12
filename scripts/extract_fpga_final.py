#!/usr/bin/env python3
import hashlib
import struct

def extract_fpga_bitstream(file_path, output_path):
    # Відомі параметри
    fpga_offset = 0x12788  # Знайдена позиція FPGA секції
    header_size = 512      # Приблизний розмір заголовка
    data_size = 2386564    # Розмір даних з dumpimage
    expected_md5 = "b74948d6473c89ebd971e543c831c34d"
    
    with open(file_path, 'rb') as f:
        # Читаємо заголовок для аналізу
        f.seek(fpga_offset)
        header = f.read(header_size)
        
        # Шукаємо початок даних (після заголовка)
        data_start = fpga_offset + header_size
        
        # Читаємо FPGA bitstream
        f.seek(data_start)
        fpga_data = f.read(data_size)
        
        # Розраховуємо MD5
        calculated_md5 = hashlib.md5(fpga_data).hexdigest()
        
        print(f"Data extraction details:")
        print(f"Start offset: 0x{data_start:x}")
        print(f"Data size: {data_size} bytes")
        print(f"Calculated MD5: {calculated_md5}")
        print(f"Expected MD5: {expected_md5}")
        
        if calculated_md5 == expected_md5:
            print("MD5 match! Extracting correct data.")
            with open(output_path, 'wb') as out:
                out.write(fpga_data)
            return True
        else:
            print("MD5 mismatch! Trying alternative offset...")
            
            # Спробуємо знайти правильний офсет
            for offset in range(data_start - 256, data_start + 256, 4):
                f.seek(offset)
                test_data = f.read(data_size)
                test_md5 = hashlib.md5(test_data).hexdigest()
                
                if test_md5 == expected_md5:
                    print(f"Found correct offset at 0x{offset:x}")
                    with open(output_path, 'wb') as out:
                        out.write(test_data)
                    return True
            
            print("Could not find correct data!")
            return False

if __name__ == "__main__":
    input_file = "pluto_txrx.bin"
    output_file = "fpga.bit"
    if extract_fpga_bitstream(input_file, output_file):
        print(f"FPGA bitstream successfully extracted to {output_file}")
    else:
        print("Failed to extract FPGA bitstream")
