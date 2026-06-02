import os
import re

def clean_id(text):
    text = re.sub(r'[^a-z0-9\s_-]', '', text.lower())
    return re.sub(r'[\s_-]+', '_', text).strip('_')

def get_max_page(folder_path):
    pages = []
    for f in os.listdir(folder_path):
        name_part = os.path.splitext(f)[0]
        if name_part.isdigit():
            pages.append(int(name_part))
    return max(pages) if pages else 0

def main():
    root = input("Please put your comic's folder path here: ").strip('"').strip("'")
    author = input("Enter the author name: ")

    series_title = os.path.basename(root)
    entries = []

    for issue_dir in os.listdir(root):
        issue_path = os.path.join(root, issue_dir)
        if not os.path.isdir(issue_path): continue
        
        max_p = get_max_page(issue_path)
        swep_id = f"comic_{clean_id(series_title)}_{clean_id(issue_dir)}"
        lua_path = f"comics/{series_title.lower()}/{issue_dir.lower()}"
        
        entry = f'    AddComic("{swep_id}", {{\n        title = "{series_title}",\n        issue = "{issue_dir}",\n        author = "{author}",\n        icon = "{lua_path}/0.jpg",\n        pages = BuildPages("{lua_path}", {max_p})\n    }})'
        entries.append(entry)

    script = 'COMICS_DATABASE = COMICS_DATABASE or {}\n\nlocal function RegisterComics()\n    if not BuildPages then\n        hook.Add("Initialize", "RegisterComics_Retry_" .. debug.getinfo(1, "S").short_src, RegisterComics)\n        return\n    end\n    local function AddComic(id, data)\n        COMICS_DATABASE[id] = data\n    end\n\n' + "\n\n".join(entries) + '\nend\nRegisterComics()'
    
    print("\n--- Generated Script\n")
    print(script)
    
    try:
        import pyperclip
        pyperclip.copy(script)
        print("\n--- ")
        print("\nScript copied to clipboard.")
    except:
        print("\npyperclip not installed, copy the output manually.")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
