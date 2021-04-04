<template>
  <div>
    {{ name }}: {{ description }}
  </div>  
</template>

<script>
export default {
  name: "AbbrItem",
  props: {
    name: String,
    description: String,
  },
  computed: {
  }
}
</script>
