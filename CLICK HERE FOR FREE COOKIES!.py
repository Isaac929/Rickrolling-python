import webbrowser
import time
import random

while True:
    sites = random.choice(['www.youtube.com/watch?v=AyOqGRjVtls', 'youtube.com/watch?v=dQw4w9WgXcQ', 'www.youtube.com/watch?v=w33zPsYhiCA'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 100)
    time.sleep(seconds)
