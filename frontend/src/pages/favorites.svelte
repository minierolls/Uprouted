<script>
  import Route from '../components/Route.svelte';
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

<a href="/profile"><img src="/images/vector/back.svg"/></a>
<main>
  <h1>Favorites</h1>
  <Route name="Some route" distance="2.5km"/>
  <Route name="This one sucked" distance="0km"/>
</main>
