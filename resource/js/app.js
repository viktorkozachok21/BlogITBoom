window.addEventListener('load', function() {
  let long;
  let lat;
  let temperatureDescription = document.querySelector(".temperature-description");
  let temperatureDegree = document.querySelector(".temperature-degree");
  let locationTimezone = document.querySelector(".location-timezone");
  var songName = document.querySelector(".songName");

  if(navigator.geolocation){
    navigator.geolocation.getCurrentPosition(position => {
      long = position.coords.longitude;
      lat = position.coords.latitude;

      const proxy = 'https://cors-anywhere.herokuapp.com/';
      const api = proxy + 'https://api.darksky.net/forecast/3bd3d9cf3c41167bfcb0e25758510e88/' + lat + ',' + long + '?units=si';

      fetch(api)
        .then(response =>{
          return response.json();
        })
        .then(data =>{
          const { temperature, summary, icon } = data.currently;
          // Set DOM Elements from the api
          temperatureDegree.textContent = Math.floor(temperature);
          temperatureDescription.textContent = summary;
          locationTimezone.textContent = data.timezone;
          // Set Icon
          setIcons(icon, document.querySelector(".icon"));
        });
    });
  }

  function setIcons(icon, iconID) {
    const skycons = new Skycons({color: "white"});
    const currentIcon = icon.replace(/-/g, "_").toUpperCase();
    skycons.play();
    return skycons.set(iconID, Skycons[currentIcon]);
  }

});
