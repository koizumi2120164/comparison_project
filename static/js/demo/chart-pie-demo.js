// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["未設定", "18歳以下", "18歳から60歳まで", "60歳以上"],
    datasets: [{
      data: [35, 10, 55,10],
      backgroundColor: ['#1E90FF','#FF8C00','#A9A9A9','#FFD700'],
      
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    title: {
      display: true,
      text: 'サイトを閲覧した人の年齢割',
      fontSize: 30,
      fontColor: "#2F4F4F"
    },
    legend: {
      display: true,
      position:'bottom'
    },
    cutoutPercentage: 80,
  },
});
