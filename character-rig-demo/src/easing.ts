/** Smooth step for animation curves (no linear robotic motion). */
export function easeInOutCubic(t: number): number {
  return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

export function easeOutCubic(t: number): number {
  return 1 - Math.pow(1 - t, 3);
}

/** Critically damped spring toward target (0 = at rest). */
export function spring(
  current: number,
  target: number,
  velocity: number,
  stiffness = 180,
  damping = 18,
  dt: number,
): { value: number; velocity: number } {
  const force = -stiffness * (current - target) - damping * velocity;
  const v = velocity + force * dt;
  const x = current + v * dt;
  return { value: x, velocity: v };
}
