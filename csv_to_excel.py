import pandas as pd
import os

# Относительный путь на один уровень выше
json_file = "divan_lighting.json"
excel_file = "../divan_lighting.xlsx"

# Загружаем JSON
df = pd.read_json(json_file)

# Сохраняем в Excel
df.to_excel(excel_file, index=False)

print(f"✅ Готово! Сохранено в {excel_file}")

# Удалим JSON (если хочешь)
if os.path.exists(json_file):
    os.remove(json_file)
    print(f"🗑️ Удалён временный файл: {json_file}")
else:
    print("⚠️ Файл JSON не найден для удаления.")
