### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:   # "=" should be "==" to compare
      return True
    else                 #a colon is missing from after "else"
      return False
   

  dif highest_card(self, card1 card2): # def is spelled incorrectly + missing comma between card1 and card2
  if card1.value > card2.value:  # incorrect indentation (this line and the ones below should be indented further).  
    return card # this should return "card2", not "card".
  else:
    return card2 
  


# incorrect indentation
def cards_total(self, cards):
  total # this variable has not been initiated correctly - should state "total = 0"
  for card in cards:  
    total += card.value
    return "You have a total of" + total # return statement should be outside the for loop.  Need to convert int to string eg str(total) and missing space " " after the word "of"
  
```
