import sys
from collections import Counter
filename = sys.argv[1]
field = int(sys.argv[2])
keyword = sys.argv[3]
with open(filename) as f:
    lines = f.readlines()
print("Total lines:", len(lines))

counts = Counter()
for line in lines:
    if keyword.lower() in line.lower():
        fields = line.split()
        if len(fields) > field:
            key = fields[field]
            counts[key] += 1
print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)