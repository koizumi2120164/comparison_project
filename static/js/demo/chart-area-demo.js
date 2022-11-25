// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["1月/2022", "2月/2022", "3月/2022", "4月/2022"],
    datasets: [{
      label: "メインページ",
      lineTension: 0,
      backgroundColor: "rgba(0,0,0,0)",
      borderColor: "rgba(78, 115, 223, 1)",
      pointRadius: 3,
      pointStyle:'rectRot', 
      pointBackgroundColor: "rgba(78, 115, 223, 1)",
      pointBorderColor: "rgba(78, 115, 223, 1)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
      borderColor: "rgba(78, 115, 223, 1)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [420, 230, 350, 415],
    },
    {
      label: "ランキング",
      lineTension: 0,
      backgroundColor: "rgba(0,0,0,0)",
      borderColor: "rgba(255,165,0)",
      pointRadius: 3,
      pointStyle:'rect',
      pointBackgroundColor: "rgba(255,165,0)",
      pointBorderColor: "rgba(255,165,0)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(255,165,0)",
      pointHoverBorderColor: "rgba(255,165,0)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [230, 440, 185,230],
    },
    {
      label: "口コミ掲示板",
      lineTension: 0,
      backgroundColor: "rgba(0,0,0,0)",
      borderColor: "rgba(128,128,128)",
      pointRadius: 3,
      pointStyle:'triangle',
      pointBackgroundColor: "rgba(128,128,128)",
      pointBorderColor: "rgba(128,128,128)",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "rgba(128,128,128)",
      pointHoverBorderColor: "rgba(128,128,128)",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [200, 200, 300,500],
    },
   ],
   
   },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 0,
        right: 0,
        top: 30,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: true,
          drawBorder: true
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [
        {ticks: {
        suggestedMax: 600,
        suggestedMin: 0,
        stepSize: 200,
        callback: function(value, index, values){
        return  value  },
       } },
       
    
    ],
    },
    title: {
      display: true,
      text: 'サイトに訪れた人の人数（万人）',
      fontSize: 30,
      fontColor: "#2F4F4F"
    },

    legend: {
      display: true,
      labels: {              
        fontSize: 12,           
        boxWidth: 12, 
        boxHeight: 0, 
        usePointStyle: true, 
                
        
    },
    
    },
    
  },
  
}
);

