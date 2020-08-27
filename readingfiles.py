# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count += 1
    line = line.rstrip()
    start = line.find(":")
    num2add = float(line[start + 1:])
    total += num2add
    # print(my_sum)
    # print(count)
    avg = total / count
print("Average spam confidence:", avg)

