import * as THREE from "three";
import manifest from "../assets/layers/manifest.json";
import { easeInOutCubic, spring } from "./easing";

type LayerMeta = {
  file: string;
  pivot: [number, number];
  z: number;
};

const ROOT_LAYERS = [
  "background",
  "hair_back",
  "arm_l_upper",
  "arm_r_upper",
  "torso",
  "legs",
  "head",
  "bell_left",
  "bell_right",
] as const;

const W = manifest.size[0];
const H = manifest.size[1];
const ASPECT = W / H;

function normToLocal(nx: number, ny: number): THREE.Vector3 {
  return new THREE.Vector3((nx - 0.5) * ASPECT * 2, (0.5 - ny) * 2, 0);
}

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
const pivots: Record<string, THREE.Group> = {};

function makeLayer(
  name: string,
  meta: LayerMeta,
  parent: THREE.Object3D = rig,
  pivotAtParentOrigin = parent === rig,
): THREE.Group {
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

  const pivotN = meta.pivot;
  const local = normToLocal(pivotN[0], pivotN[1]);
  const pivot = new THREE.Group();
  if (pivotAtParentOrigin) {
    pivot.position.set(local.x, local.y, meta.z * 0.002);
  } else {
    pivot.position.set(0, 0, meta.z * 0.002);
  }
  mesh.position.set(-local.x, -local.y, 0);
  pivot.add(mesh);
  parent.add(pivot);
  pivots[name] = pivot;
  return pivot;
}

const layersMeta = manifest.layers as Record<string, LayerMeta>;

for (const name of ROOT_LAYERS) {
  const meta = layersMeta[name];
  if (meta) makeLayer(name, meta);
}

function linkForearm(upper: string, lower: string) {
  const upperMeta = layersMeta[upper];
  const lowerMeta = layersMeta[lower];
  if (!upperMeta || !lowerMeta) return;
  const upperPivot = pivots[upper];
  if (!upperPivot) return;

  const shoulder = normToLocal(upperMeta.pivot[0], upperMeta.pivot[1]);
  const elbow = normToLocal(lowerMeta.pivot[0], lowerMeta.pivot[1]);
  const elbowHolder = new THREE.Group();
  elbowHolder.position.set(elbow.x - shoulder.x, elbow.y - shoulder.y, 0.003);
  upperPivot.add(elbowHolder);
  makeLayer(lower, lowerMeta, elbowHolder, false);
}

linkForearm("arm_l_upper", "arm_l_lower");
linkForearm("arm_r_upper", "arm_r_lower");

const mouse = { x: 0, y: 0 };
window.addEventListener("pointermove", (e) => {
  mouse.x = (e.clientX / window.innerWidth - 0.5) * 2;
  mouse.y = (e.clientY / window.innerHeight - 0.5) * 2;
});

let headAngle = 0;
let headVel = 0;
let bellL = { a: 0, v: 0 };
let bellR = { a: 0, v: 0 };
let armLU = { a: 0, v: 0 };
let armLL = { a: 0, v: 0 };
let armRU = { a: 0, v: 0 };
let armRL = { a: 0, v: 0 };

const clock = new THREE.Clock();

function animate() {
  requestAnimationFrame(animate);
  const t = clock.getElapsedTime();
  const dt = Math.min(clock.getDelta(), 0.05);

  const phase = (t % 4) / 4;
  const headTarget = easeInOutCubic(phase < 0.5 ? phase * 2 : 2 - phase * 2) * 0.06 - 0.03;
  const hs = spring(headAngle, headTarget, headVel, 120, 14, dt);
  headAngle = hs.value;
  headVel = hs.velocity;

  if (pivots.head) {
    pivots.head.rotation.z = headAngle;
    pivots.head.rotation.y = mouse.x * 0.04;
    pivots.head.rotation.x = -mouse.y * 0.03;
  }

  const breath = Math.sin(t * 1.8) * 0.012;
  if (pivots.torso) {
    pivots.torso.scale.set(1 + breath, 1 + breath * 0.6, 1);
    pivots.torso.rotation.z = headAngle * 0.15 + Math.sin(t * 1.4) * 0.004;
  }
  if (pivots.legs) {
    const sway = Math.sin(t * 1.1) * 0.012;
    pivots.legs.rotation.z = sway;
    pivots.legs.position.x = sway * 0.02;
  }
  if (pivots.hair_back) {
    pivots.hair_back.rotation.z = headAngle * 0.4 + Math.sin(t * 0.85) * 0.018;
    pivots.hair_back.rotation.x = Math.sin(t * 0.7) * 0.006;
  }

  // ~5s loop: smooth arm raise (screen-left arm lifts toward viewer)
  const armPhase = (t % 5) / 5;
  const lift = armPhase < 0.45 ? easeInOutCubic(armPhase / 0.45) : easeInOutCubic((1 - armPhase) / 0.55);
  const upperTarget = -lift * 0.95;
  const lowerTarget = -lift * 0.55;

  const slU = spring(armLU.a, upperTarget, armLU.v, 160, 16, dt);
  const slL = spring(armLL.a, lowerTarget, armLL.v, 140, 14, dt);
  armLU = { a: slU.value, v: slU.velocity };
  armLL = { a: slL.value, v: slL.velocity };
  if (pivots.arm_l_upper) pivots.arm_l_upper.rotation.z = armLU.a;
  if (pivots.arm_l_lower) pivots.arm_l_lower.rotation.z = armLL.a;

  const srU = spring(armRU.a, upperTarget * 0.35, armRU.v, 150, 15, dt);
  const srL = spring(armRL.a, lowerTarget * 0.25, armRL.v, 130, 13, dt);
  armRU = { a: srU.value, v: srU.velocity };
  armRL = { a: srL.value, v: srL.velocity };
  if (pivots.arm_r_upper) pivots.arm_r_upper.rotation.z = -armRU.a;
  if (pivots.arm_r_lower) pivots.arm_r_lower.rotation.z = -armRL.a;

  const bellTargetL = headAngle * 1.8 + Math.sin(t * 2.3) * 0.05;
  const bellTargetR = headAngle * 1.6 + Math.sin(t * 2.7 + 1) * 0.05;
  const bl = spring(bellL.a, bellTargetL, bellL.v, 220, 12, dt);
  const br = spring(bellR.a, bellTargetR, bellR.v, 200, 11, dt);
  bellL = { a: bl.value, v: bl.velocity };
  bellR = { a: br.value, v: br.velocity };
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
