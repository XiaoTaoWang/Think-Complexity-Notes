# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 11:25:52 2017

@author: XiaoTao Wang
"""

import heapq, itertools

class PriorityQueue():
    
    REMOVED = '<removed-task>'
    
    def __init__(self):
        self.hq = []
        self.entry_finder = {}
        self.counter = itertools.count()
    
    def add_with_priority(self, task, priority):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.hq, entry)
    
    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED
    
    def extract_min(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.hq:
            priority, count, task = heapq.heappop(self.hq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task, priority
        raise KeyError('pop from an empty priority queue')