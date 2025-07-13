class PriorityQueue:
    def __init__(self, condition):
        # condition is "min" or "max"
        self.condition = condition
        # 1‑based heap: index 0 unused
        self.keys = [None]
        self.vals = [None]
        self.keymap = {}   # key → heap index

    def __len__(self):
        return len(self.keys) - 1

    def isEmpty(self):
        return len(self) == 0

    def extreme(self):
        # return (key, val) at the root
        return self.keys[1], self.vals[1]

    def extractExtreme(self):
        if self.isEmpty():
            return None
        # root
        root_key = self.keys[1]
        root_val = self.vals[1]
        del self.keymap[root_key]

        # move last node to root
        last_idx = len(self)
        if last_idx > 1:
            self.keys[1] = self.keys[last_idx]
            self.vals[1] = self.vals[last_idx]
            self.keymap[self.keys[1]] = 1
        # pop last
        self.keys.pop()
        self.vals.pop()

        # bubble down from root
        idx = 1
        size = len(self)
        cond = (lambda parent, child: parent <= child) if self.condition == "min" else (lambda parent, child: parent >= child)

        while True:
            left = idx * 2
            right = left + 1
            best = idx

            if left <= size and not cond(self.vals[best], self.vals[left]):
                best = left
            if right <= size and not cond(self.vals[best], self.vals[right]):
                best = right

            if best == idx:
                break

            # swap idx and best
            self.keys[idx], self.keys[best] = self.keys[best], self.keys[idx]
            self.vals[idx], self.vals[best] = self.vals[best], self.vals[idx]
            self.keymap[self.keys[idx]] = idx
            self.keymap[self.keys[best]] = best
            idx = best

        return {"key": root_key, "val": root_val}

    def insert(self, key, val):
        # only insert if key not already present
        if key in self.keymap:
            return
        idx = len(self) + 1
        self.keys.append(key)
        self.vals.append(val)
        self.keymap[key] = idx

        # bubble up
        cond = (lambda parent, child: parent <= child) if self.condition == "min" else (lambda parent, child: parent >= child)
        while idx > 1:
            parent = idx // 2
            if cond(self.vals[parent], self.vals[idx]):
                break
            # swap
            self.keys[parent], self.keys[idx] = self.keys[idx], self.keys[parent]
            self.vals[parent], self.vals[idx] = self.vals[idx], self.vals[parent]
            self.keymap[self.keys[parent]] = parent
            self.keymap[self.keys[idx]] = idx
            idx = parent

def solution(n, ranges, shirts):
    contestants = ranges
    contestants.sort()
    
    shirts.sort()

    pq = PriorityQueue("min")
    i = 0 

    for s in shirts:
        while i < n and contestants[i][0] <= s:
            (l, r) = contestants[i]
            pq.insert(i, r)
            i += 1

        while not pq.isEmpty() and pq.extreme()[1] < s:
            pq.extractExtreme()

        if pq.isEmpty():
            return "Neibb"

        pq.extractExtreme()

    return "Jebb"

n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(0,n)]
shirts = list(map(int, input().split()))

print(solution(n,ranges,shirts))