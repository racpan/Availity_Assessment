import csv
from operator import itemgetter
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
companies = {}

with open(file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        u_id = row[0]
        name = row[1]
        version = row[2]
        key = row[3]
        if key in companies.keys():
            records = companies[key]
            try:
                record_index = next((index for (index, d) in enumerate(records) if d["u_id"] == u_id), None)
                if record_index and records[record_index]['version'] < version: 
                    companies[key][record_index].update({"version": version})
            except:
                append_data = {"u_id": u_id, "name": name, "version": version}
                companies[key].append(append_data)
        else:
            companies[key] = []
    
    for key in companies:
        items_to_write = sorted(companies[key], key=itemgetter('name'))
        f = open('key', 'w')
        writer = csv.writer(f)
        writer = csv.DictWriter(f, fieldnames=["User ID", "Name", "Version"])
        for item in items_to_write:
            writer.writerow(item)
        f.close()