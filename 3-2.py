def entry():
    global foot, inch
    foot = float(input("enter length to foot: "))
    inch = float(input("enter length to inch: "))


def calc():
    global ft_mt, ft_cm, inch_mt, inch_cm
    ft_mt = foot * 0.3048
    ft_cm = foot * 30.48
    inch_mt = (inch / 12) * 0.3048
    inch_cm = (inch / 12) * 30.48


def disp():
    print("%f foot= %f meter " % (foot, ft_mt))
    print("%f foot= %f CentiMeter " % (foot, ft_cm))
    print("%f inch= %f meter " % (inch, ft_mt))
    print("%f inch= %2f CentiMeter " % (inch, inch_cm))


def main():
    entry()
    calc()
    disp()


main()