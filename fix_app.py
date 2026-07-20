with open("app.py", encoding="utf-8") as f:
    content = f.read()

content = content.replace("import requests\n", "")

old_block = """            with st.spinner("Analyzing..."):
                res = requests.post("http://127.0.0.1:8000/get-triage", json={"symptoms": all_symptoms})
                data = res.json()"""

new_block = """            with st.spinner("Analyzing..."):
                from triage import get_triage
                data = get_triage(all_symptoms)"""

if old_block in content:
    content = content.replace(old_block, new_block)
    print("Replacement made.")
else:
    print("WARNING: old block not found - no changes made to that section.")

with open("app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Done.")
