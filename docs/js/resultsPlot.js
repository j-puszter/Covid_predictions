let { date, observed, prediction1, prediction2 } = plotData;

// Get only 40 days data from datasets
date = date.slice(-30);
observed = observed.slice(-30);

console.log(date);

// Dates prediction +1 from observed to join the lines
const datesPrediction = date.slice(-11);
// Add last value from pre predict date to join the lines
prediction1.unshift(observed.slice(-11)[0]);
prediction2.unshift(observed.slice(-11)[0]);

var traceTrue = {
    x: date,
    y: observed,
    mode: "lines",
    name: "Reálny počet hospitalizovaných",
};

var tracePrediction1 = {
    x: datesPrediction,
    y: prediction1,
    mode: "lines",
    name: "Predikcia počtu hospitalizovaných - skupina I",
};

var tracePrediction2 = {
    x: datesPrediction,
    y: prediction2,
    mode: "lines",
    name: "Predikcia počtu hospitalizovaných - skupina II",
};

var data = [traceTrue, tracePrediction1, tracePrediction2];

var layout = {
    title: "Predikcia počtu hospitalizovaných z parametrov Ag% a PCR%",
    xaxis: {
        title: "Dátum",
    },
    yaxis: {
        title: "Hospitalizovaní",
    },
};

Plotly.newPlot("resultsPlot", data, layout, { responsive: true });
