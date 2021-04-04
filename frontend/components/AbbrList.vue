<template>
  <div class="flex flex-col justify-center pt-2 px-2 mx-4">
    <div class="flex px-6 py-1 flex-wrap justify-center mb-2">
      {{ filteredAbbrData.length }} / {{ abbrData.length }}
    </div>
    
    <div class="">
      <form v-on:submit.prevent>
        <!-- <label for="search" class="text-center text-xl mb-1 mr-2">
          Search
        </label> -->
        <div class="flex items-center justify-between relative">
          <input
            id="searchInput"
            v-model="query"
            type="text"
            placeholder="Search abbreviations"
            class="pl-6 pr-24 py-2 rounded-lg w-full border border-gray-300 focus:border-gray-800 bg-gray-100 focus:outline-none"
            autofocus
          />

          <div class="absolute inset-y-1 right-0 flex items-center">
            <div
              v-if="query.length > 0"
              class="absolute inset-y-0 right-4 flex items-center"
            >
              <button
                @click="clearInput"
                class="h-full px-3 text-gray-500 hover:text-gray-800"
              >
                <svg
                  class="w-6 h-6"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M6 18L18 6M6 6l12 12"
                  ></path>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
    
    <table class="table-auto mt-2">
      <thead>
        <tr class="border-b-2 border-gray-300">
          <!-- <th class="font-bold">No</th> -->
          <th class="font-bold">Name</th>
          <th class="font-bold text-left pl-2">Description</th>
          <!-- <th class="font-bold">Wiki</th> -->
        </tr>
      </thead>
      <tbody>
        <AbbrItem
          v-for="abbr in filteredAbbrData"
          v-bind="abbr"
          :key="abbr.id"
        />
      </tbody>
    </table>
    
  </div>
</template>

<script>
import AbbrItem from './AbbrItem'

export default {
  name: 'AbbrList',
  data() {
    return {
      query: '',
    }
  },
  components: {
    AbbrItem,
  },
  props: {
    abbrData: Array,
  },
  methods: {
    clearInput() {
      this.query = ''
      document.querySelector('#searchInput').focus()
    },
  },
  computed: {
    filteredAbbrData() {
      const query = this.query.toLowerCase().trim()
      if (query.length < 1) {
        return []
      }
      return this.abbrData.filter((item) => {
        return (item.name.toLowerCase().includes(query) ||item.description.toLowerCase().includes(query))
      })
    }
  },
}
</script>
