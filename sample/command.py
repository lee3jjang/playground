import argparse
import sys

def hello(name):
    """이런게 가능한가요
    
    :param str name: name 값
    :return: 4가 나옵니다.

    Example
    -------
        >>> hello('sangjin')
        4
    """
    print(f"Hello, {name}")
    return 4

def notmain():
    """이건 왜 안되는 거져"""
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="이름입니다")
    parser.add_argument("-v", "--version", action="store_true", help="버전")
    parser.add_argument("-k", "--golive", action="store_true", help="say good bye")
    
    args = parser.parse_args()
    print(args.golive)
    print(args.version)
    # name = args.name
    # hello(name)
    # parser.print_help()

    # if args.version:
    #     print("1.0.0")
    #     sys.exit()