<template>
  <tr class="border-b border-gray-200">
    <td class="text-center py-2">
      {{ name }}
    </td>
    <td class="pl-2">
      {{ description }}
    </td>
  </tr>  
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
