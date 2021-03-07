<script>
  import Mapbox from '../components/Mapbox.svelte';
  import { onMount, onDestroy } from 'svelte';

  const user = JSON.parse(sessionStorage.getItem('user'));

  let startTime;
  let paused = true;
  let pauseTime = Date.now();
  let interval;
  let started = false;

  const geojson = JSON.parse(sessionStorage.getItem("current_route"));
  const e_d = sessionStorage.getItem("estimated_distance");
  const e_t = sessionStorage.getItem("estimated_time");
  const route_name = 'Wow a route';

  let route = {
    name: route_name,
    elapsed: 0,
    distance: 0,
    route: geojson,
    estimated_distance: e_d,
    estimated_time: String(parseInt(e_t, 10)) + "min"
  };

  onMount(async () => {
    startTime = new Date();
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
    started = true;
    if (paused) {
      startTime = new Date(startTime.getTime() + (Date.now() - pauseTime));
      paused = false;
    } else {
      pauseTime = Date.now();
      paused = true;
    }
  }
  function saveRoute() {
    let save_route_info = {
      user: user.name,
      name: route_name,
      route: geojson,
      estimated_distance: e_d,
      estimated_time: e_t
    };
    fetch($url('/saveroute'), { method: 'POST', body: save_route_info });
  }
  onDestroy(() => {
    clearInterval(interval);
  });
</script>

<style>
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
      display: flex;
      justify-content: space-evenly;
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
    <p id="time">
      {#if started}
        {prettyTime(route.elapsed)}
      {:else}
        {route.estimated_time}
      {/if}
    </p>
    <p id="distance">
      {#if started}
        {route.distance + 'km'}
      {:else}
        {route.estimated_distance + 'km'}
      {/if}
    </p>
    <div id="controls">
      {#if started}
        <div id="restart" class="circle">
          <img src="/images/vector/redo.svg" alt="Redo"/>
        </div>
      {/if}
      <div id="pause" on:click={togglePaused}>
        {#if paused}
          <img src="/images/vector/play.svg" alt="Start"/>
        {:else}
          <img src="/images/vector/pause.svg" alt="Pause"/>
        {/if}
      </div>
      {#if started}
        <a id="check" class="circle" href="/welcome" on:click={saveRoute}>
          <img src="/images/vector/check.svg" alt="Complete"/>
        </a>
      {/if}
    </div>
  </div>
</main>
<Mapbox route={route.route} />

