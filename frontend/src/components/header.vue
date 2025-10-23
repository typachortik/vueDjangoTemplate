<template>
    <div class='header'>
        <img src='../assets/img/logo.png'>
        <div class='links'>
            <span>Главная</span>
            <span>Технологии</span>
            <span>График полетов</span>
            <span>Гарантии</span>
            <span>О компании</span>
            <span>Контакты</span>
        </div>
    </div>
</template>
<style>
.header {
    display: flex;
    background-color: #00000050;
    padding: 30px 15% 30px 15%;
    justify-content: space-between;
    align-items: center;
    border-bottom: solid 2px #92929250;
    img {
        transition: all 0.5s;
    }
    img:hover {
        
    }
    .links{
        display: flex;
        font-size: 16px;
        flex-direction: row;
        justify-content: center;
        gap: 22px;
        align-items: center;
        color: #ffffff;
        span{
            transition: all 0.5s;
        }
        span:hover{
            color: #92929250;
            border-bottom: solid 1px #92929250;
            cursor: pointer;
        }
    }
}
</style>