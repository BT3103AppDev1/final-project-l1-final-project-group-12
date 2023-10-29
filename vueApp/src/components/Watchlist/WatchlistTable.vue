<template>
    <div>
        <ScrollableTable :headers="tableHeaders" :rows="tableRows" />
    </div>
</template>

<script>

  import ScrollableTable from '@/components/Common/ScrollableTable.vue';
  
  export default {
    components: {
      ScrollableTable,
    },
    data() {
      return {
        tableHeaders: ['#', 'Name', 'Price', '% Change', 'Market Cap', 'Volume'],
        tableRows: [
        ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          ["Apple", "$XXX", "0.00%", " $XXX", "$XXX"],
          
          // Add more rows as needed
        ],
      };
    },
  };
  </script>