document.addEventListener("DOMContentLoaded", function () {
  const fromCurrencyInput = document.getElementById("from_currency_input");
  const toCurrencyInput = document.getElementById("to_currency_input");
  const fromCurrencySelect = document.getElementById("from_currency");
  const toCurrencySelect = document.getElementById("to_currency");

  const createDropdownList = (selectElement, inputElement) => {
    const dropdownList = document.createElement("div");
    dropdownList.classList.add("dropdown-list");
    inputElement.parentElement.appendChild(dropdownList);

    // Populate dropdown list with options
    Array.from(selectElement.options).forEach((option) => {
      const item = document.createElement("div");
      item.textContent = option.textContent;
      item.dataset.value = option.value;
      item.addEventListener("click", function () {
        inputElement.value = this.textContent;
        selectElement.value = this.dataset.value;
        dropdownList.style.display = "none";
      });
      dropdownList.appendChild(item);
    });

    return dropdownList;
  };

  const updateDropdownList = (inputElement, dropdownList) => {
    const filter = inputElement.value.toLowerCase();
    dropdownList.querySelectorAll("div").forEach((item) => {
      if (item.textContent.toLowerCase().includes(filter)) {
        item.style.display = "";
      } else {
        item.style.display = "none";
      }
    });
    dropdownList.style.display = filter ? "block" : "none";

    // Adjust position of dropdown list
    const rect = inputElement.getBoundingClientRect();
    dropdownList.style.top = `${rect.top + window.scrollY - 35}px`;
    // dropdownList.style.left = `${rect.left + window.scrollX}px`;
    dropdownList.style.width = `${inputElement.offsetWidth}px`; // Ensure dropdown matches input width
  };

  const fromDropdownList = createDropdownList(
    fromCurrencySelect,
    fromCurrencyInput
  );
  const toDropdownList = createDropdownList(toCurrencySelect, toCurrencyInput);

  fromCurrencyInput.addEventListener("input", () =>
    updateDropdownList(fromCurrencyInput, fromDropdownList)
  );
  toCurrencyInput.addEventListener("input", () =>
    updateDropdownList(toCurrencyInput, toDropdownList)
  );

  // Hide dropdown when clicking outside
  document.addEventListener("click", (event) => {
    if (
      !fromCurrencyInput.contains(event.target) &&
      !fromDropdownList.contains(event.target)
    ) {
      fromDropdownList.style.display = "none";
    }
    if (
      !toCurrencyInput.contains(event.target) &&
      !toDropdownList.contains(event.target)
    ) {
      toDropdownList.style.display = "none";
    }
  });
});
