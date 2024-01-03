/**
 * 
 */
function codigoCuentas() {
	var cuentasCatalogo = []
    accountNames.forEach(element => cuentasCatalogo.push(element[0]+"-"+element[1]))
  
    var select = document.getElementById("accounts1"); //Seleccionamos el select
    
    for(var i=1; i < cuentasCatalogo.length; i++){ 
        var option = document.createElement("option"); //Creamos la opcion
        option.innerHTML = cuentasCatalogo[i]; //Metemos el texto en la opción
        option.value=cuentasCatalogo[i];
        select.appendChild(option); //Metemos la opción en el select
    }
    
    var select = document.getElementById("accounts2"); //Seleccionamos el select
    
    for(var i=1; i < cuentasCatalogo.length; i++){ 
        var option = document.createElement("option"); //Creamos la opcion
        option.innerHTML = cuentasCatalogo[i]; //Metemos el texto en la opción
        option.value=cuentasCatalogo[i];
        select.appendChild(option); //Metemos la opción en el select
    }  
    
}
codigoCuentas();

function paises() {
   var countryList = []
    countryNames.forEach(element => countryList.push(element[0]+"-"+element[1]))					    
    
   var select = document.getElementById("pais"); //Seleccionamos el select
    
    for(var i=1; i < countryList.length; i++){ 
        var option = document.createElement("option"); //Creamos la opcion
        option.innerHTML = countryList[i]; //Metemos el texto en la opción
        option.value=countryList[i];
        select.appendChild(option); //Metemos la opción en el select
    }
    
  }
paises();

function cities() {
	var cityList = []
    cityNames.forEach(element => cityList.push(element[0]+"-"+element[1]))				    
    
   var select = document.getElementById("city"); //Seleccionamos el select
    
    for(var i=1; i < cityList.length; i++){ 
        var option = document.createElement("option"); //Creamos la opcion
        option.innerHTML = cityList[i]; //Metemos el texto en la opción
        option.value=cityList[i];
        select.appendChild(option); //Metemos la opción en el select
    }
    
   
}
cities();

function cuotas() {
	var cuotaList = [ "0 0","1","2","3",];				    
	var cuota = document.getElementById("cuotasCheck"); //Seleccionamos el select
    
	var select = document.getElementById("cuotaSelect"); //Seleccionamos el select
  
   	if (cuota.checked) {
	    select.style.display='block';
		for(var i=1; i < cuotaList.length; i++){ 
			var option = document.createElement("option"); //Creamos la opcion
			option.innerHTML = cuotaList[i]; //Metemos el texto en la opción
			option.value=cuotaSelect[i];
			select.appendChild(option); //Metemos la opción en el select		
		}

	}else{
		select.style.display='none';
		for(var i=1; i < cuotaList.length; i++){ 	
			select.removeChild(option); //Metemos la opción en el select		
		}	
	}
}
cuotas();

function viajes() {
	var viajesList = [ " 0 0","1 UNAHUR","2 IFTS","3 UBA", "4 UPE","5 Bs As","6 AMBA" ];				    
    var viaje = document.getElementById("actividad1"); //Seleccionamos el select
	var viaje2 = viaje.options[viaje.selectedIndex].value;
	var select = document.getElementById("viajeSelect"); //Seleccionamos el select
	
   	if (viaje2==3) {   
	    select.style.display='block';
		document.getElementById("medio1").value=36
	}

}
viajes();

function precios() {
		var price1 = document.getElementById("viajeSelect");
		var price2 = price1.options[price1.selectedIndex].value;
		switch (price2) {
			case "1":
				document.getElementById("feeQuickInsert1").value = 120;
				break;
			case "2":
				document.getElementById("feeQuickInsert1").value = 180;
				break;
			case "3":
				document.getElementById("feeQuickInsert1").value = 120;
				break;
			case "4":
				document.getElementById("feeQuickInsert1").value = 227;
				break;
			case "5":
				document.getElementById("feeQuickInsert1").value = 106;
				break;
			case "6":
				document.getElementById("feeQuickInsert1").value = 150;
				break;
		}

}

precios()


function sChange() {					    
    
	document.getElementById("dateForm2").value = document.getElementById("dateForm").value
	document.getElementById("feeForm2").value = document.getElementById("feeForm").value	
	
}
sChange();

document.addEventListener('DOMContentLoaded', function(){
    let formulario = document.getElementById('form1');
    formulario.addEventListener('submit', function() {
      formulario.reset();
    });
  });



function genPDF(){
	windows.print();
	}
	
document.getElementById("pdfas").addEventListener('click',genPDF);
