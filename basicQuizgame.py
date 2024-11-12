def getindex(option):
    index=["a","b","c","d"]
    if(option not in index):
        return -1
    return index.index(option)
def quizgame(quetions,options,answer):
    score=0
    initial=0
    while(initial!=len(quetions)):
        print("quetions: "+str((initial+1))+")"+ quetions[initial])
        print("options :\n"+options[initial])
        option=input("select the options :")
        value=getindex(option)
        if(value==-1):
            print()
            print("Please Enter the valid Option!")
            print()
            continue
        if(option==answer[initial]):
            print("congrates your answer is correct you got a point")
            score+=1
        else:
            print("your answer is wrong better luck next time")
        print("your answer:"+" "+options[initial].split(",")[value])
        print("correct answer:"+" "+options[initial].split(",")[getindex(answer[initial])])
        print()
        initial+=1
    print("total score you got:"+str(score*10)+"%"+" out of 100%")
    print()
quetions = [
          "What is the correct way to create a variable with the value 10 in Python?",
          "What is the output of the following code snippet?\nprint(type(5.5))",
          "Which of the following data types is mutable in Python?",
          "How do you start a comment in Python?",
          "What will be the output of the following code?\nprint(2 * 3 ** 2)",
          "How do you create a function in Python?",
          "What is the correct syntax for a for loop in Python?",
          "Which method can be used to convert a string to lowercase in Python?",
          "What will be the output of this code snippet?\nx = [1, 2, 3]\nprint(x[1])",
          "What keyword is used to handle exceptions in Python?"
        ]
options = [
          "A) int x = 10,\nB) x = 10,\nC) var x = 10,\nD) x := 10",
          "A) <class 'int'>,\nB) <class 'str'>,\nC) <class 'float'>,\nD) <class 'bool'>",
          "A) int,\nB) tuple,\nC) list,\nD) str",
          "A) //,\nB) #,\nC) /*,\nD) ;",
          "A) 18,\nB) 36,\nC) 25,\nD) 12",
          "A) function myFunction(),\nB) def myFunction(),\nC) create myFunction(),\nD) func myFunction()",
          "A) for (i = 0; i < 10; i++):,\nB) for i in range(10):,\nC) foreach i in range(10):,\nD) loop i in range(10):",
          "A) str.to_lower(),\nB) str.toLowerCase(),\nC) str.lower(),\nD) str.downcase()",
          "A) 1,\nB) 2,\nC) 3,\nD) IndexError,",
          "A) try...catch,\nB) handle...catch,\nC) try...except,\nD) try...finally"
]
answers = ["b", "c",  "c",  "b",  "a",  "b",  "b",  "c",  "b",  "c"  ]
quizgame(quetions,options,answers)