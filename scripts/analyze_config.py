#!/usr/bin/python3

def analyze_config(filename):
   # Ключові слова для пошуку
   search_terms = {
       'HDMI': ['HDMI', 'DRM', 'FB', 'FRAMEBUFFER', 'VIDEO'],
       'DDR': ['DDR', 'MEMORY', 'RAM'],
       'Ethernet': ['ETHERNET', 'NET', 'MACB', 'PHY']
   }
   
   # Читаємо файл
   with open(filename, 'r') as f:
       content = f.readlines()
   
   print("Аналіз конфігурації ядра:\n")
   
   for category, terms in search_terms.items():
       print(f"\n=== {category} Configuration ===")
       for line in content:
           line = line.strip()
           if line.startswith('#') or not line:
               continue
           for term in terms:
               if term in line:
                   print(line)

print("Початок аналізу файлу .config...")
analyze_config('.config')
