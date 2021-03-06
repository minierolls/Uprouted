<script>
    import mapboxgl from 'mapbox-gl';
    import { onMount } from 'svelte';

    let mapContainer;
    
    onMount(async () => {
      const map = new mapboxgl.Map({
        container: mapContainer,
        style: 'mapbox://styles/mapbox/streets-v11',
        accessToken: 'pk.eyJ1IjoiYWlzNzYiLCJhIjoiY2tseDNiMHM4MDB5eTJ2cnM0YnZsdTQ0cSJ9.o3Bh8gznViclDtI-zg6t5g'
      });
	});
</script>

<style>
  #map {
    height: 100vh;
  }
  main {
    z-index: 1;
    position: relative;
  }
  h1 {
    margin: 1rem;
    background-color: white;
    position: absolute;
    border-radius: 1rem;
    padding: 0.25em 0.5em;
    box-shadow: 0px 0px 14px 1px rgba(0,0,0,0.2);
  }
</style>

<main>
  <h1>Hello. Please run</h1>
</main>
<div id="map" bind:this={mapContainer}></div>

