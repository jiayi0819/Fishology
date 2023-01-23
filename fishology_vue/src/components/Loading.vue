<template>
  <div class="loading">
    <div class="spinner-border text-info" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
</template>
<style scoped>
.loading {
  top: 0;
  z-index: 101;
  height: 100%;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
