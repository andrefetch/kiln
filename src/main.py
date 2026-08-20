import os
import shutil


def copy_dir(src: str, dst: str) -> None:

    if not os.path.isdir(dst):
        os.mkdir(dst)

    for item in os.listdir(src):

        srcfull_path = os.path.join(src, item)
        dstfull_path = os.path.join(dst, item)

        if os.path.isfile(srcfull_path):
            print(f"Created File: {srcfull_path}")
            shutil.copy(srcfull_path, dstfull_path)

        if os.path.isdir(srcfull_path):
            print(f"Created Directory: {srcfull_path}")
            copy_dir(srcfull_path, dstfull_path)

def main():

    if os.path.exists("public"):
        shutil.rmtree("public")

    copy_dir("static", "public")

if __name__ == "__main__":

    main()
