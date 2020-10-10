sizeMultiplier = 1
for a in range(35 * sizeMultiplier):
      if((a * sizeMultiplier) < ((5 * sizeMultiplier) * sizeMultiplier) or ((a * sizeMultiplier) > ((8 * sizeMultiplier) * sizeMultiplier) and (a * sizeMultiplier) < ((14 * sizeMultiplier) * sizeMultiplier))):
        print("F" * 35 * sizeMultiplier)
      else:
        print("F" * 12 * sizeMultiplier)
