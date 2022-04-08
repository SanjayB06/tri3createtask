## User input


```py
userSelection = input("What is a book you have recently read and liked? ")
```

## Data collection
```py
data = {books.loc[str(k),"isbn13"]:[books.loc[str(k),"title"],books.loc[str(k),"authors"].replace('/'," and ")] for k in list(data.keys())[:5]}

```

## Procedure

```py
def dispDict(dict,delim):
    output = ""
    for key,value in dict.items(): #iteration
        if type(value) is not list: #selection
            output += (f"{key} {delim*10} {value}\n")
        else:
            val = ' , '.join(value) #sequencing
            output += (f"{key} {delim*10} {val}\n")
    return output #string output

```

## Calls to student procedure
```py
print(dispDict(options,"="))
```

```py
print(dispDict(data,"-"))
```

## Output

```py
data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
data = {books.loc[str(k),"isbn13"]:[books.loc[str(k),"title"],books.loc[str(k),"authors"].replace('/'," and ")] for k in list(data.keys())[:5]}
print(dispDict(data,"-"))
```