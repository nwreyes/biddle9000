"use client";

import VideoPlayer from "./VideoPlayer";
import KatexSpan from "./KatexSpan";

const quadraticEquationTest = `Given a general quadratic equation of the form
$$ax^{2} + bx + c = 0$$
with $x$ representing an unknown, with $a$, $b$ and $c$ representing constants, and with $a \\ne 0$, the quadratic formula is:
$$x = \\frac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}$$`;

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24 gap-4">
      <VideoPlayer/>
      <KatexSpan text={quadraticEquationTest} />
    </main>
  );
}
