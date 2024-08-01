from __future__ import print_function
import six
import argparse

def greet(name):
    if isinstance(name, six.binary_type):
        name = name.decode('utf-8')
    print("Hello, {}!".format(name))

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Tool")
    parser.add_argument('name', help="Name of the person to greet")
    args = parser.parse_args()
    
    greet(args.name)

if __name__ == "__main__":
    main()