"""
Student Name: Dan Shaw w0190983
Program Name: Hipster's Local Vinyl Records
Program Description: Hipster's Local Vinyl Records sell and hand-deliver vinyl records to their customers.
"""

RATE_PER_KM = 15
TAX_RATE = 0.14

def main():
    global RATE_PER_KM
    global TAX_RATE

    greeting = "HIPSTER'S LOCAL VINYL RECORDS DELIVERY SERVICE"

    # Output greeting and instructions
    print(greeting)
    print("-" * len(greeting))

    # Get name from user
    customerName = input("Enter the name of the customer: ")

    # Get travel distance from user, validate it as a number
    deliveryDistance = getDeliveryDistance()
    while validateFloat(deliveryDistance) == 0:
        deliveryDistance = getDeliveryDistance()
    
    # Once deliveryDistance has been validated as a number, convert it to a float
    deliveryDistance = float(deliveryDistance)

    # Get sub-total of bill (record prices only), validate it as a number
    billSubtotal = getBillSubtotal()
    while validateFloat(billSubtotal) == 0:
        billSubtotal = getBillSubtotal()

    # Once billSubtotal has been validated as a number, convert it to a float
    billSubtotal = float(billSubtotal)

    # Perform calculations
    deliveryCost = RATE_PER_KM * deliveryDistance
    taxCost = TAX_RATE * billSubtotal
    billTotal = billSubtotal + deliveryCost + taxCost

    # Display customer name
    # Display calculation results: delivery cost, bill with tax, and total charge to customer
    print("-" * len(greeting))
    print("""Summary of purchase for bill in the name of: {0}
        Delivery Cost: ${1:.2f} for {2:.1f} kilometres
        Purchase Cost: ${3:.2f}
        Tax Rate: {4:.1f}%
        Subtotal: ${5:.2f}
        Total Charge: ${6:.2f}""".format(customerName, deliveryCost, deliveryDistance, billSubtotal, TAX_RATE * 100, billSubtotal + taxCost, billTotal))
    print("-" * len(greeting))

def getDeliveryDistance():
    return input("Enter the delivery distance in Kilometres: ")

def getBillSubtotal():
    return input("Enter the cost of records purchased: ")

# Validates whether inputQuery is a valid number by trying to convert to a float
def validateFloat(inputQuery):
    try:
        float(inputQuery)
        return 1
    except:
        errorString = "Please enter a valid number"
        print("-" * len(errorString))
        print(errorString)
        print("-" * len(errorString))
        return 0

if __name__ == "__main__":
    main()