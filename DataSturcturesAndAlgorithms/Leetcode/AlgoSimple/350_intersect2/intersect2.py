# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:25:11 2020

@author: kevin.fei
"""
#两个数组的交际2
import collections

def intersect(nums1,nums2):
#哈希表
    # 取小的list作为哈希表，提高效率
#    if len(nums1) > len(nums2):
#            return self.intersect(nums2, nums1)
    m = collections.Counter()
    # 建立哈希表
    for num in nums1:
        m[num] += 1
    
    intersection = list()
    for num in nums2:
        count = m.get(num,0)
        print(count)
        if(count) > 0:
            intersection.append(num)
            m[num] -= 1
            if m[num] ==0:
                m.pop(num)
    
    return intersection

print(intersect([1,2,2,1,4,5],[2,2,1,1,6,8,9,0,1,4]))
    