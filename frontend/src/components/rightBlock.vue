<template>
  <div class="statsGrid">
    <div class="statCard">
      <div class="label">Мы</div>
      <div class="value">{{ stats.position }}</div>
      <div class="subLabel">на рынке</div>
    </div>

    <div class="statCard">
      <div class="label">Гарантируем</div>
      <div class="value">{{ stats.percent }}<span class="unit">%</span></div>
      <div class="subLabel">безопасность</div>
    </div>

    <div class="statCard">
      <div class="label">Календарик за</div>
      <div class="value">{{ stats.year }}<span class="unit">г.</span></div>
      <div class="subLabel">в подарок</div>
    </div>

    <div class="statCard">
      <div class="label">Путешествие</div>
      <div class="value">{{ stats.days }}</div>
      <div class="subLabel">дней</div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'

const stats = ref({
  position: 0,
  percent: 0,
  year: 0,
  days: 0
})

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/data/')
    if (response.ok) {
      const data = await response.json()
      stats.value = {
        position: data.position,
        percent: data.percent,
        year: data.year,
        days: data.days
      }
    } else {
      console.error('Ошибка загрузки данных')
    }
  } catch (error) {
    console.error('Сетевая ошибка:', error)
  }
})
</script>
<style>
.statsGrid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  padding: 40px;
  border-radius:50%;
}

.statCard {
  padding: 20px;
  text-align: center;
  transition: all 0.3s ease;
  cursor: pointer;
  backdrop-filter: blur(1px);
  background-color: #00000015;
}

.statCard:hover {
  backdrop-filter: blur(5px);
}

.label {
  font-size: 18px;
  color: #929292;
  margin-bottom: 10px;
  letter-spacing: 0.5px;
}

.value {
  font-size: 60px;
  font-weight: 700;
  color: #fafafa;

}

.unit {
  font-size: 24px;
  vertical-align: bottom;
}

.subLabel {
  font-size: 18px;
  color: #929292;
  margin-top: 10px;
}
</style>