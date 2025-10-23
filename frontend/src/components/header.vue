<template>
    <div class='header'>
        <div class="logo">
            <img src='../assets/img/logo.png'></img>
        </div>
        <button class="burger" @click="toggleMenu" aria-label="Меню">
            <span></span>
            <span></span>
            <span></span>
        </button>
        <div class='links' :class="{ active: isMenuOpen }">
            <span>Главная</span>
            <span>Технологии</span>
            <span>График полетов</span>
            <span>Гарантии</span>
            <span>О компании</span>
            <span>Контакты</span>
        </div>
    </div>
</template>
<script setup>
import { ref } from 'vue';

const isMenuOpen = ref(false);

function toggleMenu() {
    isMenuOpen.value = !isMenuOpen.value;
}
</script>
<style>
.logo {
    border: 1px solid #92929225;
    background: 
    linear-gradient(to right, #fff 10px, transparent 0, transparent calc(100% - 10px), #fff 0) 0 0 / 100% 1px no-repeat,
    linear-gradient(to right, #fff 10px, transparent 0, transparent calc(100% - 10px), #fff 0) 0 100% / 100% 1px no-repeat,
    linear-gradient(to bottom, #fff 10px, transparent 0, transparent calc(100% - 10px), #fff 0) 0 0 / 1px 100% no-repeat,
    linear-gradient(to bottom, #fff 10px, transparent 0, transparent calc(100% - 10px), #fff 0) 100% 0 / 1px 100% no-repeat;
}
.header {
    display: flex;
    position: relative;
    background-color: #00000050;
    padding: 0 15% 0 15%;
    justify-content: space-between;
    align-items: center;
    border-bottom: solid 2px #92929250;
    border-top: solid 2px #92929250;
    img {
        transition: all 0.5s;
        padding: 30px 20px 30px 30px;
        border: 1px solid #92929200;
    }
    .links{
        display: flex;
        font-size: 16px;
        flex-direction: row;
        justify-content: center;
        gap: 30px;
        align-items: center;
        color: #ffffff;
        span{
            transition: all 0.5s;
            border-bottom: solid 1px #92929200;
        }
        span:hover{
            color: #92929250;
            border-bottom: solid 1px #92929250;
            cursor: pointer;
        }
    }
    .burger {
    display: none; 
    flex-direction: column;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 8px;
    z-index: 10;

    span {
        width: 28px;
        height: 3px;
        background-color: #ffffff;
        margin: 4px 0;
        transition: 0.3s;
        border-radius: 2px;
    }
  }
}
@media (max-width: 768px) {
    .header {
        padding: 0;
        .burger {
            display: flex;
        }
        .links {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background-color: #00000075;
            flex-direction: column;
            gap: 20px;
            padding: 20px;
            display: none;
            z-index: 9;
            backdrop-filter: blur(5px);
        }
        .links.active {
            display: flex;
        }
        .logo {
            display: flex;
            margin-left: 5px;
            justify-content: center;
            align-items: center;
        }
  }
}
</style>