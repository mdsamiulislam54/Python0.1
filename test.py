notes = [
    {
        "term": "test",
        "definition": "This is a test note.",
        "note": "Additional information about the test note."
    },
    {
        "term": "example",
        "definition": "This is an example note.",
        "note": "Additional information about the example note."
    },
    {
        "term": "sample",
        "definition": "This is a sample note.",
        "note": "Additional information about the sample note."
    },
    {
        "term": "demo",
        "definition": "This is a demo note.",
        "note": "Additional information about the demo note."
    }
]

query = "Test"

for note in notes:
    if query.lower() in note["term"].lower():
        print("Term:", note)
   

def find_term(notes, name):
    for note in notes:
        if note["term"].lower() == name.lower():
            return note

result = find_term(notes, "examples")
if result:
    print("Found term:", result)
else:
    print("Term not found.")
