## Fishology 🐟
Welcome to Fishology, an underwater diary website for your mindfulness!

In Fishology, we symbolize a user’s diary space as their aquarium, and when they submit a diary,
it will turn into a fish in their aquarium.


>📺 ***Watch how Fishology [works](https://www.youtube.com/watch?v=4Odq8R4rbQ8)***

>📃 Read the full [report](Fishology_Report.pdf)


### HOW TO RUN FISHOLOGY LOCALLY IN YOUR COMPUTER ?

Under ***\fishology_project*** directory, run below commands
```
source env/scripts/activate
```

Under ***\fishology_project\fishology_django*** directory, run below commands and leave the server runnning
```
python manage.py runserver
```

Under ***\fishology_project\fishology_vue*** directory, run below commands and leave the server runnning
```
npm run serve
```

## Background ⛓
>Fishology was a final year project I created back in 2023 (long, long time ago...)\
>This repository includes the artifacts of the project.

We redefine how users can store, read, and write their diaries, besides turning their diary space into an
immersive and beautiful underwater scene.

This project can be treated as an experiment to probe new ways of user interaction with their
diary records created on the internet besides providing users a small breathing space to regain
their mindfulness.

## Features 🔮
**Visualize your Memories in a Healing Aquarium 🌊**
- Transform diary writing into a healing 3D aquarium experience, where your memories flow
- Past diaries rendered as sea creatures for users to interact and unwind

**Unlock Collectible Sea Creatures for your Aquarium as you write 🐠**
- The more diaries you have written, the more variety of sea creatures you unlock in your aquarium!
- Check out catalogue of sea creatures and the required number of diaries to unlock them

**Powerful Diary Filter 🔎**
- Pick out only your sweet and sour fishes in your aquarium
- View analytics of mood changes in your diaries over time

**More Rewarding Features 🎁**
- Unlock new aquarium props and scenes by writing more diaries!

**Swim Together 🐟🐟**
- Share aquarium with your love ones, a secret aquarium where our fish swim together 🧀

## Development Overview

**🖼 Front End**  : Vue
- ***Bootstrap 5***   ：CSS framework that provides design templates for user interface components
- ***Three.js***      ：Library used to import & process 3D models in webpage
- ***Chart.js***      ：Library used to visualize data using charts, graph in webpage

**🔨 Backend**    : Django
- **📦 API**        : Axios was used to transfer data between backend and frontend

**🌷 Visual Design**
- ***Magica Voxel***      : Modelling & export .obj
- ***Maxon Cinema4D***    : Convert model into .gltf
- ***Three.js***          : Import model into website

Not sure if anyone reading this, but welcome to Fishology ; )
