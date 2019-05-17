const Animation = (n1, n2, direction, props) => {
  if (!props) props = {};

  n1 = document.querySelector(n1);
  n2 = document.querySelector(n2);
  let old_height = n1.getBoundingClientRect().height;
  n1.classList.add("fade-out--" + direction);
  n2.classList.add("fade-in--" + direction);
  n1.addEventListener('transitionend', (e) => {
    if (e.propertyName === "transform") {
      n1.style.display = "none";
      n2.style.display = "block";
      let new_height = n2.getBoundingClientRect().height;
      if (props.transitionHeight)
        n2.style.height = old_height + "px";
      setTimeout(function () {
        n2.classList.remove("fade-in--" + direction);
        if (props.transitionHeight)
          n2.style.height = new_height + "px";
      });
    }
  });
}

setTimeout(function () {
}, 1000);

new Vue({
  el: "#app",
  methods: {
    register: (e) => {
      console.log(e);
      Animation(".form-section > .part-1", ".parts--register .part-1", "left")
    },

    preventDefault: (e) => {
      e.preventDefault();
    },

    animate: Animation,

    addLine: function () { this.work_history.push(null) }
  },
  data: {
    work_history: [null, null]
  }
});
