<script>
  import Route from '../components/Route.svelte';

  const user = JSON.parse(sessionStorage.getItem('user'));

  let routes = [
    {name: 'Some route', distance: '2.5km'},
    {name: 'Another one', distance: '99km'},
  ];

  function setHistory(data) {
    routes = [];
    for (index = 0; index < data["history"].length; index++) {
      current_history_route = data["history"][index];
      routes.push({
        name: current_history_route.name,
        distance: current_history_route.estimated_distance
      });
    }
  }

  onMount(() => {
    fetch($url('/loadhistory/' + user.name))
      .then(response => response.json())
      .then(data => setHistory(data));
  });
</script>

<style>
  a {
    display: block;
    img {
      padding: 1.5rem;
      width: 1rem;
    }
  }
  h1 {
    margin-top: 0;
  }
  main {
    max-width: 70rem;
    margin: 0 auto;
    padding: 0 2rem;
  }
</style>

<a href="/profile"><img src="/images/vector/back.svg" alt="Go back"/></a>
<main>
  <h1>History</h1>
  {#each routes as {name, distance}}
    <Route {name} {distance}/>
  {/each}
</main>
