test1 = [0,2,4,1,6,2]
test2 = [2, -1, 0, 2]

def fences(jumps):
      len_fence = len(jumps)-1
      if len_fence in jumps:
            return True
      else:
            jumps.sort()
            for num in jumps:
                  summ = 0
                  while summ <= len_fence:
                        ans = len_fence - num
                        if ans in jumps:
                              return True
                        else: summ+=ans


fences(test1)