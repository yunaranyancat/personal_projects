def addTags(*tags):
    def decorator(oldFunc):
        def inside(*args, **kwargs):
            code = oldFunc(*args, **kwargs)
            for tag in reversed(tags):
                code = "<{0}>{1}</{0}>".format(tag,code)
            return code
        return inside
    return decorator

@addTags("p","i","b")
def myWebpage(name):
    return "Welcome "+name+" To my blog!"

print(myWebpage("Yunaranyancat"))
