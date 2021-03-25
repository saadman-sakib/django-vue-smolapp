<template>
  <div class="main">
    <h1>Jobs</h1>
    <ul class="list-group list-group-flush">
      <li v-for="job in jobs" :key="job.key" class="list-group-item">
        <router-link
          class="job"
          :to="{ name: 'JobDetails', params: { id: job.id } }"
        >
          {{ job.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      jobs: [],
    };
  },
  mounted() {
    fetch("http://localhost:5000/jobs",{
    })
      .then(res => res.json())
      .then(data => this.jobs = data)
      .catch(err => console.log(err.message));
  },
};
</script>

<style scoped>
h1 {
  color: #e79b77;
}

.list-group-item {
  background: rgb(26, 32, 41);
  border-color: white;
}

.main {
  padding: 5%;
}

.job {
  color: #e5e6b0;
  font-weight: bolder;
}
</style>