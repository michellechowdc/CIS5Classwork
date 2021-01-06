piVal = 3.14
userRadius = int(input ("\nEnter a radius value: "))

print("\nA circle with radius %d has a(n)" %(userRadius))
print(f"   AREA of {piVal * userRadius**2}")
print(f"   CIRCUMFERENCE of {2 * piVal * userRadius}")

print("\nA sphere with radius %d has a(n)" %(userRadius))
print(f"   VOLUME of {(4 * piVal * userRadius**3) / 3}")
print(f"   SURFACE AREA of {4 * piVal * userRadius**2}\n")
