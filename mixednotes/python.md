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
It doesn't include all syntaxs here, but here notes some Python's features.<br/>If you'd like to know more, you can check [Code with Mosh](https://codewithmosh.com/), which I've learning from.<br/>
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
# remember to space two lines
# remember to space two lines
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

```python
print("hello world!")
```
