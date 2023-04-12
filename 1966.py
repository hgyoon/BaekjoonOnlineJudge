import sys
NUM_LINE = int(sys.stdin.readline())
for _ in range(NUM_LINE):
    NUM_ELEM, target_index = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    pop_count = 0
    while (queue):
        next_idx = queue.index(max(queue))
        for i in range(next_idx):
            queue.append(queue.pop(0))
            if target_index == 0:
                target_index = len(queue)-1
            else:
                target_index -= 1
        queue.pop(0)
        pop_count += 1
        if target_index == 0:
            break
        target_index -= 1
    print(pop_count)
