def jumpingOnClouds(c):
    # 剩下多少路要走的概念，來遞迴
    # [0, 1, 0]
    # 當剩下1步跟2步 回傳 0/ 1
    if len(c) == 1 : return 0
    if len(c) == 2: return 0 if c[1]==1 else 1

    # 如果第3步是 1 地雷, 加1步, 從第2步遞迴
    if c[2]==1:
        return 1 + jumpingOnClouds(c[1:])
    # 如果第3步 是 0, 加1步，從第3步開始遞迴
    if c[2]==0:
        return 1 + jumpingOnClouds(c[2:])


if __name__ == '__main__':
    pass
    # [0, 0, 0, 0, 1, 0]
    # 3
