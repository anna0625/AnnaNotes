<style>
.highlight1{
    color: #EAC100 !important;
}
.highlight2{
    color: #AFAF61;
}
.comingsoon{
    color: red;
}
</style>

## Python NoteBook
---

Stay here or [Go Back to Home Page](../index.md).<br/>
It doesn't include all syntaxs here, but here notes some Python's features.<br/>If you'd like to know more, you can check [Programming with Mosh](https://www.youtube.com/user/programmingwithmosh), which I've learning from, and it's really helpful for me to get into Python from beginning.<br/>
There is also free resrouce from [W3school Python Tutorial](https://www.w3schools.com/python/).<br/>
If you'd like to know the vocabulary about programming, please [check here](https://hackmd.io/@s4y0wTjhTAipbBv-m9yryg/rJTNZBXaH).

### Categories
* [Python Basic](#python-basic)
  * [Arguments](#arguments)
  * [Scope](#scope)
* [Data Structures](#data-structures)
* Exceptions

<br/>

## Python Basic
---

### Arguments
* xargs
  
```python
def numbers(*list):
    print(list)
# Space two lines.
# Space two lines.
numbers(2, 3, 4, 5)

# OUTPUT : (2, 3, 4, 5) <- It's a tuple.
```
* xxargs

If we want to pass keyword arguments...
```python
def save_user(**user):
    print(user)
    print(user["name"])


save_user(id=1, name="Lena")

# OUTPUT : {'id': 1, 'name': 'Lena'}
#          Lena
```

### Scope
* local variables

In Python, we don't have block level scope. No matter we define a variable in a function,
it is always `accessible` in that function after it is defined. So it is about `local variables`.
```python
def greet():
    if True:
        message = "Hi, the beautiful world!"
    print(message)


greet()

# OUTPUT : Hi, the beautiful world!
```

* global variables

```python
message = "Hello"

def greet():
    message = "Hi" 
    # It created a new local variable here.


greet()
print(message)

# OUTPUT : Hello
```
So, how to modify the value of global varible inside of a function? But `avoid` using the global
statment, it is a bad practice because this can create a side of effect in other functions.
```python
message = "Hello"

def greet():
    global message = "Hi"


greet()
print(message)

# OUTPUT : Hi
```

## Data Structures
---

### List
* List Unpacking

The lift number should be equal to the list.
```python
numbers = [1, 2, 3] # a list
first, second, third = numbers
print(first)

# OUTPUT : 1
```
This is wrong. It would be error with "too many values to unpack".
```python
numbers = [1, 2, 3]
first, second = numbers

# VALUEERROR!!
```
If there are many variables.. and we just want to care about the first and the second item.
```python
numbers = [1, 2, 3, 4, 4, ,4 , 5, 6]
first, second, *other = numbers
print(other)

# Here we can get the first and the last item.
first, *other, last = numbers 
print(last)

# OUTPUT : [3, 4, 4, 4, 5, 6] 
#          6
```

* Looping over Lists

```python
letters = ['a', 'b', 'c']

for index, letter in enumerate(letters): # letters became a tuple.
    print(index, letter)

# OUTPUT : 0 a  // index letter
#          1 b
#          2 c
```

* Adding, Removing or Finding Items

Adding
```python
letters = ['a', 'b', 'c']

letters.append('d')
letters.insert(0, '-')
print(letters)

# OUTPUT : ['-', 'a', 'b', 'c', 'd']
```
Removing
```python
letters = ['-', 'a', 'b', 'c', 'd']

letters.pop()
print(letters)

# OUTPUT : ['-', 'a', 'b', 'c']

letters.pop(0)
print(letters)

# OUTPUT : ['a', 'b', 'c']

letters.remove('b')
del letters[0:3]
letters.clear()
```
Finding
```python
letters = ['a', 'b', 'c']
print(letters.count('d'))

# OUTPUT : 0

if 'd' in letters:
    print(letters.index('d'))

# NO OUTPUT
```

* Sorting Items

```python
numbers = [1, 2, 6, 5, 4]
numbers.sort()
# It returns a new list, not modify the original list.
print(sorted(numbers))
numbers.sort(reverse=True)
print(sorted(numbers, reverse=True)
```
This is another way and it could be written in more beautiful way, please to check below this one.
```python
items = [
    ('Product1', 10),
    ('Product2', 50),
    ('product3', 30)
]

# It doesn't work here.
items.sort()

# The solution
def sort_item(item):
    return item[1] # return value

items.sort(key=sort_item)
print(items)

# OUTPUT : [('Product1', 10),
#          ('Product3', 30),
#          ('product2', 50)]
```

* Lambda Functions(expressions)

Here is to optimize the last codes. We also have items.
```python
items = [
    ('Product1', 10),
    ('Product2', 50),
    ('product3', 30)
]

# We don't need these.
#def sort_item(item):
#    return item[1] # return value

#items.sort(key=lambda parameters=expression)
items.sort(key=lambda item=item[1])
print(items)

# OUTPUT : [('Product1', 10),
#          ('Product3', 30),
#          ('product2', 50)]
```

* Map Function
  
How to make a list of the prices from products(items)?
```python
items = [
    ('Product1', 10),
    ('Product2', 50),
    ('product3', 30)
]

# one of the ways
prices = []
for item in items:
    prices.append(items[1])
print(prices)

# OUTPUT : [10, 50, 30]

# another way
map(lambda item:item[1], items) # It's a object.
prices = list(map(lambda item:item[1], items))
print(prices)

# OUTPUT : [10, 50, 30]
```

* Filter Function

How to get the product which price is greater than 10?
```python
items = [
    ('Product1', 10),
    ('Product2', 50),
    ('product3', 30)
]

filtered = list(filter(lambda item:item[1] > 10, items))
print(filtered)

# OUTPUT : [('Product3', 30),
#          ('product2', 50)]
```

* 