<template>
    <div class='blockLeft'>
        <div class='texts'>
            <p class='mainText'>ПУТЕШЕСТВИЕ</p>
            <p class='secondText'>на красную планету</p>
        </div>
        <div class='button'>
            Начать путешествие
        </div>
    </div>
</template>
<style>
.blockLeft {
    display: flex;
    flex-direction: column;
    gap: 150px;
    text-align: left;
}
.texts {
    background-image: linear-gradient(to right, #ffffff, #ff4208);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent; 
    display: flex;
    gap: 2px;
    flex-direction: column;
    margin: 0;
}
.mainText {
    font-size: 58px;
    font-weight: 700;
    margin: 0;
}
.secondText {
    margin: 0;
    font-size: 25px;
}
.button {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 14px;
    width: 180px;
    height: 35px;
    padding: 5px;
    font-weight: 100;
    border: 1px solid #224b72;
    border-image: linear-gradient(to right top, #224b72, #001b3a, #224b72);
    border-image-slice: 1;
    background: 
    linear-gradient(to right, #fff 0px, transparent 0, transparent calc(100% - 10px), #fff 0) 0 0 / 100% 1px no-repeat,
    linear-gradient(to right, #fff 10px, transparent 0, transparent calc(100% - 0px), #fff 0) 0 100% / 100% 1px no-repeat,
    linear-gradient(to bottom, #fff 0px, transparent 0, transparent calc(100% - 10px), #fff 0) 0 0 / 1px 100% no-repeat,
    linear-gradient(to bottom, #fff 10px, transparent 0, transparent calc(100% - 0px), #fff 0) 100% 0 / 1px 100% no-repeat;

}
@media (max-width: 768px) {
    .blockLeft {
        justify-content: center;
        align-items: center;
    }
    .mainText {
        font-size: 42px;
    }
}
</style>