var dom = document.getElementById("container");
var myChart = echarts.init(dom);
var app = {};
option = {
    title: {
        text: '关系图'
    },
    tooltip: {},
    animationDurationUpdate: 1500,
    animationEasingUpdate: 'quinticInOut',
    series : [
        {
            type: 'graph',
            layout: 'force',
            force:{
              repulsion: 10000
            },
            symbolSize: 50,
            roam: true,
            label: {
                normal: {
                    show: true
                }
            },
            edgeSymbol: ['circle', 'arrow'],
            edgeSymbolSize: [4, 10],
            edgeLabel: {
                normal: {
                    show:true,
                    textStyle: {
                        fontSize: 20
                    },
                    formatter:"{c}"
                }
            },
            nodes: [],
            links: [],
            lineStyle: {
                normal: {
                    opacity: 0.9,
                    width: 2,
                    curveness: 0.2
                }
            }
        }
    ]
};;
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}
