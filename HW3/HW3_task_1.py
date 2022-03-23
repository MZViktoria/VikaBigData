# cache function
def cache(times):
    def mind(func):
        def memory():
            memory.count += 1  # its for track how many times func was requested
            if memory.count == 1 or memory.count > times + 1:  # start and end
                memory.x = func()
                memory.count = 1  # we enter the [if] when count = 1(start) and count = times+1(end)
                # for reset the counter we use this string
            else:
                print(memory.x)

        # defining variables
        memory.x = ''
        memory.count = 0
        return memory

    return mind


@cache(times=3)  # u can change times if u want
def f():
    return input('? ')


f()
f()
f()
f()
f()
f()
f()
f()
f()
f()