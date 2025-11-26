# 3D Clock Animation – Real-Time Rotation (Maya + Python)

This project is a fully modeled and animated **3D analog clock** created using **Autodesk Maya**, 
**Python (maya.cmds)** scripting, and **Arnold Renderer**. It was developed as part of the 
**Graphics and Visual Computing (GVC)** course.

The clock features:
- Real-time rotation of hour, minute, and second hands based on system time  
- Procedurally generated hour markers using trigonometric placement  
- Physically-based materials (Arnold aiStandardSurface)  
- Studio-style lighting using Skydome and Area lights  
- Accurate modeling, transformations, shading, and rendering pipeline  

This repository includes:
- Maya project files  
- Python scripts for markers and real-time animation  
- Rendered animation video  
- Screenshots and workflow documentation  
- Project PPT with voice-over  

## ✨ Features

- ✔ Real-time animation using Python script
- ✔ Procedural generation of hour markers (sin/cos mathematical placement)
- ✔ Fully modeled clock: face, hands, pin, hour markers
- ✔ Correct pivot alignment for smooth rotation
- ✔ Arnold-based physically accurate lighting
- ✔ 1080p rendering (240-frame animation)
- ✔ Organized Maya hierarchy and clean transforms
- ✔ Includes GVC theory: 3D Viewing Pipeline, Z-buffer, Frame-buffer, etc.

## 🛠 Workflow Overview

### 1. Modeling
- Created clock face using polyCylinder
- Modeled hands and pin, adjusted scale and pivot
- Added 12 hour markers using Python automation
- Grouped hands under individual pivot groups

### 2. Transformations
- Applied translation, rotation, scaling
- Freeze transformations for clean hierarchy
- Correct parent-child relationships for animation

### 3. Shading & Texturing
- Applied Arnold aiStandardSurface materials:
  - Clock face: matte grey
  - Hour/minute hand: dark metal
  - Second hand: glossy red
  - Markers: dark metallic

### 4. Lighting
- Added Skydome light for global illumination
- Added Area light for highlight and shadows
- Adjusted exposure and rotation

### 5. Animation
- Python script reads system time
- Updates clock hand rotation every frame
- Baked animation to 240 frames for rendering

### 6. Rendering
- Arnold renderer at 1080p resolution
- 1–240 frame range (24 FPS)
- Output rendered as PNG sequence
- Assembled into video using Clipchamp

## 🧩 Python Scripts

### • Hour Marker Generation
Creates 12 evenly spaced markers around the clock face.

### • Real-Time Clock Animation
Reads system time and rotates hour/minute/second hand accordingly.
Uses scriptJob for continuous updates.

All scripts are included in the directory.

## 🚧 Challenges Faced

- Marker alignment issues due to rotation errors
- Fixing pivot placement for hands
- Real-time animation not running during render
- Lighting was too bright/dark initially
- Long render time for 240 frames

## 📈 Scope for Improvement

- Add glass cover using transparency shader
- Add environment or wall mount
- Add motion blur for second hand
- Export the clock for AR/VR using Unity
- Add sound effects for ticking

## 📚 References

- Autodesk Maya Documentation
- Arnold Renderer Documentation
- StackOverflow (maya.cmds discussions)
- YouTube (Maya lighting & materials)
- ChatGPT assistance for logic and scripting

<img width="1919" height="1022" alt="3dclock" src="https://github.com/user-attachments/assets/9765ed6b-2f82-41a5-94c3-63192d6892d5" />
