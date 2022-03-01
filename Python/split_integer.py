def split_integer(num, parts):
    answer = divmod(num,parts)
    checks = ((str(answer[0])+' ') * parts).split()
    ans = [int(x) for x in checks]
    if answer[1] > 0:
      counter = 0
      total = sum(ans)
      for x in ans:
        if sum(ans) < num:
          ans.append(x+1)
          ans = ans[1:]
          print(ans[1:])
    return(ans)