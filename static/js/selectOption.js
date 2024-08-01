function populateSelect(selectId, optionsArray) {
    const selectElement = document.getElementById(selectId); //Seleccionamos el select

    // Limpiar las opciones existentes
    selectElement.innerHTML = '';

    optionsArray.forEach(optionText => {
        const option = document.createElement("option"); //Creamos la opcion
        option.innerHTML = optionText; //Metemos el texto en la opción
        option.value = optionText;
        selectElement.appendChild(option);
    });
}

// Carga codigo cuentas en el selector
function codigoCuentas() {
    var cuentasCatalogo = accountNames.map(element => `${element[0]}-${element[1]}`);
    populateSelect("accounts1", cuentasCatalogo);
    populateSelect("accounts2", cuentasCatalogo);
}

// Carga paises en el selector
function paises() {
    var countryList = countryNames.map(element => `${element[0]}-${element[1]}`);
    populateSelect("pais", countryList);
}

// Carga ciudades en el selector
function cities() {
    var cityList = cityNames.map(element => `${element[0]}-${element[1]}`);
    populateSelect("city", cityList);
}


function viajes() {
    var viaje = document.getElementById("actividad1");
    var viaje2 = viaje.options[viaje.selectedIndex].value;
    var select = document.getElementById("viajeSelect"); // Seleccionamos el select

    if (viaje2 == 3) {
        select.style.display = 'block';
        document.getElementById("medio1").value = 36;
    }
}

function precios() {
    var price1 = document.getElementById("viajeSelect");
    var price2 = price1.options[price1.selectedIndex].value;
    var priceValues = {
        "1": 120,
        "2": 180,
        "3": 120,
        "4": 227,
        "5": 106,
        "6": 150
    };

    document.getElementById("feeQuickInsert1").value = priceValues[price2] || 0;
}

function sChange() {
    document.getElementById("dateForm2").value = document.getElementById("dateForm").value;
    document.getElementById("feeForm2").value = document.getElementById("feeForm").value;
}

// Llamada inicial para llenar los selects y otros elementos
codigoCuentas();
paises();
cities();
viajes();
precios();
sChange();


