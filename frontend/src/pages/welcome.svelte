<script>
  // idk why im parsing this anew on each page
  const user = JSON.parse(sessionStorage.getItem('user'));
  // just use these to construct an URL or something to get the request you want
  let difficulty; // stores difficulty selected
  let distance; // stores distance desired
  let startLocation; // desired start location
  let endLocation; // desired end location
</script>

<style>
  #profile {
    display: flex;
    justify-content: flex-end;
    a {
      justify-self: end;
      align-self: center;
      img {
        max-height: 4rem;
        border-radius: $radius;
      }
    }
  }
  #settings {
    background-color: $jade;
    border-radius: 0 0 $radius $radius;
    color: white;
    padding: 1rem;
  }
  #text {
    margin-bottom: 2rem;
    h1 {
      font-size: 36px;
      font-weight: 900;
      margin: 0.25em 0;
    }
    h2 {
      font-weight: 100;
      font-size: 22px;
      margin: 0.5em 0;
    }
  }
  #difficulty {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    border-radius: 1rem;
    margin: 1rem 0;
    overflow: hidden;
    label {
      text-align: center;
      margin: 0;
      padding: 1rem;
      font-weight: 900;
      font-size: 18px;
      input {
        display: none;
      }
    }
    #chill {
      background-color: #8ae8dd;
    }
    #moderate {
      background-color: #4fd0c0;
    }
    #intense {
      background-color: #30bcab;
    }
    input:checked + span {
      color: $orange;
    }
  }
  #time {
    background-color: #4fd0c0;
    padding: 1rem;
    border-radius: 1rem;
    display: block;
    margin: 2rem 0;
    p {
      font-size: 22px;
      text-align: center;
      margin: 0;
      margin-bottom: 1em;
      font-weight: bold;
    }
    input {
      font-size: 22px;
      margin: 0 auto;
      display: block;
      text-align: center;
      width: 100%;
      box-sizing: border-box;
    }
  }
  input {
    -moz-appearance: textfield;
    color: white;
    font-family: $font-stack;
    border: none;
    background-color: transparent;
    &:invalid {
      box-shadow: none;
      color: red;
    }
    &:focus {
      outline: none;
    }
    &::-webkit-outer-spin-button,
    &::-webkit-inner-spin-button {
      -webkit-appearance: none;
      margin: 0;
    }
  }
  button {
    box-shadow: $shadow;
    border-radius: 50%;
    background-color: $orange;
    border: 0;
    width: 6rem;
    height: 6rem;
    display: flex;
    justify-content: center;
    align-items: center;
    img {
      width: 3rem;
      height: 3rem;
    }
  }
  #select {
    display: flex;
    justify-content: space-evenly;
    margin: 3rem 0;
  }
  #locations {
    font-size: 22px;
    padding: 1rem;
    background-color: #4fd0c0;
    border-radius: 1rem;
    input {
      font-size: 20px;
      width: 100%;
    }
    label {
      display: grid;
      grid-template-columns: auto 1fr;
      grid-gap: 1rem;
      padding: 0.5rem 0;
    }
  }
</style>

<div id="settings">
  <div id="profile">
    <a href="/profile"><img src={user.picture} alt={user.name}></a>
  </div>
  <div id="text">
    <h1>Welcome!</h1>
    <h2>What is your goal for today?</h2>
  </div>
  <div id="difficulty">
    <label id="chill">
      <input type="radio" bind:group={difficulty} value={1} />
      <span>Chill</span>
    </label>
    <label id="moderate">
      <input type="radio" bind:group={difficulty} value={2} />
      <span>Moderate</span>
    </label>
    <label id="intense">
      <input type="radio" bind:group={difficulty} value={3} />
      <span>Intense</span>
    </label>
  </div>
  <label id="time">
    <p>Kilometers</p>
    <input type="number" bind:this={distance} step="0.1" />
  </label>
  <div id="locations">
    <label>
      <strong>Start:</strong>
      <input bind:this={startLocation}/>
    </label>
    <label>
      <strong>End:</strong>
      <input bind:this={endLocation}/>
    </label>
  </div>
</div>
<div id="select">
  <button>
    <img src="/images/vector/running.svg"/>
  </button>
  <button>
    <img src="/images/vector/bicycle.svg"/>
  </button>
</div>
