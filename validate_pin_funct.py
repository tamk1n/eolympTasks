def validate_pin(pin):
    try:
        intpin = int(pin)
        for x in pin:
            if type(int(x)) == int and (len(pin.strip()) == 4 or len(pin.strip())==6):
                return True
            else:
                return False
    except ValueError:
        return False 

