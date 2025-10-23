import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Header from './components/header.vue'
import './assets/fonts/museo-sans-cyrl.css'
import LeftBlock from './components/leftBlock.vue'
import RightBlock from './components/rightBlock.vue'

const app = createApp(App)

app.use(router)
app.component('Header', Header)
app.component('leftBlock',LeftBlock)
app.component('rightBlock',RightBlock)

app.mount('#app')
