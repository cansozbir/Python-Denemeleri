class kareler:
    def __init__(self,maxsayi):
        self.sayi=0
        self.maxsayi=maxsayi
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.sayi<self.maxsayi:
            self.sayi += 1
        return self.sayi**2


iterator=iter(kareler(10))


print(next(iterator))
print(next(iterator))
print(next(iterator))
