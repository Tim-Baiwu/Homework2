import csv
with open("product_data.csv", "r", encoding="utf-8") as inp_file:
    f = csv.reader(inp_file)
    with open("expensive.csv", "w", encoding="utf-8", newline = "") as out_file:
        w = csv.writer(out_file)
        head = next(f)
        w.writerow(head)
        for row in f:
            if float(row[2]) > 100:
                w.writerow(row)