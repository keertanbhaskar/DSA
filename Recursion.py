
def func(count):
  if count == 4:
    return
  print("keerti")
  func(count + 1)
func(0)


# Head Recursion
counting = 0
def func():
    global counting
    if counting == 4:
        return
    print("keerti")
    counting += 1
    func()

func()

# tail recursion (back tracking)
count1 = 0
def func():
   global count1
   if count1 == 4:
      return
   count1 += 1
   func()
   print("sam")
func()
      