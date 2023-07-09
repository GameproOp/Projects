def car_discount(base_price, add_on_services):
  """
  Calculates the discount for a car purchase, given the base price and add-on services.

  Args:
    base_price: The base price of the car.
    add_on_services: A list of add-on services.

  Returns:
    The discount for the car purchase.
  """

  discount = 0
  for add_on_service in add_on_services:
    if add_on_service == "warranty":
      discount += 500
    elif add_on_service == "extended_service_plan":
      discount += 200
    elif add_on_service == "car_seats":
      discount += 100

  return discount

def main():
  """
  The main function of the program.
  """

  base_price = 20000
  add_on_services = ["warranty", "extended_service_plan", "car_seats"]

  discount = car_discount(base_price, add_on_services)

  print("The discount for the car purchase is $", discount)

if __name__ == "__main__":
  main()
