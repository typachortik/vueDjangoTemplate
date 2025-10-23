<template>
  <div class="admin-page">
    <h1>Админка</h1>
    <form @submit.prevent="saveData" v-if="data">
      <div>
        <label>Position (число):</label>
        <input v-model.number="data.position" type="number" />
      </div>
      <div>
        <label>Percent:</label>
        <input v-model.number="data.percent" type="number" step="0.1" />
      </div>
      <div>
        <label>Year:</label>
        <input v-model.number="data.year" type="number" />
      </div>
      <div>
        <label>Days:</label>
        <input v-model.number="data.days" type="number" />
      </div>
      <button type="submit">Сохранить</button>
      <p v-if="message" :class="{ error: isError }">{{ message }}</p>
    </form>
    <p v-else>Загрузка...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const data = ref(null)
const message = ref('')
const isError = ref(false)

const API_URL = 'http://127.0.0.1:8000/api/data/'

// Загрузка данных
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

// Сохранение данных
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
.admin-page {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1rem;
}
input {
  width: 100%;
  padding: 0.5rem;
  margin: 0.5rem 0 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
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