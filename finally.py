import pickle

def displayrec():
    try:
        f = open("story.dat", "rb")
        while True:
            try:
                d = pickle.load(f)
                print(d)
            except EOFError:
                break
    except FileNotFoundError:
        print("File not found!")
    finally:
        f.close()

displayrec()
