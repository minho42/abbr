export { default as AbbrItem } from '../../components/AbbrItem.vue'
export { default as AbbrList } from '../../components/AbbrList.vue'
export { default as Navbar } from '../../components/Navbar.vue'

export const LazyAbbrItem = import('../../components/AbbrItem.vue' /* webpackChunkName: "components/abbr-item" */).then(c => wrapFunctional(c.default || c))
export const LazyAbbrList = import('../../components/AbbrList.vue' /* webpackChunkName: "components/abbr-list" */).then(c => wrapFunctional(c.default || c))
export const LazyNavbar = import('../../components/Navbar.vue' /* webpackChunkName: "components/navbar" */).then(c => wrapFunctional(c.default || c))

// nuxt/nuxt.js#8607
export function wrapFunctional(options) {
  if (!options || !options.functional) {
    return options
  }

  const propKeys = Array.isArray(options.props) ? options.props : Object.keys(options.props || {})

  return {
    render(h) {
      const attrs = {}
      const props = {}

      for (const key in this.$attrs) {
        if (propKeys.includes(key)) {
          props[key] = this.$attrs[key]
        } else {
          attrs[key] = this.$attrs[key]
        }
      }

      return h(options, {
        on: this.$listeners,
        attrs,
        props,
        scopedSlots: this.$scopedSlots,
      }, this.$slots.default)
    }
  }
}
