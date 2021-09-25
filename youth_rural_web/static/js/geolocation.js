const successfulLookup = position => {
 const { latitude, longitude } = position.coords;
 fetch(`https://api.opencagedata.com/geocode/v1/json?q=${latitude}+${longitude}&key=1234`)
   .then(response => response.json())
   .then(console.log); 
}
if (window.navigator.geolocation) {
    // Geolocation available
    window.navigator.geolocation.getCurrentPosition(console.log, console.log);
    window.navigator.geolocation
  .getCurrentPosition(successfulLookup, console.log);


    console.log()
   } 

