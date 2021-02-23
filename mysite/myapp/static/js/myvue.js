// const axios = require("axios");

const Counter = {
  data() {
    return {
      counter: 0,
    };
  },
  mounted() {
    setInterval(() => {
      this.counter++;
    }, 1000);
  },
};

Vue.createApp(Counter).mount("#counter");

const AttributeBinding = {
  data() {
    return {
      message: "You loaded this page on " + new Date().toLocaleString(),
    };
  },
};

Vue.createApp(AttributeBinding).mount("#bind-attribute");

const EventHandling = {
  data() {
    return {
      message: "Hello Vue.js!",
    };
  },
  methods: {
    reverseMessage() {
      this.message = this.message.split("").reverse().join("");
    },
  },
};

Vue.createApp(EventHandling).mount("#event-handling");

const ConditionalRendering = {
  data() {
    return {
      seen: true,
    };
  },
};

Vue.createApp(ConditionalRendering).mount("#conditional-rendering");

const ListRendering = {
  data() {
    return {
      suggestions: [],
    };
  },
  mounted() {
    //get request
    //get results
    axios
      .get("/suggestions/")
      .then(function (response) {
        // handle success
        myapp.suggestions = response.data.suggestions;
        console.log(response);
      })
      .catch(function (error) {
        // handle error
        console.log(error);
      });
    //this.suggestions = new list
    setInterval(() => {
      axios
        .get("/suggestions/")
        .then(function (response) {
          // handle success
          myapp.suggestions = response.data.suggestions;
          console.log(response);
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        });
      //get request
      //get results
      //this.suggestions = new list
    }, 10000);
  },
};

const myapp = Vue.createApp(ListRendering).mount("#list-rendering");
