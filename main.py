from Services.LcdI2CWriter import LcdI2CWriter


lcd = LcdI2CWriter()
if __name__ == '__main__':   #Program entry
    lcd.Write("I Love You",1)
    lcd.Write("My Izolda",2)
