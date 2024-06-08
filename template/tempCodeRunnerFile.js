    // function onClickedEstimatePrice() {
    //   console.log("Estimate price button clicked");
    //   var sqft = document.getElementById("uiSqft");
    //   var bhk = getBHKValue();
    //   var bathrooms = getBathValue();
    //   var location = document.getElementById("uiLocations");
    //   var estPrice = document.getElementById("uiEstimatedPrice");
    
    //   var url = "http://127.0.0.1:5000/predict_home_price"; 
    //   $.post(url, {
    //       total_sqft: parseFloat(sqft.value),
    //       bhk: bhk,
    //       bath: bathrooms,
    //       location: location.value
    //   },function(data, status) {
    //       console.log(data.estimated_price);
    //       estPrice.innerHTML = "<h4>" + data.estimated_price.toString() + " Lakh</h4>";
    //       console.log(status);
    //   });
    // }