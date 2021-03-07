<script>
  import { goto } from '@roxi/routify';
  function setSession() {
    const Einstein = {
      name: 'Albert Einstein',
      picture: '/images/einstein.jpg',
      friends: [
        { name: 'Marie Curie', picture: '/images/curie.jpg' },
        { name: 'Stephen Hawking', picture: '/images/hawking.jpg' },
      ]
    }
    sessionStorage.setItem('user', JSON.stringify(Einstein));
    $goto('/welcome');
  }
</script>

<style>
  main {
    padding: 0 1rem;
  }
</style>

<main>
  <h1>User log in</h1>
  <p>Are we doing this through google or what?</p>
  <p>Anyway, for now, just click the button below to make yourself Einstein</p>
  <button on:click={setSession}>Make me Einstein!</button>
</main>
