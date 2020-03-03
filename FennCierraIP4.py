def main():
    validateUserInput1to7= int(input("Enter a number 1 through 7 "))

def validateUserInput1to7():
    while validateUserInput1to7 <= 7:
        print(printWelcome)
        if validateUserInput1to7 > 7:
            print("Please quit and enter number 1 through 7")


N= validateUserInput1to7                     
def printWelcome():
    while n == 1:
        print("PET is intended for single use. Reusing increases the risk of carcinogen leaching and bacterial growth. PET is difficult to decontaminate. Recycle but don’t reuse.")
    while n == 2:
        print("HDPE is one of the safest forms of plastic. Resistant to heat and cold. Can be reused and recycled.")
    while n == 3:
        print("PVC is relatively impervious to sunlight and weather. It contains numerous toxins that can leach throughout the lifecycle of the plastic. Cannot be recycled. Can be reused.")
    while n == 4:
        print("LDPE is relatively safe for use. Reusable but not always recyclable.")
    while n == 5:
        print("PP is heat-resistant and acts as a barrier against moisture, grease, and chemicals. Can be reused and recycled.")
    while n == 6:
        print("PS is inexpensive and lightweight. Leaches carcinogens and breaks up easily. Low market for recycling and difficult to reuse. Should be avoided.")
    while n == 7:
        print("PC and “other” plastics. These vary which is confusing for consumers. Because of concerns with carcinogen leaching, avoid these unless it also contains the letters PLA or Compostable. These are made from bio-based polymers that can be composted.")
        

printWelcome()
main()

