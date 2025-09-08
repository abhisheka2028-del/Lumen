
processes = [
    ["P1", 0, 5],
    ["P2", 1, 3],
    ["P3", 2, 8],
    ["P4", 3, 6]
]


processes.sort(key=lambda x: x[1])

time = 0
completion_time = []
turnaround_time = []
waiting_time = []
gantt_chart = []

for p in processes:
    pname, at, bt = p

   
    if time < at:
        time = at

    start = time
    time += bt
    end = time

   
    ct = end
    tat = ct - at
    wt = tat - bt

    completion_time.append(ct)
    turnaround_time.append(tat)
    waiting_time.append(wt)

    gantt_chart.append((pname, start, end))


print("Process | AT | BT | CT | TAT | WT")
for i, p in enumerate(processes):
    print(f"{p[0]:7} | {p[1]:2} | {p[2]:2} | {completion_time[i]:2} | {turnaround_time[i]:3} | {waiting_time[i]:2}")

avg_tat = sum(turnaround_time) / len(turnaround_time)
avg_wt = sum(waiting_time) / len(waiting_time)

print(f"\nAverage Turnaround Time = {avg_tat:.2f}")
print(f"Average Waiting Time    = {avg_wt:.2f}")


print("\nGantt Chart:")
for g in gantt_chart:
    print(f"| {g[0]} ", end="")
print("|")

for g in gantt_chart:
    print(f"{g[1]:2}   ", end="")
print(f"{gantt_chart[-1][2]:2}")













