<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
  props: ["data", "labels"],
  mounted() {
    console.log(this.data);
    this.renderBarChart();
  },
  computed: {
    chartData() {
      return Object.values(this.data).reverse();
    },
    chartLabels() {
      let today = new Date().getDay();
      if (today == 0) {
        return this.labels;
      }
      return [
        ...this.labels.slice(new Date().getDay(), 7),
        ...this.labels.slice(0, new Date().getDay()),
      ];
    },
  },
  watch: {
    chartData() {
      this.renderBarChart();
    },
  },
  methods: {
    renderBarChart() {
      const self = this;
      this.renderChart(
        {
          labels: self.chartLabels,
          datasets: [
            {
              label: "일주일의 기록",
              backgroundColor: " #37cdc2",
              data: self.chartData,
              borderColor: "rgba(1, 116, 188, 0.50)",
              hoverBackgroundColor: "#079992",
            },
          ],
        },
        { responsive: true, maintainAspectRatio: false }
      );
    },
  },
};
</script>
