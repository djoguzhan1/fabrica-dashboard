import * as THREE from "three";
import manifest from "../assets/layers/manifest.json";
import { easeInOutCubic, spring } from "./easing";

type LayerMeta = {
  file: string;
  pivot: [number, number];
  z: number;
};

const ORDER = [
  "background",
  "hair_back",
  "torso",
  "legs",
  "head",
  "bell_left",
  "bell_right",
] as const;

const W = manifest.size[0];
const H = manifest.size[1];
const ASPECT = W / H;

const app = document.getElementById("app")!;
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.outputColorSpace = THREE.SRGBColorSpace;
app.appendChild(renderer.domElement);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(35, window.innerWidth / window.innerHeight, 0.1, 100);
camera.position.set(0, 0, 4.2);

const rig = new THREE.Group();
scene.add(rig);

const ambient = new THREE.AmbientLight(0xffeedd, 0.55);
const key = new THREE.DirectionalLight(0xffaa88, 0.85);
key.position.set(2, 3, 4);
const rim = new THREE.DirectionalLight(0x88aaff, 0.35);
rim.position.set(-3, 1, -2);
scene.add(ambient, key, rim);

const loader = new THREE.TextureLoader();
const layers: Record<string, THREE.Mesh> = {};
const pivots: Record<string, THREE.Group> = {};

function makeLayer(name: string, meta: LayerMeta): THREE.Group {
  const tex = loader.load(`/${meta.file}`);
  tex.colorSpace = THREE.SRGBColorSpace;
  tex.minFilter = THREE.LinearFilter;
  tex.magFilter = THREE.LinearFilter;

  const geom = new THREE.PlaneGeometry(ASPECT * 2, 2);
  const mat = new THREE.MeshBasicMaterial({
    map: tex,
    transparent: true,
    depthWrite: name === "background",
    side: THREE.DoubleSide,
  });
  const mesh = new THREE.Mesh(geom, mat);
  layers[name] = mesh;

  const pivotN = meta.pivot;
  const px = (pivotN[0] - 0.5) * ASPECT * 2;
  const py = (0.5 - pivotN[1]) * 2;

  const pivot = new THREE.Group();
  pivot.position.set(px, py, meta.z * 0.002);
  mesh.position.set(-px, -py, 0);
  pivot.add(mesh);
  pivots[name] = pivot;
  rig.add(pivot);
  return pivot;
}

for (const name of ORDER) {
  const meta = (manifest.layers as Record<string, LayerMeta>)[name];
  if (meta) makeLayer(name, meta);
}

const mouse = { x: 0, y: 0 };
window.addEventListener("pointermove", (e) => {
  mouse.x = (e.clientX / window.innerWidth - 0.5) * 2;
  mouse.y = (e.clientY / window.innerHeight - 0.5) * 2;
});

let headAngle = 0;
let headVel = 0;
let bellL = { a: 0, v: 0 };
let bellR = { a: 0, v: 0 };
let breath = 0;

const clock = new THREE.Clock();

function animate() {
  requestAnimationFrame(animate);
  const t = clock.getElapsedTime();
  const dt = Math.min(clock.getDelta(), 0.05);

  // Idle cycle ~4s: subtle head look + breathing
  const phase = (t % 4) / 4;
  const headTarget = easeInOutCubic(phase < 0.5 ? phase * 2 : 2 - phase * 2) * 0.06 - 0.03;
  const s = spring(headAngle, headTarget, headVel, 120, 14, dt);
  headAngle = s.value;
  headVel = s.velocity;

  if (pivots.head) pivots.head.rotation.z = headAngle;
  if (pivots.head) pivots.head.rotation.y = mouse.x * 0.04;
  if (pivots.head) pivots.head.rotation.x = -mouse.y * 0.03;

  breath = Math.sin(t * 1.8) * 0.012;
  if (pivots.torso) {
    pivots.torso.scale.set(1 + breath, 1 + breath * 0.6, 1);
  }
  if (pivots.legs) {
    pivots.legs.rotation.x = Math.sin(t * 1.2) * 0.008;
  }
  if (pivots.hair_back) {
    pivots.hair_back.rotation.z = headAngle * 0.35 + Math.sin(t * 0.9) * 0.01;
  }

  const bellTargetL = headAngle * 1.8 + Math.sin(t * 2.3) * 0.05;
  const bellTargetR = headAngle * 1.6 + Math.sin(t * 2.7 + 1) * 0.05;
  const sl = spring(bellL.a, bellTargetL, bellL.v, 220, 12, dt);
  const sr = spring(bellR.a, bellTargetR, bellR.v, 200, 11, dt);
  bellL = { a: sl.value, v: sl.velocity };
  bellR = { a: sr.value, v: sr.velocity };
  if (pivots.bell_left) pivots.bell_left.rotation.z = bellL.a;
  if (pivots.bell_right) pivots.bell_right.rotation.z = bellR.a;

  camera.position.x = mouse.x * 0.08;
  camera.position.y = -mouse.y * 0.05;
  camera.lookAt(0, 0, 0);

  renderer.render(scene, camera);
}

animate();

window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
