import pandas as pd
from scipy import spatial
books = pd.read_csv("data/books.csv")
books.set_index("bookID",inplace=True)
def dispDict(dict,delim):
    output = ""
    for key,value in dict.items():
        if type(value) is not list:
            output += (f"{key} {delim*10} {value}\n")
        else:
            val = ' , '.join(value)
            output += (f"{key} {delim*10} {val}\n")
    return output
userSelection = input("What is a book you have recently read and liked? ")
options = {}
for x in range(len(books)):
    try:
        book = books.loc[str(x),"title"]
        if userSelection.lower() in book.lower():
            options[x] = book
    except:
        continue
if len(options) > 1:
    print(dispDict(options,"="))
    selection = int(input("Which of these is your selection? "))
    while selection not in options:
        selection = int(input("Which of these is your selection? "))
    finalSelection = [str(selection),options[selection],books.loc[str(selection),"  num_pages"]]
elif len(options) ==0:
    print("Sorry, we have nothing for that book. ")
    quit()
else:
    finalSelection = [str(list(options.keys())[0]),list(options.values())[0],books.loc[str(list(options.keys())[0]),"  num_pages"]]
user_authors = books.loc[finalSelection[0],"authors"].split('/')
data = {}
for x in range(len(books)):
    if str(x) == finalSelection[0]:
        continue
    try:
        numRatings = books.loc[str(x),"ratings_count"]
        if numRatings < 3000:
            continue
        authors = books.loc[str(x),"authors"].split('/')
        commonAuthors = len(list(set(authors).intersection(user_authors)))
        pages = books.loc[str(x),"  num_pages"]
        rating = books.loc[str(x),"average_rating"]
        data[x] = spatial.distance.cosine([commonAuthors,pages,rating],[len(user_authors),finalSelection[2],5])

    except:
        continue

data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
data = {books.loc[str(k),"isbn13"]:[books.loc[str(k),"title"],books.loc[str(k),"authors"].replace('/'," and ")] for k in list(data.keys())[:5]}
print(dispDict(data,"-"))