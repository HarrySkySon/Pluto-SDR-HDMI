#!/usr/bin/python3

def find_kernel_section(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    
    # Шукаємо маркер linux_kernel@1
    marker = b'linux_kernel@1'
    kernel_pos = data.find(marker)
    
    if kernel_pos != -1:
        print(f"Found kernel marker at: 0x{kernel_pos:x}")
        
        # Переходимо назад до початку секції
        # Шукаємо MD5 хеш
        md5_marker = b'b74948d6473c89ebd971e543c831c34d'
        section_start = data.find(md5_marker)
        
        if section_start != -1:
            print(f"Found section start at: 0x{section_start:x}")
            
            # Читаємо 4.1MB даних після цього
            kernel_size = 4328000
            kernel_data = data[section_start:section_start + kernel_size]
            
            with open('kernel.bin', 'wb') as out:
                out.write(kernel_data)
            print(f"Written {len(kernel_data)} bytes to kernel.bin")

find_kernel_section('pluto_txrx.bin')
