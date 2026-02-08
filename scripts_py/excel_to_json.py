import pandas as pd
import json
from pathlib import Path

# Rutas
EXCEL_PATH = "../excel/test-excel-1.xlsx"
INDEX_PATH = "../index.json"

# Leer Excel
meta = pd.read_excel(EXCEL_PATH, sheet_name="meta")
preguntas_df = pd.read_excel(EXCEL_PATH, sheet_name="preguntas")

# Meta a diccionario
meta_dict = dict(zip(meta["campo"], meta["valor"]))

# Construir preguntas
preguntas = []
for _, row in preguntas_df.iterrows():
    preguntas.append({
        "id": int(row["id"]),
        "pregunta": row["pregunta"],
        "opciones": [
            row["A"], row["B"], row["C"], row["D"], row["E"]
        ],
        "respuesta_correcta": row["correcta"]
    })

# JSON del quiz
quiz_json = {
    "tema": meta_dict["tema"],
    "descripcion": meta_dict["descripcion"],
    "preguntas": preguntas
}

# Guardar quiz
quiz_path = Path(f"../{meta_dict['archivo']}")
quiz_path.parent.mkdir(parents=True, exist_ok=True)

with open(quiz_path, "w", encoding="utf-8") as f:
    json.dump(quiz_json, f, ensure_ascii=False, indent=2)

# Actualizar index
if Path(INDEX_PATH).exists():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index_data = json.load(f)
else:
    index_data = []

# Evitar duplicados
index_data = [i for i in index_data if i["id"] != meta_dict["id_index"]]

index_data.append({
    "id": meta_dict["id_index"],
    "titulo": meta_dict["titulo"],
    "area": meta_dict["area"],
    "nivel": meta_dict["nivel"],
    "preguntas": len(preguntas),
    "archivo": meta_dict["archivo"]
})

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(index_data, f, ensure_ascii=False, indent=2)

print("✔ Quiz generado y index actualizado")
