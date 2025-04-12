#!/usr/bin/env python3

def analyze_uboot_env(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            
        print("=== U-Boot Environment Analysis ===\n")
        
        # U-Boot environment зберігає змінні у форматі "name=value\0"
        # Розділяємо на окремі записи
        entries = data.split(b'\x00')
        
        # Виводимо всі знайдені змінні
        for entry in entries:
            if entry:  # пропускаємо пусті записи
                try:
                    # Декодуємо як ASCII, ігноруємо помилки
                    decoded = entry.decode('ascii', errors='ignore')
                    if '=' in decoded:
                        name, value = decoded.split('=', 1)
                        print(f"{name.strip():<20} = {value.strip()}")
                except:
                    continue
                    
    except Exception as e:
        print(f"Error analyzing file: {e}")

if __name__ == "__main__":
    input_file = "uboot-env.bin"
    analyze_uboot_env(input_file)
