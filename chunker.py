def chunker(iterable, size):
    for var in range(0,len(iterable),size):
        yield iterable[var:var+size]
    
    
for chunk in chunker(range(25), 4):
    print(list(chunk))