# Stack works on last in first out(LIFO)
class stack:
  def __init__(self):
    self.list = []

  def length(self):
    return len(self.list)
  
  def push(self,value):
    self.list.insert(0,value)

  def peek(self):
    if len(self.list) == 0:
      raise Exception("Stack is empty")
    else:
      return self.list[0]
    
  def pop(self):
    if len(self.list) == 0:
      raise Exception("Stack is empty")
    else:
      return self.list.pop(0)
    
  def __str__(self):
    return str(self.list)
    
stk = stack()

stk.push(20)
stk.push(23)
stk.push(67)
stk.pop()
print(stk)
print(stk.peek())


