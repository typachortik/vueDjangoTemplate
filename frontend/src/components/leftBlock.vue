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
    width: 150px;
    height: 30px;
    padding: 5px;
    border: 1px solid #263e66
}

</style>