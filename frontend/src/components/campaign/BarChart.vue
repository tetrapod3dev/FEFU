<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
  props: ["data", "labels"],
  mounted() {
    // console.log(this.data);
    // console.log(Object.keys(this.data));
    // console.log(Object.entries(this.data));
    // console.log(Object.values(this.data));
    // console.log(Object.keys(this.data).map(key => this.data[key]));
    this.renderBarChart();
  },
  computed: {
    chartData() {
      return this.data["isEnd"]
        ? Object.values(this.data).reverse().slice(0, -1)
        : [0, 0, 0, 0, 0, 0, 0];
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
      // console.log(this.chartData);
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
