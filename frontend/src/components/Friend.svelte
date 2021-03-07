<script>
  export let picture;
  export let name;
</script>

<style>
  div {
    margin: 2rem 0;
    background-color: $lightgray;
    border-radius: $radius;
    padding: 0.75rem;
    display: grid;
    grid-gap: 1rem;
    grid-template-columns: minmax(4rem, 10%) 1fr;
    align-items: center;
    box-shadow: $shadow;
    img {
      width: 100%;
      border-radius: $radius;
      object-fit: cover;
    }
  }
</style>

<div>
  <img src={picture} alt={name} />
  <h3>{name}</h3>
</div>
