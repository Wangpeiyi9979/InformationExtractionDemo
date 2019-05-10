function getTriple(){
  $.getJSON('./IEDemo', {text: $("#textBox").val(),}, function(data)
  {
      option.series[0].nodes = data.nodes;
      option.series[0].links = data.links;
      myChart.setOption(option, true);
  });
}
