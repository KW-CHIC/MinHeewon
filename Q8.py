# 빗물 트래핑 (p.180) (풀이1 참조)

def trap(height):
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
    volume = 0
    while left < right:
        if left_max <= right_max :
            volume += left_max - height[left]
            left += 1
            left_max = max(left_max, height[left])
        else :
            volume += right_max - height[right]
            right -= 1
            right_max = max(right_max, height[right])
    return volume

result = trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(result)
