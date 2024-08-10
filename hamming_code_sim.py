def correctCode(info):
    if len(info)!=16:
        raise Exception("Error")
        
    msg = info[1:-4]
    parity_checks = info[-4:]
    even_check = info[0]
    
    new_parity = 0
    for i in range(1,len(msg)):
        if msg[i-1] == "1":
            new_parity ^= i
    
    error_loc = new_parity ^ parity_checks
    
    # no error
    if error_loc == 0:
        return msg
    
    msg[error_loc-1] = 1 - msg[error_loc-1]
    
        
        