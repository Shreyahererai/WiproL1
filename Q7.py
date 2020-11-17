s = """Python is a widely used high-level programming langauage for general-purpose prograaming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to concpets in fewer lines of code than possible languages such as C++ or Java. The language provides constructs inteneded to enable writing clear programs on both a small scale and a large scale. Python featues a dynamic type system and sutomatic memory management and supports multiple programming paradgms,including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython , the reference implementation of Python, is opne source software and has a community-based development model, as do nearly all of its variant implementations. CPython os managed by the non-profit Python Software Foundation."""
s = s.lower()
low = s.split()
wordCounttable = {}
for word in low:
    if word not in wordCounttable.keys():
        wordCounttable[word] = 1
    else:
        wordCounttable[word] += 1
sorted(wordCounttable.items(), reverse=True)
s1 = list(wordCounttable.items())
print(s1)
def fun(t):
    return t[-1]
print(sorted (s1, key=fun, reverse= True)[:5])


