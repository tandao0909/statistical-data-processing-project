import json
import os
import argparse

def convert_ipynb_to_text(ipynb_file, output_file):
    with open(ipynb_file, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    with open(output_file, 'w', encoding='utf-8') as f:
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown':
                f.write('\n')
                f.write(''.join(cell['source']))
                f.write('\n\n')
            elif cell['cell_type'] == 'code':
                f.write('\n```{r}\n')
                f.write(''.join(cell['source']))
                f.write('\n```\n\n')

def main():
    parser = argparse.ArgumentParser(description='Convert Jupyter Notebook to R Markdown')
    parser.add_argument('ipynb_file', help='Path to the Jupyter Notebook file')
    args = parser.parse_args()

    ipynb_file = args.ipynb_file
    notebook_name = os.path.splitext(os.path.basename(ipynb_file))[0]
    output_dir = 'jupyter_to_rmd'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{notebook_name}.rmd')

    convert_ipynb_to_text(ipynb_file, output_file)
    print(f'Converted {ipynb_file} to {output_file}')

if __name__ == '__main__':
    main()