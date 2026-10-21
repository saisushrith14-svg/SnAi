import sys


filename = sys.argv[1]
field = int(sys.argv[2])
keyword = sys.argv[3]


with open(filename) as f:
    lines = f.readlines()
print("Total lines:", len(lines))


skipped=0
counts = {}


for line in lines:
    if not line.strip():
        skipped += 1 
        continue
    
    if keyword.lower() in line.lower():
        fields = line.split()
        if not len(fields) > field:
                skipped += 1
                continue
        key = fields[field]
        if key in counts:
            counts[key] += 1
        else:
             counts[key] = 1 
        
print("Top 5:")


ranked = sorted(
    counts.items(),
    key=lambda item: item[1],
    reverse=True
)
for i in range(min(len(ranked),5)):
     print(ranked[i])


print("Lines Skipped: ", skipped)