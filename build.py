import os
import zipfile

def build_scs_mod(source_dir, output_filename):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print("Error: Source directory '" + source_dir + "' not found.")
        return

    print("Building Mod: " + output_filename)
    
    # Open zip file with ZIP_STORED (0 compression level), crucial for SCS games
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_STORED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate relative path to ensure 'def' is at the root of the zip
                rel_path = os.path.relpath(file_path, source_dir)
                
                print("  Adding: " + rel_path)
                zipf.write(file_path, arcname=rel_path)
                
    print("Build Complete! File saved as: " + output_filename)

if __name__ == "__main__":
    # Define directories and output name
    SRC_FOLDER = "src"
    OUTPUT_FILE = "GT6Speed.scs"
    
    build_scs_mod(SRC_FOLDER, OUTPUT_FILE)