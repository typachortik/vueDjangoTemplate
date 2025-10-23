<template>
  <div class="page">
    <div class="admin-page">
      <h1>Админка</h1>
      <p>Изменение данных правого блока главной страницы, которая отрисовывает статистику</p>
      <form @submit.prevent="saveData" v-if="data">
        <div class="inputData">
          <label>Position:</label>
          <input v-model.number="data.position" type="number" />
        </div>
        <div class="inputData">
          <label>Percent:</label>
          <input v-model.number="data.percent" type="number" step="0.1" />
        </div>
        <div class="inputData">
          <label>Year:</label>
          <input v-model.number="data.year" type="number" />
        </div>
        <div class="inputData">
          <label>Days:</label>
          <input v-model.number="data.days" type="number" />
        </div>
        <button type="submit">Сохранить</button>
        <p v-if="message" :class="{ error: isError }">{{ message }}</p>
      </form>
      <p v-else>Загрузка...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const data = ref(null)
const message = ref('')
const isError = ref(false)

const API_URL = 'http://127.0.0.1:8000/api/data/'

onMounted(async () => {
  try {
    const res = await fetch(API_URL)
    if (res.ok) {
      data.value = await res.json()
    } else {
      throw new Error('Не удалось загрузить данные')
    }
  } catch (err) {
    message.value = err.message
    isError.value = true
  }
})

async function saveData() {
  try {
    const res = await fetch(API_URL, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data.value)
    })

    if (res.ok) {
      message.value = 'Данные успешно сохранены!'
      isError.value = false
    } else {
      const error = await res.json()
      message.value = 'Ошибка: ' + JSON.stringify(error)
      isError.value = true
    }
  } catch (err) {
    message.value = 'Сетевая ошибка: ' + err.message
    isError.value = true
  }
}
</script>

<style scoped>
.inputData {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  backdrop-filter: blur(5px);
  min-height: 100vh;
}
.admin-page {
  padding: 20px;
  background-color: #92929225;
  display: flex;
  margin: 150px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;
  width: 400px;
  border-radius: 30px;
  p {
    text-align: center;
  }
}
form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 5px;
}
input {
  width: 100px;
  padding: 5px;
  border: 5px solid white;
  border-radius: 15px;
  text-align: center;
  transition: all 0.5s;
}
input:focus {
  border: 5px solid orangered;
  background-color: rgba(255, 68, 0, 0.041);
}
button {
  background: #42b883;
  color: white;
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.error {
  color: red;
}
</style>