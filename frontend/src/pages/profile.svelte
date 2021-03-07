<script>
  import Friend from '../components/Friend.svelte';

  const user = JSON.parse(sessionStorage.getItem('user'));
</script>

<style>
  main {
    max-width: 80rem;
    margin: 0 auto;
  }
  img {
    display: block;
  }
  #picture {
    #nav {
      padding: 2rem;
      display: flex;
      justify-content: flex-end;
    }
    #profile-pic {
      width: 10rem;
      height: 10rem;
      object-fit: cover;
      border-radius: $radius;
      margin: 1rem auto;
    }
    h1 {
      text-align: center;
      color: white;
      font-size: 28px;
      margin: 0;
    }
    padding-bottom: 3rem;
    background-color: $jade;
    border-radius: 0 0 $radius $radius;
    margin-bottom: 2rem;
    box-shadow: $shadow;
  }
  #buttons {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    grid-gap: 2rem;
    margin: 2rem;
    a {
      box-shadow: $shadow;
      text-decoration: none;
      height: 9rem;
      text-align: center;
      background-color: $orange;
      border-radius: $radius;
      border: none;
      color: white;
      font-size: 24px;
      display: flex;
      place-content: center;
      img {
        max-width: 60%;
        width: 5rem;
      }
    }
  }
  #badges {
    background-color: $lightgray;
    margin: 2rem;
    border-radius: $radius;
    padding: 1rem;
    overflow-x: scroll;
    white-space: nowrap;
    -ms-overflow-style: none;
    scrollbar-width: none;
    box-shadow: $shadow;
    &::-webkit-scrollbar { 
      display: none;
    }
    .badge {
      display: inline-block;
      background-color: $gray;
      padding: 2rem;
      border-radius: $radius;
      margin-right: 1rem;
      img {
        margin: 0 auto;
        width: 3rem;
      }
    }
  }
  #friends {
    margin: 2rem;
    button {
      box-shadow: $shadow;
      cursor: pointer;
      background-color: $jade;
      border: 0;
      padding: 1em;
      color: white;
      font-size: 24px;
      border-radius: $radius;
      width: 20rem;
      max-width: 100%;
      min-width: 50%;
      display: block;
      margin: 2rem auto;
    }
  }
</style>

<main>
  <div id="picture">
    <div id="nav">
      <a href="/"><img src="/images/vector/close.svg" alt="Go back"/></a>
    </div>
    <img id="profile-pic" src={user.picture} alt={user.name}>
    <h1>{user.name}</h1>
  </div>
  <div id="buttons">
    <a href="/favorites">
      <img src="/images/vector/heart.svg" alt="Heart Icon">
    </a>
    <a href="/history">
      <img src="/images/vector/route.svg" alt="Route Icon">
    </a>
  </div>
  <div id="badges">
    <div class="badge">
      <img src="/images/vector/badge.svg" alt="Badge"/>
    </div>
    <div class="badge">
      <img src="/images/vector/badge.svg" alt="Badge"/>
    </div>
    <div class="badge">
      <img src="/images/vector/badge.svg" alt="Badge"/>
    </div>
  </div>
  <div id="friends">
    <button>Add Friends</button>
    <div id="friends-list">
      {#each user.friends as { name, picture }}
        <Friend {name} {picture} />
      {/each}
    </div>
  </div>
</main>
