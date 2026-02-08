## Data Contract (Backend ↔ App)

The mobile application consumes ONLY the following files:

- index.json
- quizzes/**/*.json

No other files are accessed by the app.

### index.json structure

- Contains areas, difficulty levels and quiz metadata.
- It MUST respect the following structure:

```json
{
  "areas": [{ "id": "string", "nombre": "string" }],
  "niveles": [{ "id": "string", "nombre": "string" }],
  "quizzes": [
    {
      "id": "string",
      "titulo": "string",
      "area_id": "string",
      "nivel_id": "string",
      "archivo": "string",
      "version": "number"
    }
  ]
}
