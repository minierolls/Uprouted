<script>
    import mapboxgl from 'mapbox-gl';
    import { onMount, onDestroy } from 'svelte';

    const user = JSON.parse(sessionStorage.getItem('user'));

    let mapContainer;
    let startTime;
    let paused = true;
    let pauseTime = Date.now();
    let interval;

    // just fill this in with actual route info I guess
    let route = {
      name: 'Wow a route',
      elapsed: 0,
      distance: 0,
    }
    
    onMount(async () => {
      startTime = new Date();
      const map = new mapboxgl.Map({
        container: mapContainer,
        style: 'mapbox://styles/mapbox/streets-v11',
        accessToken: 'pk.eyJ1IjoiYWlzNzYiLCJhIjoiY2tseDNiMHM4MDB5eTJ2cnM0YnZsdTQ0cSJ9.o3Bh8gznViclDtI-zg6t5g',
        attributionControl: false
      });
      interval = setInterval(() => {
        if (!paused) {
          route.elapsed = Date.now() - startTime;
        }
      }, 1000);
	});
    function prettyTime(ms) {
      let secs = ms / 1000;
      ms = Math.floor(ms % 1000);
      let minutes = secs / 60;
      secs = Math.floor(secs % 60).toString().padStart(2, '0');
      let hours = minutes / 60;
      minutes = Math.floor(minutes % 60).toString().padStart(2, '0');
      hours = Math.floor(hours % 24).toString().padStart(2, '0');
      return hours + ":" + minutes + ":" + secs;  
    }
    function togglePaused() {
      if (paused) {
        startTime = new Date(startTime.getTime() + (Date.now() - pauseTime));
        paused = false;
      } else {
        pauseTime = Date.now();
        paused = true;
      }
    }
    onDestroy(() => {
      clearInterval(interval);
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
  #top {
    position: absolute;
    background-color: $jade;
    width: 100%;
    color: white;
    border-radius: 0 0 $radius $radius;
    padding: 0.5rem 1rem;
    box-sizing: border-box;
    display: grid;
    grid-template-columns: auto 1fr;
    grid-gap: 1rem;
    box-shadow: $shadow;
    a {
      justify-self: end;
      align-self: center;
      img {
        max-height: 4rem;
        border-radius: $radius;
      }
    }
  }
  #info {
    position: fixed;
    bottom: 0;
    background-color: white;
    margin: 1rem;
    border-radius: $radius;
    width: calc(100% - 2rem);
    box-sizing: border-box;
    display: grid;
    grid-template-columns: auto auto;
    padding-top: 1.5rem;
    box-shadow: $shadow;
    p {
      text-align: center;
      font-size: 24px;
    }
    #controls {
      position: absolute;
      top: -2.5rem;
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      width: 100%;
      max-width: 20rem;
      margin: 0 auto;
      box-sizing: border-box;
      left: 50%;
      transform: translateX(-50%);
      place-items: center;
      .circle {
        box-shadow: $shadow;
        border-radius: 50%;
        border: 5px solid $orange;
        width: 3.5rem;
        background-color: white;
        height: 3.5rem;
        display: flex;
        justify-content: center;
        align-items: center;
        img {
          width: 2.25rem;
          height: 2.25rem;
        }
      }
      #pause {
        box-shadow: $shadow;
        cursor: pointer;
        width: 5rem;
        height: 5rem;
        background-color: $orange;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        img {
          width: 2.5rem;
          height: 2.5rem;
        }
      }
    }
  }
</style>

<main>
  <div id="top">
    <h1>{route.name}</h1>
    <a href="/profile"><img src={user.picture} alt={user.name}></a>
  </div>
  <div id="info">
    <p id="time">{prettyTime(route.elapsed)}</p>
    <p id="distance">{route.distance + 'km'}</p>
    <div id="controls">
      <div id="restart" class="circle">
        <img src="/images/vector/redo.svg"/>
      </div>
      <div id="pause" on:click={togglePaused}>
        {#if paused}
          <img src="/images/vector/play.svg"/>
        {:else}
          <img src="/images/vector/pause.svg"/>
        {/if}
      </div>
      <a id="check" class="circle" href="/welcome">
        <img src="/images/vector/check.svg"/>
      </a>
    </div>
  </div>
</main>
<div id="map" bind:this={mapContainer}></div>

