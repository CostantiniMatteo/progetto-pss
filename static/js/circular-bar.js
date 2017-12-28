// progressbar.js@1.0.0 version is used
// Docs: http://progressbarjs.readthedocs.org/en/1.0.0/
function circularBar(value) {
  var bar = new ProgressBar.Circle(document.getElementById("container"), {
    color: '#aaa',
    // This has to be the same size as the maximum width to
    // prevent clipping
    strokeWidth: 6,
    trailWidth: 1,
    easing: 'easeInOut',
    duration: 1400,
    text: {
      autoStyleContainer: false
    },
    svgStyle: {
        display: 'block',

        // Important: make sure that your container has same
        // aspect ratio as the SVG canvas. See SVG canvas sizes above.
        width: '100%'
    },
   from: {color: '#FFEA82', width: 4},
    to: {color: '#ED6A5A', width: 6},
    // Set default step function for all animate calls
    step: function(state, circle) {
      circle.path.setAttribute('stroke', state.color);
      circle.path.setAttribute('stroke-width', state.width);

      //var value = Math.round(circle.value() * 100);

      circle.setText(value + '%');


    }
  });
  bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
  bar.text.style.fontSize = '2rem';
  bar.animate(value/100);  // Number from 0.0 to 1.0
}
