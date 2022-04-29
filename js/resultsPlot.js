const { date, observed, prediction1, prediction2 } = plotData;

// Dates prediction +1 from observed to join the lines
const datesPrediction = date.slice(-11);
// Add last value from pre predict date to join the lines
prediction1.unshift(observed.slice(-11)[0]);
prediction2.unshift(observed.slice(-11)[0]);

console.log(prediction1);
console.log(prediction2);

var traceTrue = {
    x: date,
    y: observed,
    mode: "lines",
    name: "True",
};

var tracePrediction1 = {
    x: datesPrediction,
    y: prediction1,
    mode: "lines",
    name: "Predikcia dát z delty a omikronu",
};

var tracePrediction2 = {
    x: datesPrediction,
    y: prediction2,
    mode: "lines",
    name: "Predikcia dát prevažne z omikronu",
};

var data = [traceTrue, tracePrediction1, tracePrediction2];

var layout = {
    title: "Najlepšie predikcie",
    xaxis_title: "Dátum",
    yaxis_title: "Hospitalizovaní",
};

Plotly.newPlot("resultsPlot", data, layout);
