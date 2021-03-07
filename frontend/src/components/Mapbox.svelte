<script>
  import mapboxgl from 'mapbox-gl';
  import { onMount } from 'svelte';

  export let route;

  let mapContainer;

  onMount(async () => {
    const map = new mapboxgl.Map({
      container: mapContainer,
      style: 'mapbox://styles/mapbox/streets-v11',
      accessToken: 'pk.eyJ1IjoiYWlzNzYiLCJhIjoiY2tseDNiMHM4MDB5eTJ2cnM0YnZsdTQ0cSJ9.o3Bh8gznViclDtI-zg6t5g',
      zoom: 12,
      center: route.coordinates[0],
      attributionControl: false
    });
    map.on('load', () => {
      map.addSource('route', {
        'type': 'geojson',
        'data': route,
      });
      map.addLayer({
          'id': 'route',
          'type': 'line',
          'source': 'route',
          'layout': {
            'line-join': 'round',
            'line-cap': 'round'
          },
          'paint': {
            'line-color': '#F4A261',
            'line-width': 4
          }
      });
    });
  });
</script>

<style>
  #map {
    height: 100vh;
  }
</style>

<div id="map" bind:this={mapContainer}></div>
