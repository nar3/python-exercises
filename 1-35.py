liter_used=float(input('liter used ? '))
mile_drived=float(input('mile drived? '))
liter_to_galon=lambda x:x*0.264179
print(liter_to_galon(liter_used)/mile_drived,' galon per mile')