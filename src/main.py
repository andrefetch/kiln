import os
import shutil
import sys

from src.markdown.block_markdown import markdown_to_html_node


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

def extract_title(markdown: str) -> str:

    lines = markdown.split('\n')

    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()

    raise Exception(
        "There must be an <h1> tag"
    )

def generate_page(from_path, template_path, dest_path, basepath="/"):

    if os.path.isdir(from_path):

        for item in os.listdir(from_path):

            srcfull_path = os.path.join(from_path, item)
            dstfull_path = os.path.join(dest_path, item)

            if os.path.isdir(srcfull_path):
                generate_page(srcfull_path, template_path, dstfull_path, basepath)

            elif item.endswith(".md"):
                generate_page(srcfull_path, template_path, dstfull_path[:-3] + ".html", basepath)

        return

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        md_content = f.read()

    with open(template_path, 'r') as f:
        template_path_content = f.read()

    html_string = markdown_to_html_node(md_content).to_html()
    extracted_title = extract_title(md_content)

    replaced_title = template_path_content.replace("{{ Title }}", extracted_title)
    replaced_content = replaced_title.replace("{{ Content }}", html_string)

    replaced_content = replaced_content.replace('href="/', f'href="{basepath}')
    replaced_content = replaced_content.replace('src="/', f'src="{basepath}')

    dir_name = os.path.dirname(dest_path)
    os.makedirs(dir_name, exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(replaced_content)



def main():

    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    if os.path.exists("docs"):
        shutil.rmtree("docs")

    copy_dir("static", "docs")
    generate_page("content", "template.html", "docs", basepath)

if __name__ == "__main__":

    main()
