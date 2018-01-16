def later():
    import sys
    print("Bye sys world")
    sys.exit(42)
    print("never reach")

if __name__ == "__main__":
    later()
