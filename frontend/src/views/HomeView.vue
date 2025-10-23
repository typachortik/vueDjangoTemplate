<template>
  <Header></Header>
  <div class='main'>
    <leftBlock></leftBlock>
    <rightBlock></rightBlock>
  </div>
</template>
<style>
  .main {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin: 100px 15% 0 15%;
    gap: 30px;
    flex-wrap: wrap;
  }
  @media (max-width: 768px) {
    .main {
      justify-content: center;
    }
  }
</style>