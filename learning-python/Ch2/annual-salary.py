def SetAnnual():
  global annual
  annual=10000
def PrintMonthly():
  print("Your monthly payment is "+str(annual/12)+" USD.")
SetAnnual()
PrintMonthly()