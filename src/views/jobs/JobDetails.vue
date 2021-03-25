<template>
  <div class="main">
    <h1 id="heading">Job Detail Page</h1>
    <br>
    <div class="card">
    <div class="card-body">
      <h5 class="card-title">{{ job.title }}</h5>
      <br>
      <p class="card-text">
        {{ job.details }}
      </p>
    </div>
  </div>
  </div>
  
</template>

<script>
export default {
  props: ["id"],
  data() {
    return {
      job: {},
    };
  },
  mounted() {
    fetch(`http://localhost:5000/jobs/${this.id}`, {})
      .then((res) => res.json())
      .then((data) => (this.job = data))
      .catch((err) => console.log(err.message));
  },
};
</script>

<style scoped>
.main {
  text-align: center;
}
.card-title {
  color: #ebe4a9;
}
.card-text {
  color: #f5e3eb;
}
.card{
    margin-left: auto;
    margin-right: auto;
    background: rgb(40, 44, 51);
    width: 450px;
    padding: 10px;
}
</style>