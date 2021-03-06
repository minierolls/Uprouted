<script>
  export let picture;
  export let name;
</script>

<style>
  div {
    margin: 2rem 0;
    background-color: $lightgray;
    border-radius: $radius;
    padding: 1rem;
    display: grid;
    grid-gap: 2rem;
    grid-template-columns: minmax(10%, 7rem) 1fr;
    align-items: center;
    img {
      width: 100%;
      border-radius: $radius;
      object-fit: cover;
    }
  }
</style>

<div>
  <img src={picture} alt={name} />
  <h2>{name}</h2>
</div>
