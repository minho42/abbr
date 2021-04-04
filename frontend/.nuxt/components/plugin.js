import Vue from 'vue'
import { wrapFunctional } from './index'

const components = {
  AbbrItem: () => import('../../components/AbbrItem.vue' /* webpackChunkName: "components/abbr-item" */).then(c => wrapFunctional(c.default || c)),
  AbbrList: () => import('../../components/AbbrList.vue' /* webpackChunkName: "components/abbr-list" */).then(c => wrapFunctional(c.default || c)),
  Navbar: () => import('../../components/Navbar.vue' /* webpackChunkName: "components/navbar" */).then(c => wrapFunctional(c.default || c))
}

for (const name in components) {
  Vue.component(name, components[name])
  Vue.component('Lazy' + name, components[name])
}
