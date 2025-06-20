class Calculator:
  claculation_type = "Arithmetic Operations"
  @staticmethod
  def add(a,b):
    return f"The sum is: {a + b}"
  @classmethod
  def multiply(cls, a, b):
    print(f"Calculattion type: {cls.calculation_type}")
    return f"The product is: {a * b}"
