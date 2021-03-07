<script>
  import Route from '../components/Route.svelte';

  const routes = [
    {name: 'Some route', distance: '2.5km'},
    {name: 'Another one', distance: '99km'},
  ];
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
