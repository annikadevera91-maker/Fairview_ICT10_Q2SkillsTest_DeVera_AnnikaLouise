from pyscript import document

# Python dictionary storing non-metal elements information
non_metals = {
    "H": ("Hydrogen", 1, "1.008"),
    "C": ("Carbon", 6, "12.011"),
    "N": ("Nitrogen", 7, "14.007"),
    "O": ("Oxygen", 8, "15.999"),
    "F": ("Fluorine", 9, "18.998"),
    "P": ("Phosphorus", 15, "30.974"),
    "S": ("Sulfur", 16, "32.06"),
    "Cl": ("Chlorine", 17, "35.45"),
    "Se": ("Selenium", 34, "78.971"),
    "Br": ("Bromine", 35, "79.904"),
    "I": ("Iodine", 53, "126.90"),
    "At": ("Astatine", 85, "210"),
    "He": ("Helium", 2, "4.0026"),
    "Ne": ("Neon", 10, "20.180"),
    "Ar": ("Argon", 18, "39.95"),
    "Kr": ("Krypton", 36, "83.80"),
    "Xe": ("Xenon", 54, "131.29"),
    "Rn": ("Radon", 86, "222"),
}


def search_element(event):
  # Get the input value from the text box
  element_input = document.getElementById("element-code").value.strip()

  # Format the symbol to match dictionary capitalization rules
  if len(element_input) == 2:
    formatted_symbol = element_input.capitalize()
  elif len(element_input) == 1:
    formatted_symbol = element_input.upper()
  else:
    formatted_symbol = element_input

  # Retrieve information using the dictionary
  result = non_metals.get(formatted_symbol, ("Element not found", "-", "-"))

  # Display the results in the HTML span elements
  if result[0] == "Element not found":
    document.getElementById("symbol").innerText = (
        element_input if element_input else "-"
    )
    document.getElementById("name").innerText = "Element not found"
    document.getElementById("atomic_number").innerText = "-"
    document.getElementById("atomic_mass").innerText = "-"
  else:
    document.getElementById("symbol").innerText = formatted_symbol
    document.getElementById("name").innerText = str(result[0])
    document.getElementById("atomic_number").innerText = str(result[1])
    document.getElementById("atomic_mass").innerText = str(result[2])