import csv
with open('requirements.csv', newline='') as f:
    for r in csv.DictReader(f):
        print(f"{r['Requirement']}: {r['MoSCoW']} / {r['Kano']}")
