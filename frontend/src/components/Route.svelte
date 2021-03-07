<script>
  export let name;
  export let distance;
</script>

<style>
  div {
    background-color: $orange;
    border-radius: $radius;
    color: white;
    display: flex;
    padding: 1.5rem;
    font-size: 20px;
    align-items: center;
    box-shadow: $shadow;
    margin: 1.5rem 0;
    justify-content: space-between;
    grid-auto-flow: column;
    font-weight: 900;
  }
</style>

<div>
  <h2>{name}</h2>
  <h2>{distance}</h2>
</div>
