<template>
  <div id="game-status">
    <div class="status-box">
      <span class="text-bold">Thanks for joining the game with PIN: </span>
      <span>{{ Game.publicId }}</span>
      <br />
      <span class="text-bold">The game will start soon!</span>
      <br />
      <span class="text-bold">Current game state: </span>
      <span>{{ Game.state }}</span>
    </div>
  </div>
</template>


<script>
    export default {
        name: 'game-status',
        props: {
            Game: {},
        }
    }
</script>

<style scoped>
#game-status {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.status-box {
  background-color: #c68f65;
  color: #000;
  border-radius: 10px;
  box-shadow: 0px 0px 20px 5px #6b4c35;
  padding: 1rem 1.5rem;
  font-size: 2.5rem;
  font-weight: bold;
  text-align: center;
}

.status-box .text-bold {
  font-weight: bold;
  color: #000;
}
</style>