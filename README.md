## Fishology 🐟
Welcome to Fishology, an underwater diary website for your mindfulness!

### Background
Fishology was a final year project I created back in 2023 (long, long time ago...)
This repository includes the artifacts of the project.

📺 Watch how Fishology [works](https://www.youtube.com/watch?v=4Odq8R4rbQ8)\
📃 Read the full report 

### Development Overview

**🖼 Front End**  : Vue\
  ***Bootstrap 5***   ：CSS framework that provides design templates for user interface components\
  ***Three.js***      ：Library used to import & process 3D models in webpage\
  ***Chart.js***      ：Library used to visualize data using charts, graph in webpage\
\
**🔨 Backend**    : Django\
**📦 API**        : Axios\
\
**Visual Design**\
  ***Magica Voxel***      : Modelling & export .obj\
  ***Maxon Cinema4D***   : Convert model into .gltf\
  ***Three.js***          : Import model into website\

### HOW TO RUN FISHOLOGY IN YOUR COMPUTER ?

Under ***\fishology_project*** directory, run
```
source env/scripts/activate
```

Under ***\fishology_project\fishology_django*** directory, run
```
python manage.py runserver
```
And leave the server runnning

Under ***\fishology_project\fishology_vue*** directory, run
```
npm run serve
```
And leave server runnning

Not sure anyone reading this, but welcome to Fishology ; )
