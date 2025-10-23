<template>
  <div class="statsGrid">
    <div class="statCard leftTop">
      <div class="label">Мы</div>
      <div class="value">{{ stats.position }}</div>
      <div class="subLabel">на рынке</div>
    </div>

    <div class="statCard rightTop">
      <div class="label">Гарантируем</div>
      <div class="value">{{ stats.percent }}<span class="unit">%</span></div>
      <div class="subLabel">безопасность</div>
    </div>

    <div class="statCard leftBottom">
      <div class="label">Календарик за</div>
      <div class="value">{{ stats.year }}<span class="unit">г.</span></div>
      <div class="subLabel">в подарок</div>
    </div>

    <div class="statCard rightBottom">
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

.leftTop {
    border-bottom: 2px solid #92929200;
  border-right: 2px solid #92929200;
  background: linear-gradient(to bottom right, #92929200, #92929207);
}
.leftBottom {
    border-top: 2px solid #92929200;
  border-right: 2px solid #92929200;
  background: linear-gradient(to top right, #92929200, #92929207);
}
.rightTop {
  border-left: 2px solid #92929200;
  border-bottom: 2px solid #92929200;
  background: linear-gradient(to bottom left, #92929200, #92929207);
}
.rightBottom {
    border-left: 2px solid #92929200;
  border-top: 2px solid #92929200;
  background: linear-gradient(to top left, #92929200, #92929207);
}

.leftTop:hover {
  border-bottom: 2px solid #99999920;
  border-right: 2px solid #99999920;
  background: linear-gradient(to bottom right, #92929200, #92929215);
}
.leftBottom:hover {
  border-top: 2px solid #99999920;
  border-right: 2px solid #99999920;
  background: linear-gradient(to top right, #92929200, #92929215);
}
.rightTop:hover {
  border-left: 2px solid #99999920;
  border-bottom: 2px solid #99999920;
  background: linear-gradient(to bottom left, #92929200, #92929215);
}
.rightBottom:hover {
  border-left: 2px solid #99999920;
  border-top: 2px solid #99999920;
  background: linear-gradient(to top left, #92929200, #92929215);
}
.statsGrid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  border-radius:50%;
}

.statCard {
  padding: 20px;
  text-align: center;
  transition: all 0.3s ease;
  cursor: pointer;
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
@media (max-width: 768px) {
  .statsGrid {
    gap: 5px;
  }
  .statCard {
    padding: 10px;
  }
  .label {
    font-size: 12px;
  }
  .value {
    font-size: 42px;
  }
  .unit {
    font-size: 18px;
  }
  .subLabel {
    font-size: 14px;
  }
}
</style>