from typing import List

from executor._decorator import executor


@executor()
def ls(folder: str) -> List[str]:
    return ["ls", folder]


def main():
    result = ls(".")
    print(result)


if __name__ == "__main__":
    main()
