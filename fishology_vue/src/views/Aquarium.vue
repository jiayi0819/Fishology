<template>
  <div>
    <Loading v-show="loading" />
    <canvas id="three"></canvas>
    <button
      type="button"
      class="btn btn-light"
      @click="this.openModal('writeDiaryModal')"
      id="btnWrite">
      <i class="fa fa-pencil" aria-hidden="true"></i>
    </button>

    <!-- PANELS -->

    <WriteDiary @diary-added="this.initAquarium()" />
    <ReadDiary :diary="this.openDiary" />
    <Filter @filter-diary="this.reloadDiaries()" />
    <Catalogue @change-scene="changeScene" @change-sky="changeSky" />
    <EditAquarium :aquarium="this.aquarium" />
    <Statistics />
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters, mapActions } from "vuex";
import { toRaw } from "@vue/reactivity";

import * as THREE from "three";
import * as dat from "dat.gui";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

import Catalogue from "../views/Catalogue.vue";
import Loading from "../components/Loading.vue";
import WriteDiary from "../views/WriteDiary.vue";
import ReadDiary from "../views/ReadDiary.vue";
import Filter from "../views/Filter.vue";
import Statistics from "../views/Statistics.vue";
import EditAquarium from "../views/EditAquarium.vue";

export default {
  name: "Aquarium",
  components: {
    Loading,
    Catalogue,
    EditAquarium,
    WriteDiary,
    ReadDiary,
    Filter,
    Statistics,
  },
  computed: {
    ...mapGetters([
      "getFish",
      "getFishes",
      "getDiaries",
      "getDiary",
      "getTotalDiary",
      "getProps",
      "getScenes",
    ]),
  },
  data() {
    return {
      diaryList: [],
      openDiary: Object,
      loading: false,
      aquarium: Object,
    };
  },
  async mounted() {
    // this.initAquarium();
    // this.initializePanels();

    this.fetchAquarium(this.$route.params.aquarium_id).then((resolve) => {
      this.aquarium = resolve;
      console.log(this.aquarium);
      this.initAquarium();
      this.initializePanels();
    });
  },
  methods: {
    ...mapActions([
      "fetchAquarium",
      "fetchDiaries",
      "fetchFishes",
      "fetchMoods",
      "fetchProps",
      "fetchScenes",
      "fetchSkies",
      "fetchWeathers",
      "resetProps",
      "setCurrentAquarium",
      "updateAquariumSky",
      "updateAquariumScene",
      "initializePanels",
      "openModal",
    ]),
    reloadDiaries() {
      this.diaryList = this.$store.getters.getDiaries;
      this.initThree();
    },
    changeScene(sceneName) {
      this.loading = true;

      const payload = {
        sceneName: sceneName,
        id: this.$route.params.aquarium_id,
      };

      this.updateAquariumScene(payload).then((response) => {
        this.aquarium.scene = sceneName;
        this.initAquarium();
        this.loading = false;
      });

      // this.fetchProps(sceneName).then((response) => {
      //   this.initThree();
      //   this.loading = false;
      // });
      // this.initAquarium(sceneName);
    },
    changeSky(mapName) {
      this.loading = true;

      const payload = {
        mapName: mapName,
        id: this.$route.params.aquarium_id,
      };

      this.updateAquariumSky(payload).then((response) => {
        this.aquarium.sky = mapName;
        this.initThree();
        this.loading = false;
      });
    },
    initAquarium(sceneName = this.aquarium.scene) {
      console.log("The scene is " + this.aquarium.scene);
      this.loading = true;
      Promise.all([
        this.fetchDiaries(this.$route.params.aquarium_id),
        this.fetchFishes(),
        this.fetchMoods(),
        this.fetchProps(this.aquarium.scene),
        this.fetchScenes(),
        this.fetchSkies(),
        this.fetchWeathers(),
      ]).then(
        (response) => {
          this.setCurrentAquarium(this.$route.params.aquarium_id),
            (this.diaryList = this.$store.getters.getDiaries);
          this.initThree();
          this.loading = false;
        },
        (error) => {
          console.log("Shit Happens, you know" + error);
        }
      );
    },
    initThree() {
      console.log("init Three");
      const scene = new THREE.Scene();
      const canvas = document.querySelector("#three");
      const gui = new dat.GUI({
        top: 40,
      });

      ///////////////////////////////////
      // PARTICLE
      ///////////////////////////////////

      // Geometry
      const particleGeometry = new THREE.BufferGeometry();
      const count = 3000;

      const positions = new Float32Array(count * 3);

      for (let i = 0; i < count * 3; i++) {
        positions[i] = (Math.random() - 0.5) * 30;
      }

      particleGeometry.setAttribute(
        "position",
        new THREE.BufferAttribute(positions, 3)
      );

      // Material
      const particleMaterial = new THREE.PointsMaterial();
      particleMaterial.size = 1.5;
      particleMaterial.sizeAttenuation = false;

      // Points
      const particles = new THREE.Points(particleGeometry, particleMaterial);
      scene.add(particles);

      ///////////////////////////////////
      // SKY COLOUR
      ///////////////////////////////////

      //   scene.background.setHSL(hsl.hue, hsl.saturation, hsl.lightness);
      // }

      const cubeTextureLoader = new THREE.CubeTextureLoader();

      var time = {
        hour: new Date().getHours(),
        minutes: parseInt(new Date().getHours() * 60 + new Date().getMinutes()),
        sunrise_start: 6,
        sunrise_end: 8,
        sunset_start: 18,
        sunset_end: 21,
      };

      // var mapName = "ocean-dawn";
      var mapName = this.aquarium.sky;
      console.log("THe sky is " + this.aquarium.sky);

      var environmentMap = cubeTextureLoader.load([
        `http://127.0.0.1:8000/media/models/sky/${mapName}/px.png`,
        `http://127.0.0.1:8000/media/models/sky/${mapName}/nx.png`,
        `http://127.0.0.1:8000/media/models/sky/${mapName}/py.png`,
        `http://127.0.0.1:8000/media/models/sky/${mapName}/ny.png`,
        `http://127.0.0.1:8000/media/models/sky/${mapName}/pz.png`,
        `http://127.0.0.1:8000/media/models/sky/${mapName}/nz.png`,
      ]);

      // const environmentMap = cubeTextureLoader.load([
      //   `http://127.0.0.1:8000/media/models/sky/${mapIndex}/px.png`,
      //   `http://127.0.0.1:8000/media/models/sky/${mapIndex}/nx.png`,
      //   `http://127.0.0.1:8000/media/models/sky/${mapIndex}/py.png`,
      //   `http://127.0.0.1:8000/media/models/sky/${mapIndex}/ny.png`,
      //   `http://127.0.0.1:8000/media/models/sky/${mapIndex}/pz.png`,
      //   `http://127.0.0.1:8000/media/models/sky/${mapIndex}/nz.png`,
      // ]);
      environmentMap.encoding = THREE.sRGBEncoding;

      scene.background = environmentMap;

      ///////////////////////////////////
      // RAYCASTER
      ///////////////////////////////////

      const raycaster = new THREE.Raycaster();

      ///////////////////////////////////
      // RESIZE WINDOW
      ///////////////////////////////////

      const sizes = {
        width: window.innerWidth,
        height: window.innerHeight,
      };

      window.addEventListener("resize", () => {
        // Update Sizes
        sizes.width = window.innerWidth;
        sizes.height = window.innerHeight;

        // Update Camera
        camera.aspect = sizes.width / sizes.height;
        camera.updateProjectionMatrix();

        // Update Renderer
        renderer.setSize(sizes.width, sizes.height);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      });

      ///////////////////////////////////
      // Camera
      ///////////////////////////////////

      // var axesHelper = new THREE.AxesHelper(5);
      // scene.add(axesHelper);

      const camera = new THREE.PerspectiveCamera(
        50,
        sizes.width / sizes.height,
        0.1,
        100
      );
      camera.position.y = 1;
      camera.position.z = 12;

      camera.fov = 40;
      scene.add(camera);

      const camFolder = gui.addFolder("Cam");

      for (var axis of ["x", "y", "z"]) {
        camFolder
          .add(camera.position, axis)
          .max(50)
          .min(-50)
          .step(0.01)
          .name(`camera-${axis}`)
          .onChange(function () {
            camera.updateProjectionMatrix();
          });
      }

      camFolder
        .add(camera, "fov")
        .max(100)
        .min(10)
        .step(0.01)
        .name("camera-fov")
        .onChange(function () {
          camera.updateProjectionMatrix();
        });

      ///////////////////////////
      // CONTROL
      ///////////////////////////

      const controls = new OrbitControls(camera, canvas);
      controls.enableDamping = true;
      controls.enablePan = false;
      controls.minDistance = 10;
      controls.maxDistance = 20;
      controls.update();

      ///////////////////////////
      // RENDERER
      ///////////////////////////

      const renderer = new THREE.WebGLRenderer({
        canvas: canvas,
      });
      renderer.physicallyCorrectLights = true;
      renderer.setSize(sizes.width, sizes.height);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.outputEncoding = THREE.sRGBEncoding;
      renderer.toneMapping = THREE.ACESFilmicToneMapping;

      gui
        .add(renderer, "toneMapping", {
          No: THREE.NoToneMapping,
          Linear: THREE.LinearToneMapping,
          Reihhard: THREE.ReihhardToneMapping,
          Cineon: THREE.CineonToneMapping,
          ACESFilmic: THREE.ACESFilmicMapping,
        })
        .onFinishChange(() => {
          renderer.toneMapping = Number(renderer.toneMapping);
        });

      ///////////////////////////////////
      // LIGHT
      ///////////////////////////////////

      const ambientLight = new THREE.AmbientLight(0xffffff, 0.3);
      scene.add(ambientLight);

      gui
        .add(ambientLight, "intensity")
        .min(0)
        .max(10)
        .step(0.001)
        .name("amb-int");

      const directionalLight1 = new THREE.DirectionalLight("#ffffff", 0.7);
      directionalLight1.position.set(-1.7, 1.5, 2.5);
      directionalLight1.castShadow = true;
      directionalLight1.shadow.camera.far = 15;
      directionalLight1.shadow.mapSize.set(1024, 1024);
      directionalLight1.shadow.normalBias = 0.05;
      scene.add(directionalLight1);

      const directLFolder = gui.addFolder("directL");

      directLFolder
        .add(directionalLight1, "intensity")
        .min(0)
        .max(10)
        .step(0.001)
        .name("lightIntensity");

      for (var axis of ["x", "y", "z"]) {
        directLFolder
          .add(directionalLight1.position, axis)
          .min(-50)
          .max(50)
          .step(0.001)
          .name(`light-${axis}`);
      }

      const directionalLight2 = new THREE.DirectionalLight("#ffffff", 0.7);
      directionalLight2.position.set(-6, 35, 11.5);
      directionalLight2.castShadow = true;
      directionalLight2.shadow.camera.far = 15;
      directionalLight2.shadow.mapSize.set(1024, 1024);
      directionalLight2.shadow.normalBias = 0.05;
      scene.add(directionalLight2);

      const directLFolder2 = gui.addFolder("directL2");

      directLFolder2
        .add(directionalLight2, "intensity")
        .min(0)
        .max(10)
        .step(0.001)
        .name("lightIntensity");

      for (var axis of ["x", "y", "z"]) {
        directLFolder2
          .add(directionalLight2.position, axis)
          .min(-50)
          .max(50)
          .step(0.001)
          .name(`light-${axis}`);
      }

      // HELPER
      // const helper = new THREE.DirectionalLightHelper(directionalLight2, 0.2);
      // scene.add(helper);

      ///////////////////////////////////
      // FISH 🐟
      ///////////////////////////////////

      const Fish = function (direction, speed, diary) {
        this.direction = direction;
        this.speed = speed;
        this.diary = diary;
      };

      const fishArray = [];
      const fishBodyArray = [];
      var intersects = [];

      // MODEL 🎈
      const gltfLoader = new GLTFLoader();

      // var randomIndex = Math.floor(Math.random() * this.diaryList.length);
      // MAXIMUM NO. OF FISH: ?

      for (const diary of this.diaryList) {
        console.log("Make a fish!");
        diary.fishLoaded = true;
        generateFish(diary, this.getFish(diary.fish).get_model);
      }

      async function loadFishModel(fishModel) {
        return new Promise((resolve) => {
          gltfLoader.load(fishModel, resolve);
        });
      }

      function loadModel(model_path) {
        return new Promise((resolve) => {
          gltfLoader.load(model_path, resolve);
        });
      }

      ///////////////////////////////////
      // LOAD AQUARIUM ISLAND
      ///////////////////////////////////

      console.log(this.$store.getters.getScenes);

      var propList;
      const that = this;

      async function buildAquarium() {
        propList = that.$store.getters.getProps;

        for (const prop of propList) {
          var gltf = await loadModel(prop.get_model);
          prop.mesh = gltf.scene;

          prop.mesh.traverse(function (node) {
            // ignore bones and other nodes without any material
            if (!node.material) return;

            // keep the reference to the old material - we want to dispose it later
            var tmp = node.material;
            // substitute the material
            node.material = new THREE.MeshStandardMaterial({
              skinning: true, // the original material is using skinning
              map: node.material.map, // we want the original texture
            });
            // update and clean up
            node.material.needsUpdate = true;
            tmp.dispose();
          });

          prop.mesh.position.x = parseInt(prop.x);
          prop.mesh.position.y = parseInt(prop.y);
          prop.mesh.position.z = parseInt(prop.z);

          scene.add(toRaw(prop.mesh));

          const folder = gui.addFolder(prop.name);

          for (var axis of ["x", "y", "z"]) {
            folder
              .add(prop.mesh.position, axis)
              .max(30)
              .min(-30)
              .step(0.1)
              .name(`${prop.name}-${axis}`);
          }
        }
      }

      buildAquarium();

      ///////////////////////////////////
      // CREATE NEW FISH ✨
      ///////////////////////////////////

      async function generateFish(diary, model) {
        // const fishBody = new THREE.Mesh(fishGeometry, fishMaterial);

        const direction = Math.random() < 0.5 ? -1 : 1;
        const speed = Math.random() + 0.25;

        let gltf = await loadFishModel(model);

        ///////////// TESTING ///////////

        var testFish = {};
        testFish.direction = direction;
        testFish.speed = speed;
        testFish.diary = diary;
        testFish.body = gltf.scene;
        testFish.body.children[0].userData = {
          diary: diary,
          direction: direction,
          speed: speed,
        };

        testFish.body.traverse(function (node) {
          // ignore bones and other nodes without any material
          if (!node.material) return;

          // keep the reference to the old material - we want to dispose it later
          var tmp = node.material;
          // substitute the material
          node.material = new THREE.MeshStandardMaterial({
            skinning: true, // the original material is using skinning
            map: node.material.map, // we want the original texture
          });
          // update and clean up
          node.material.needsUpdate = true;
          tmp.dispose();
        });

        testFish.body.castShadow = true;
        testFish.body.receiveShadow = true;

        testFish.body.position.x =
          direction == -1
            ? (camera.position.z * sizes.width) / sizes.height
            : -(camera.position.z * sizes.width) / sizes.height;

        testFish.body.position.y = (Math.random() - 0.5) * 6;
        testFish.body.position.z = (Math.random() - 0.5) * 2;

        testFish.body.rotation.y =
          direction == -1 ? Math.PI * 1.5 : Math.PI * 0.5;

        fishArray.push(testFish);
        scene.add(testFish.body);
      }

      ///////////////////////////////////
      // UPDATE MATERIAL SCENE
      ///////////////////////////////////

      const updateAllMaterials = () => {
        scene.traverse((child) => {
          if (
            child instanceof THREE.Mesh &&
            child.material instanceof THREE.MeshStandardMaterial
          ) {
            console.log("Aloha");
            child.material.envMap = environmentMap;
            child.material.envMapIntensity = 5;
          }
        });
      };

      // updateAllMaterials();

      //////////////////////////////////////
      // MOUSE MOVEMENT 🐁
      //////////////////////////////////////

      const mouse = new THREE.Vector2();

      const cursor = {
        x: 0,
        y: 0,
      };

      window.addEventListener("mousemove", (event) => {
        mouse.x = (event.clientX / sizes.width) * 2 - 1;
        mouse.y = -(event.clientY / sizes.width) * 2 + 1;

        ////////////////////

        var rect = canvas.getBoundingClientRect();

        cursor.x = ((event.clientX - rect.left) / sizes.width) * 2 - 1;
        cursor.y = -((event.clientY - rect.top) / sizes.height) * 2 + 1;
      });

      window.addEventListener("click", () => {
        if (intersects.length != 0 && !this.$store.state.modalOpened) {
          console.log("Should open diary");
          this.openDiary = intersects[0].object.userData.diary;
          this.openModal("readDiaryModal");
        }
      });

      function animate() {
        controls.update();
        renderer.render(scene, camera);
        requestAnimationFrame(animate);
      }

      //////////////////////////////////////
      // ANIMATIONS
      //////////////////////////////////////

      // CLOCK
      const clock = new THREE.Clock();
      var deltaTime = 0;
      var currentFish = [];

      const tick = () => {
        // const elapsedTime = clock.getElapsedTime();
        deltaTime = clock.getDelta();

        // UPDATE SKY COLOUR
        // time.minutes = parseInt(
        //   new Date().getHours() * 60 + new Date().getMinutes()
        // );
        // skyPainter();

        /////////////////////////////
        // UPDATE CAMERA
        /////////////////////////////
        camera.position.x = cursor.x * 3;
        camera.position.y = cursor.y * 3;
        camera.updateProjectionMatrix();

        /////////////////////////////
        // ANIMATE MOUNTAIN
        /////////////////////////////
        propList.forEach((prop, id) => {
          if (prop.mesh) {
            if (prop.min_x != prop.max_x) {
              var movement = Math.sin(
                clock.getElapsedTime() * (prop.max_x - prop.min_x) * 0.2
              );
              prop.mesh.position.x = movement;
            }
          }
        });

        /////////////////////////////
        // ANIMATE PARTICLE ⚪
        /////////////////////////////

        for (let i = 0; i < count; i++) {
          const i3 = i * 3;
        }

        particles.rotation.x = clock.getElapsedTime() * 0.15;
        particles.rotation.y = clock.getElapsedTime() * 0.15;
        particles.rotation.z = clock.getElapsedTime() * 0.15;

        /////////////////////////////
        // UPDATE FISH
        /////////////////////////////

        fishArray.forEach((fish, id) => {
          if (
            fish.body.position.x >
              (camera.position.z * sizes.width) / sizes.height ||
            fish.body.position.x <
              -((camera.position.z * sizes.width) / sizes.height)
          ) {
            // REMOVE MODEL
            scene.remove(fish.body);

            // RESET 'LOADED' RECORD
            var fishIndex = this.diaryList.findIndex(
              (diary) => diary.id == fishArray[id].diary.id
            );
            this.diaryList[fishIndex].fishLoaded = false;

            // COMPLETE REMOVE
            fishArray.splice(id, 1);
          } else {
            fish.body.position.x += deltaTime * fish.speed * fish.direction;
          }

          // REGENERATE FISH

          // var randomIndex = Math.floor(Math.random() * this.diaryList.length);

          // if(!diaryList[randomIndex].fishLoaded){
          //   generateFish(diary, this.getFish(diary.fish).get_model);
          //   diary.fishLoaded = true;
          // }

          // console.log(
          //   "Total Fish now: " +
          //     this.diaryList.filter((diary) => diary.fishLoaded).length
          // );

          if (this.diaryList.filter((diary) => diary.fishLoaded).length < 20) {
            for (const diary of this.diaryList) {
              if (!diary.fishLoaded) {
                generateFish(diary, this.getFish(diary.fish).get_model);
                diary.fishLoaded = true;
              }
            }
          }
        });

        // RAYCASTER

        raycaster.setFromCamera(cursor, camera);
        intersects = raycaster.intersectObjects(
          fishArray.map((fish) => fish.body)
        );

        // UPDATE CONTROLS
        controls.update();

        // RENDER
        renderer.render(scene, camera);

        window.requestAnimationFrame(tick);
      };
      tick();
    },
  },
};
</script>

<style scoped>
#three {
  display: block;
  height: 100vh;
}

#btnWrite {
  position: fixed;
  bottom: 20px;
  right: 20px;
}
</style>
