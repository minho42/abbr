<template>
  <div>
    <AbbrList :abbrData="abbrData" />
  </div>
</template>

<script>
import abbrData from '../data.json'
import AbbrList from '../components/AbbrList'

export default {
  components: {
    AbbrList,    
  },
  data() {
    return {
      abbrData
    }
  },
}
</script>
