<template>
  <div class="home">
    <!-- Background video -->
    <div class="video-background-holder">
      <div class="video-background-overlay"></div>
      <video
        playsinline="playsinline"
        autoplay="autoplay"
        muted="muted"
        loop="loop">
        <source
          src="../../../fishology_django/media/assets/CoverVideo.mp4"
          type="video/mp4" />
      </video>
      <div class="video-background-content container h-100">
        <div class="d-flex h-100 text-center align-items-center">
          <div class="w-100 text-white">
            <h1 class="light">Write, Read and Relax...</h1>
            <p class="lead mb-3 light">
              An underwater diary website that your journey to mindfulness.
            </p>
            <a class="btn btn-primary light" href="#about"> Find out more </a>
          </div>
        </div>
      </div>
    </div>
    <!-- End -->

    <section class="container-fluid mx-3 bg-white" id="about">
      <div class="row h-100 align-items-center mx-3">
        <div class="col-4">
          <img
            class="img-fluid"
            src="../../../fishology_django/media/assets/fisho-mascot.png"
            alt="" />
        </div>
        <div class="col-8">
          <h2 class="light-blue">A special place to keep your memories</h2>
          <p class="text-muted">
            Fishology provides a whole new experience of diary application with
            visual indulgence, where every diary you submitted will be carried
            by the fish in your aquarium.
          </p>
          <br />
          <a href="#write" class="dark-blue"><u>What's next</u></a>
        </div>
      </div>
    </section>

    <section class="container-fluid mx-3" id="write">
      <div class="row h-100 align-items-center mx-3">
        <div class="col-5 text-center">
          <img
            class="img-fluid rounded"
            src="../../../fishology_django/media/assets/write.png"
            alt="" />
        </div>
        <div class="col-7">
          <h2 class="light-blue">Write Diary</h2>
          <p class="text-muted">
            Express your feeling freely using Rich Text Editor in Fishology. You
            can also choose your mood, weather and fish you want the diary to be
            carried by!
          </p>
          <br />
          <a href="#catalogue" class="dark-blue"><u>What's next</u></a>
        </div>
      </div>
    </section>

    <section class="container-fluid mx-3 bg-white" id="catalogue">
      <div class="row h-100 align-items-center mx-3">
        <div class="col-7">
          <h2 class="light-blue">Catalogue</h2>
          <p class="text-muted">
            Catalogue contains information of all fish types in the aquarium,
            but some remain mysterious: write more diaries to unlock them! You
            can also change your aquarium theme and sky here.
          </p>
          <br />
          <a href="#statistics" class="dark-blue"><u>What's next</u></a>
        </div>
        <div class="col-5 text-center">
          <img
            class="img-fluid rounded"
            src="../../../fishology_django/media/assets/catalogue.png"
            alt="" />
        </div>
      </div>
    </section>

    <section class="container-fluid mx-3" id="statistics">
      <div class="row h-100 align-items-center">
        <div class="col-5 text-center">
          <img
            class="img-fluid rounded"
            src="../../../fishology_django/media/assets/statistics.png"
            alt="" />
        </div>
        <div class="col-7">
          <h2 class="light-blue">Statistics</h2>
          <p class="text-muted">
            Understand your diary habit and mood swing throughout the time.
            Track your mood and diary submissions in weeks, months and year!
          </p>
          <br />
          <a href="#filter" class="dark-blue"><u>What's next</u></a>
        </div>
      </div>
    </section>

    <section class="container-fluid mx-3 bg-white" id="filter">
      <div class="row h-100 gx-4 gx-lg-5">
        <div class="col-12">
          <h2 class="text-center mt-5 light-blue">Filter your diary!</h2>
          <hr class="divider mx-5" />
        </div>
        <div class="col-lg-3 col-sm-6 text-center">
          <div class="mt-md-4 mt-sm-3">
            <div class="mb-2">
              <i class="fa-duotone fa-calendar-days dark-blue"></i>
            </div>
            <h3 class="h4 mb-2 dark-blue">Date</h3>
            <p class="text-muted mb-0">
              When you want to look back the memories during some special times.
            </p>
          </div>
        </div>
        <div class="col-lg-3 col-sm-6 text-center">
          <div class="mt-md-4 mt-sm-3">
            <div class="mb-2">
              <i class="fa-duotone fa-face-laugh-wink dark-blue"></i>
            </div>
            <h3 class="h4 mb-2 dark-blue">Mood</h3>
            <p class="text-muted mb-0">
              Doesn’t matter if it’s a happy or sad memory, these experiences
              have their own meaning!
            </p>
          </div>
        </div>
        <div class="col-lg-3 col-sm-6 text-center">
          <div class="mt-md-4 mt-sm-3">
            <div class="mb-2">
              <i class="fa-duotone fa-sun-cloud dark-blue"></i>
            </div>
            <h3 class="h4 mb-2 dark-blue">Weather</h3>
            <p class="text-muted mb-0">
              Weather can have great impact on one’s mood. Check out what you
              were doing at that time!
            </p>
          </div>
        </div>
        <div class="col-lg-3 col-sm-6 text-center">
          <div class="mt-md-4 mt-sm-3">
            <div class="mb-2">
              <i class="fa-duotone fa-fish dark-blue"></i>
            </div>
            <h3 class="h4 mb-2 dark-blue">Fish</h3>
            <p class="text-muted mb-0">
              Looking for some special memory by some special fish? Call them
              out!
            </p>
          </div>
        </div>
        <div class="col-12 text-center">
          <div class="mt-md-4 mt-sm-3">
            <div class="mb-2">
              <i class="fa-duotone fa-user dark-blue"></i>
            </div>
            <h3 class="h4 mb-2 dark-blue">Author</h3>
            <p class="text-muted mb-0">
              Check out diaries written by your beloved one in shared aquarium.
            </p>
          </div>
        </div>
        <br />
        <a href="#share" class="dark-blue text-center"><u>What's next</u></a>
      </div>
    </section>

    <section class="container-fluid mx-3" id="share">
      <div class="row h-100 align-items-center mx-3">
        <div class="col-5 text-center">
          <img
            class="img-fluid rounded"
            src="../../../fishology_django/media/assets/share.png"
            alt="" />
        </div>
        <div class="col-7">
          <h2 class="light-blue">Share</h2>
          <p class="text-muted">
            Create a shared aquarium with your friends and exchange diaries with
            each other!
          </p>
          <br />
          <a href="#" class="dark-blue"><u>Back to top</u></a>
          <br class="my-5" />
          <a @click="this.navigateTo('sign-up')" class="btn btn-primary"
            >Sign Up Today!</a
          >
        </div>
      </div>
    </section>

    <footer class="container py-5">
      <div class="row">
        <div class="col-12 col-md">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            fill="none"
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            class="d-block mb-2"
            role="img"
            viewBox="0 0 24 24">
            <title>Product</title>
            <circle cx="12" cy="12" r="10" />
            <path
              d="M14.31 8l5.74 9.94M9.69 8h11.48M7.38 12l5.74-9.94M9.69 16L3.95 6.06M14.31 16H2.83m13.79-4l-5.74 9.94" />
          </svg>
          <small class="d-block mb-3 text-muted">&copy; 2017–2021</small>
        </div>
        <div class="col-6 col-md">
          <h5>Features</h5>
          <ul class="list-unstyled text-small">
            <li><a class="link-secondary" href="#">Cool stuff</a></li>
            <li><a class="link-secondary" href="#">Random feature</a></li>
            <li><a class="link-secondary" href="#">Team feature</a></li>
            <li><a class="link-secondary" href="#">Stuff for developers</a></li>
            <li><a class="link-secondary" href="#">Another one</a></li>
            <li><a class="link-secondary" href="#">Last time</a></li>
          </ul>
        </div>
        <div class="col-6 col-md">
          <h5>Resources</h5>
          <ul class="list-unstyled text-small">
            <li><a class="link-secondary" href="#">Resource name</a></li>
            <li><a class="link-secondary" href="#">Resource</a></li>
            <li><a class="link-secondary" href="#">Another resource</a></li>
            <li><a class="link-secondary" href="#">Final resource</a></li>
          </ul>
        </div>
        <div class="col-6 col-md">
          <h5>Resources</h5>
          <ul class="list-unstyled text-small">
            <li><a class="link-secondary" href="#">Business</a></li>
            <li><a class="link-secondary" href="#">Education</a></li>
            <li><a class="link-secondary" href="#">Government</a></li>
            <li><a class="link-secondary" href="#">Gaming</a></li>
          </ul>
        </div>
        <div class="col-6 col-md">
          <h5>About</h5>
          <ul class="list-unstyled text-small">
            <li><a class="link-secondary" href="#">Team</a></li>
            <li><a class="link-secondary" href="#">Locations</a></li>
            <li><a class="link-secondary" href="#">Privacy</a></li>
            <li><a class="link-secondary" href="#">Terms</a></li>
          </ul>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "Home",
  components: {},
  methods: {
    navigateTo(destination) {
      this.$router.push(`/${destination}`);
    },
  },
};
</script>

<style scoped lang="scss">
section {
  height: 100vh;

  img {
    max-height: 400px;
  }
}

#filter {
  i {
    font-size: 1.5rem;
    @media (min-width: 768px) {
      font-size: 3rem;
    }
  }
}

/* VIDEO */

.video-background-holder {
  position: relative;
  background-color: black;
  height: calc(100vh - 72px);
  min-height: 25rem;
  width: 100%;
  overflow: hidden;
}

.video-background-holder video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  z-index: 0;
  -ms-transform: translateX(-50%) translateY(-50%);
  -moz-transform: translateX(-50%) translateY(-50%);
  -webkit-transform: translateX(-50%) translateY(-50%);
  transform: translateX(-50%) translateY(-50%);
}

.video-background-content {
  position: relative;
  z-index: 2;
}

.video-background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: #5bbae8;
  opacity: 0.3;
  z-index: 1;
}
</style>
