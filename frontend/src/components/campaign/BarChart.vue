<script>
import { Bar } from "vue-chartjs";

export default {
  extends: Bar,
  mounted() {
    this.renderChart(
      {
        labels: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
        datasets: [
          {
            label: "일주일의 기록",
            backgroundColor: " #37cdc2",
            data: [40, 20, 12, 39, 14, 20, 39],
            borderColor: "rgba(1, 116, 188, 0.50)",
            hoverBackgroundColor: "#079992",
          },
        ],
      },
      { responsive: true, maintainAspectRatio: false }
    );
  },
};
</script>
